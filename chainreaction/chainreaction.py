from __future__ import annotations

import asyncio
import random
import re
import time
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import discord
from redbot.core import commands, Config
from redbot.core.bot import Red

from wordfreq import zipf_frequency


WORD_RE = re.compile(r"^[A-Za-z]{2,30}$")  # real-word check uses wordfreq; keep input clean


@dataclass
class Rule:
    key: str
    title: str
    text: str


class LobbyView(discord.ui.View):
    def __init__(self, cog: "ChainReaction", guild_id: int, channel_id: int):
        super().__init__(timeout=None)
        self.cog = cog
        self.guild_id = guild_id
        self.channel_id = channel_id

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if not interaction.guild or interaction.guild.id != self.guild_id:
            return False
        if interaction.channel_id != self.channel_id:
            await interaction.response.send_message("Use the Join button in the lobby channel.", ephemeral=True)
            return False
        return True

    @discord.ui.button(label="Join", style=discord.ButtonStyle.success, emoji="🧪")
    async def join(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.cog._lobby_join(interaction)


class ChainReaction(commands.Cog):
    """Turn-based ChainReaction with a Join lobby, lives, and a 10-second countdown turn."""

    __author__ = "Gabi"
    __version__ = "2.1.0"

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=884_219_337_501, force_registration=True)

        default_guild = {"active_games": {}}  # channel_id(str) -> game dict
        default_member = {"wins": 0, "games_played": 0, "eliminations": 0}

        self.config.register_guild(**default_guild)
        self.config.register_member(**default_member)

        # runtime tasks: (guild_id, channel_id) -> task
        self._tasks: Dict[Tuple[int, int], asyncio.Task] = {}

        # lightweight per-channel lock to avoid edit races (join spam + countdown edits)
        self._locks: Dict[Tuple[int, int], asyncio.Lock] = {}

    # -------------------- utilities --------------------

    def _lock(self, guild_id: int, channel_id: int) -> asyncio.Lock:
        key = (guild_id, channel_id)
        if key not in self._locks:
            self._locks[key] = asyncio.Lock()
        return self._locks[key]

    def _normalize(self, word: str) -> str:
        return word.strip().lower()

    def _is_real_word(self, word: str) -> bool:
        # zipf > 0 => present in wordfreq lexicon
        return zipf_frequency(word.lower(), "en") > 0.0

    def _basic_validate(self, word: str) -> Optional[str]:
        w = word.strip()
        if not WORD_RE.match(w):
            return "Must be a single word (A–Z only), 2–30 letters."
        return None

    def _pick_rule(self, last_word: Optional[str]) -> Dict[str, Any]:
        rules = ["minlen", "contains", "endletter", "norepeat", "startslast"]
        key = random.choice(rules)
        if key == "startslast" and not last_word:
            key = "minlen"

        data: Dict[str, Any] = {"key": key}
        if key == "minlen":
            data["minlen"] = random.choice([4, 5, 6])
        elif key == "contains":
            data["need"] = random.choice(["ae", "sh", "ph", "oo", "st", "cr", "th", "ing"])
        elif key == "endletter":
            data["end"] = random.choice(list("tnrlyse"))
        elif key == "norepeat":
            pass
        elif key == "startslast":
            n = random.choice([1, 2, 2, 3])  # bias toward 2
            data["n"] = n
            data["prefix"] = last_word[-n:]
        return data

    def _rule_display(self, rule: Dict[str, Any]) -> Rule:
        key = rule["key"]
        if key == "minlen":
            return Rule(key, "Minimum length", f"Word must be **{rule['minlen']}+** letters.")
        if key == "contains":
            return Rule(key, "Contains", f"Word must contain **{rule['need'].upper()}**.")
        if key == "endletter":
            return Rule(key, "Ends with", f"Word must end with **{rule['end'].upper()}**.")
        if key == "norepeat":
            return Rule(key, "No repeats", "No letter may appear twice.")
        if key == "startslast":
            return Rule(key, "Chain prefix", f"Word must start with **{rule['prefix'].upper()}**.")
        return Rule(key, "Rule", "Do the thing.")

    def _check_rule(self, rule: Dict[str, Any], word: str) -> bool:
        w = self._normalize(word)
        key = rule["key"]
        if key == "minlen":
            return len(w) >= int(rule["minlen"])
        if key == "contains":
            return rule["need"] in w
        if key == "endletter":
            return w.endswith(rule["end"])
        if key == "norepeat":
            return len(set(w)) == len(w)
        if key == "startslast":
            return w.startswith(rule["prefix"])
        return True

    async def _get_game(self, guild: discord.Guild, channel_id: int) -> Optional[Dict[str, Any]]:
        data = await self.config.guild(guild).active_games()
        return data.get(str(channel_id))

    async def _set_game(self, guild: discord.Guild, channel_id: int, game: Optional[Dict[str, Any]]) -> None:
        async with self.config.guild(guild).active_games() as data:
            k = str(channel_id)
            if game is None:
                data.pop(k, None)
            else:
                data[k] = game

    def _task_key(self, guild_id: int, channel_id: int) -> Tuple[int, int]:
        return (guild_id, channel_id)

    async def _safe_edit(self, msg: discord.Message, *, embed: discord.Embed, view: Optional[discord.ui.View] = None):
        try:
            await msg.edit(embed=embed, view=view)
        except Exception:
            pass

    # -------------------- embeds --------------------

    def _lobby_embed(self, channel: discord.TextChannel, game: Dict[str, Any]) -> discord.Embed:
        players: List[int] = game.get("players", [])
        host_id = int(game["host_id"])
        remaining = int(game.get("lobby_seconds_left", 60))

        e = discord.Embed(
            title="🧪 ChainReaction Lobby",
            description=(
                "Click **Join** to enter.\n\n"
                "**Auto-starts in:** "
                f"⏳ **{remaining}s**\n\n"
                "**Rules:** turn-based • 10 seconds per turn • real words only • 3 lives • last one standing wins"
            ),
            color=discord.Color.blurple(),
        )
        e.add_field(name="Host", value=f"<@{host_id}>", inline=True)
        e.add_field(name="Players Joined", value=f"**{len(players)}**", inline=True)
        e.add_field(name="Minimum to start", value="**2**", inline=True)

        if players:
            names = "\n".join([f"{i+1}. <@{uid}>" for i, uid in enumerate(players[:25])])
            if len(players) > 25:
                names += f"\n… +{len(players)-25} more"
            e.add_field(name="Turn Order", value=names, inline=False)
        else:
            e.add_field(name="Turn Order", value="*(no one yet — be brave)*", inline=False)

        e.set_footer(text="Only joined players can submit words.")
        return e

    def _turn_embed(
        self,
        game: Dict[str, Any],
        player_id: int,
        rule: Dict[str, Any],
        seconds_left: int,
        last_word: Optional[str],
        feedback: str,
    ) -> discord.Embed:
        rd = self._rule_display(rule)
        lives = int(game["lives"].get(str(player_id), 0))

        e = discord.Embed(
            title="⚡ ChainReaction Turn",
            description=f"It's <@{player_id}>'s turn.",
            color=discord.Color.gold(),
        )
        e.add_field(name="Rule", value=f"**{rd.title}:** {rd.text}", inline=False)
        e.add_field(name="Lives", value="❤️ " * lives + f"({lives}/3)", inline=True)
        e.add_field(name="Time", value=f"⏳ **{seconds_left}s**", inline=True)

        if last_word:
            e.add_field(name="Last accepted word", value=f"**{last_word.upper()}**", inline=False)
        else:
            e.add_field(name="Last accepted word", value="*(none yet)*", inline=False)

        if feedback:
            e.add_field(name="Last attempt", value=feedback, inline=False)

        e.set_footer(text="Send a word message in chat. You can retry until time runs out.")
        return e

    def _announce_embed(self, title: str, text: str, color: discord.Color) -> discord.Embed:
        return discord.Embed(title=title, description=text, color=color)

    # -------------------- lobby join --------------------

    async def _lobby_join(self, interaction: discord.Interaction):
        guild = interaction.guild
        if guild is None:
            return
        channel = interaction.channel
        if not isinstance(channel, discord.TextChannel):
            await interaction.response.send_message("This game needs a text channel.", ephemeral=True)
            return

        async with self._lock(guild.id, channel.id):
            game = await self._get_game(guild, channel.id)
            if not game or game.get("phase") != "lobby":
                await interaction.response.send_message("No active lobby in this channel.", ephemeral=True)
                return

            uid = interaction.user.id
            players: List[int] = game.get("players", [])

            if uid in players:
                await interaction.response.send_message("You’re already in.", ephemeral=True)
                return

            players.append(uid)
            game["players"] = players
            game["lives"][str(uid)] = 3

            await self._set_game(guild, channel.id, game)

            # update lobby embed immediately
            try:
                msg = await channel.fetch_message(int(game["lobby_message_id"]))
                await self._safe_edit(
                    msg,
                    embed=self._lobby_embed(channel, game),
                    view=LobbyView(self, guild.id, channel.id),
                )
            except Exception:
                pass

        await interaction.response.send_message("✅ Joined. Stretch your brain cells.", ephemeral=True)

    # -------------------- lobby countdown + start --------------------

    async def _run_lobby_countdown(self, guild_id: int, channel_id: int):
        guild = self.bot.get_guild(guild_id)
        if guild is None:
            return
        channel = guild.get_channel(channel_id)
        if not isinstance(channel, discord.TextChannel):
            return

        for remaining in range(60, -1, -1):
            async with self._lock(guild_id, channel_id):
                game = await self._get_game(guild, channel_id)
                if not game or game.get("phase") != "lobby":
                    return

                game["lobby_seconds_left"] = remaining
                await self._set_game(guild, channel_id, game)

                # edit lobby message
                try:
                    msg = await channel.fetch_message(int(game["lobby_message_id"]))
                    await self._safe_edit(
                        msg,
                        embed=self._lobby_embed(channel, game),
                        view=LobbyView(self, guild_id, channel_id),
                    )
                except Exception:
                    pass

            await asyncio.sleep(1)

        # time's up: start if >=2 players
        async with self._lock(guild_id, channel_id):
            game = await self._get_game(guild, channel_id)
            if not game or game.get("phase") != "lobby":
                return

            players: List[int] = game.get("players", [])
            if len(players) < 2:
                # disable button by removing view
                try:
                    msg = await channel.fetch_message(int(game["lobby_message_id"]))
                    await msg.edit(embed=self._lobby_embed(channel, game), view=None)
                except Exception:
                    pass

                await channel.send(embed=self._announce_embed(
                    "😔 Not enough players",
                    "Lobby closed. Need **at least 2** players to start.",
                    discord.Color.orange(),
                ))
                await self._set_game(guild, channel_id, None)
                return

            # start game
            await self._start_game(guild, channel, game)

    async def _start_game(self, guild: discord.Guild, channel: discord.TextChannel, game: Dict[str, Any]):
        game["phase"] = "running"
        game["current_index"] = 0
        game["last_word"] = ""
        game["turn_rule"] = None
        game["turn_message_id"] = None

        await self._set_game(guild, channel.id, game)

        # disable lobby button
        try:
            msg = await channel.fetch_message(int(game["lobby_message_id"]))
            await msg.edit(embed=self._lobby_embed(channel, game), view=None)
        except Exception:
            pass

        await channel.send(embed=self._announce_embed(
            "🚦 Game started!",
            f"Players: {len(game.get('players', []))}. Turn order is join order. Good luck, nerds.",
            discord.Color.green(),
        ))

        # kick off game loop
        key = self._task_key(guild.id, channel.id)
        t = self._tasks.get(key)
        if t and not t.done():
            t.cancel()
        self._tasks[key] = asyncio.create_task(self._game_loop(guild.id, channel.id))

    # -------------------- game loop --------------------

    async def _game_loop(self, guild_id: int, channel_id: int):
        await asyncio.sleep(0.5)

        guild = self.bot.get_guild(guild_id)
        if guild is None:
            return
        channel = guild.get_channel(channel_id)
        if not isinstance(channel, discord.TextChannel):
            return

        while True:
            game = await self._get_game(guild, channel_id)
            if not game or game.get("phase") != "running":
                return

            alive = [uid for uid in game["players"] if int(game["lives"].get(str(uid), 0)) > 0]
            if len(alive) <= 1:
                if alive:
                    winner_id = alive[0]
                    await channel.send(embed=self._announce_embed(
                        "🏆 Winner!",
                        f"<@{winner_id}> is the last one standing. The dictionary salutes.",
                        discord.Color.green(),
                    ))
                    winner_member = guild.get_member(winner_id)
                    if winner_member:
                        await self.config.member(winner_member).wins.set((await self.config.member(winner_member).wins()) + 1)

                await self._set_game(guild, channel_id, None)
                return

            idx = int(game.get("current_index", 0))
            players = game["players"]
            if idx >= len(players):
                idx = 0

            start_idx = idx
            while int(game["lives"].get(str(players[idx]), 0)) <= 0:
                idx = (idx + 1) % len(players)
                if idx == start_idx:
                    break

            player_id = players[idx]
            game["current_index"] = (idx + 1) % len(players)

            last_word = game.get("last_word", "") or ""
            rule = self._pick_rule(last_word if last_word else None)
            game["turn_rule"] = rule
            await self._set_game(guild, channel_id, game)

            await channel.send(
                content=f"<@{player_id}> you’re up!",
                allowed_mentions=discord.AllowedMentions(users=True),
            )

            ok_word = await self._run_turn(guild, channel, game, player_id, rule)

            game = await self._get_game(guild, channel_id)
            if not game or game.get("phase") != "running":
                return

            if ok_word:
                game["last_word"] = ok_word
                await self._set_game(guild, channel_id, game)
            else:
                lives = max(0, int(game["lives"].get(str(player_id), 0)) - 1)
                game["lives"][str(player_id)] = lives
                await self._set_game(guild, channel_id, game)

                if lives <= 0:
                    await channel.send(embed=self._announce_embed(
                        "💀 Eliminated",
                        f"<@{player_id}> ran out of lives and is out.",
                        discord.Color.red(),
                    ))

    async def _run_turn(
        self,
        guild: discord.Guild,
        channel: discord.TextChannel,
        game: Dict[str, Any],
        player_id: int,
        rule: Dict[str, Any],
    ) -> Optional[str]:
        last_word = game.get("last_word", "") or ""
        feedback = ""

        turn_msg = await channel.send(embed=self._turn_embed(game, player_id, rule, 10, last_word, feedback))
        game["turn_message_id"] = turn_msg.id
        await self._set_game(guild, channel.id, game)

        for sec_left in range(10, 0, -1):
            game_now = await self._get_game(guild, channel.id)
            if not game_now or game_now.get("phase") != "running":
                return None

            await self._safe_edit(
                turn_msg,
                embed=self._turn_embed(game_now, player_id, rule, sec_left, last_word, feedback),
            )

            try:
                msg = await self.bot.wait_for(
                    "message",
                    timeout=1.0,
                    check=lambda m: (
                        m.guild
                        and m.guild.id == guild.id
                        and m.channel.id == channel.id
                        and m.author.id == player_id
                    ),
                )
            except asyncio.TimeoutError:
                continue

            attempt = msg.content.strip()
            err = self._basic_validate(attempt)
            if err:
                feedback = f"❌ `{attempt[:50]}` — {err}"
                continue

            word = self._normalize(attempt)

            if not self._is_real_word(word):
                feedback = f"❌ `{word}` — not a recognized English word."
                continue

            if not self._check_rule(rule, word):
                rd = self._rule_display(rule)
                feedback = f"❌ `{word}` — fails rule: {rd.title}."
                continue

            feedback = f"✅ `{word}` accepted!"
            await self._safe_edit(
                turn_msg,
                embed=self._turn_embed(game_now, player_id, rule, 0, last_word, feedback),
            )
            await channel.send(embed=self._announce_embed(
                "✅ Accepted",
                f"<@{player_id}> played **{word.upper()}**.",
                discord.Color.green(),
            ))
            return word

        await channel.send(embed=self._announce_embed(
            "⏰ Time!",
            f"<@{player_id}> didn’t land a valid word in time and loses a life.",
            discord.Color.orange(),
        ))
        return None

    async def _end_game(self, guild: discord.Guild, channel: discord.TextChannel, reason: str):
        key = self._task_key(guild.id, channel.id)
        t = self._tasks.pop(key, None)
        if t:
            t.cancel()
        await self._set_game(guild, channel.id, None)
        await channel.send(embed=self._announce_embed("🧯 ChainReaction Ended", reason, discord.Color.dark_gray()))

    # -------------------- commands --------------------

    @commands.hybrid_group(name="chain", aliases=["chainreaction"])
    @commands.guild_only()
    async def chain(self, ctx: commands.Context):
        """ChainReaction commands."""
        if ctx.invoked_subcommand is None:
            await ctx.send_help()

    @chain.command(name="start")
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def chain_start(self, ctx: commands.Context):
        """Create a lobby with a Join button; auto-starts in 60 seconds (min 2 players)."""
        assert isinstance(ctx.channel, discord.TextChannel)
        guild = ctx.guild
        channel = ctx.channel

        existing = await self._get_game(guild, channel.id)
        if existing:
            await ctx.send(embed=self._announce_embed(
                "Already running",
                "There’s already a ChainReaction lobby/game in this channel. Use `[p]chain stop` first.",
                discord.Color.red(),
            ))
            return

        game: Dict[str, Any] = {
            "phase": "lobby",
            "host_id": ctx.author.id,
            "players": [],
            "lives": {},  # user_id(str) -> lives int
            "current_index": 0,
            "last_word": "",
            "turn_rule": None,
            "lobby_message_id": None,
            "turn_message_id": None,
            "lobby_seconds_left": 60,
        }

        view = LobbyView(self, guild.id, channel.id)
        lobby_msg = await channel.send(embed=self._lobby_embed(channel, game), view=view)
        game["lobby_message_id"] = lobby_msg.id
        await self._set_game(guild, channel.id, game)

        # start the 60s countdown task
        key = self._task_key(guild.id, channel.id)
        t = self._tasks.get(key)
        if t and not t.done():
            t.cancel()
        self._tasks[key] = asyncio.create_task(self._run_lobby_countdown(guild.id, channel.id))

    @chain.command(name="stop")
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def chain_stop(self, ctx: commands.Context):
        """Stop the lobby/game in this channel."""
        assert isinstance(ctx.channel, discord.TextChannel)
        guild = ctx.guild
        channel = ctx.channel

        game = await self._get_game(guild, channel.id)
        if not game:
            await ctx.send(embed=self._announce_embed("Nothing running", "No ChainReaction lobby/game here.", discord.Color.blurple()))
            return

        await self._end_game(guild, channel, reason="Stopped by an admin.")

    @chain.command(name="status")
    @commands.guild_only()
    async def chain_status(self, ctx: commands.Context):
        """Show status for this channel."""
        assert isinstance(ctx.channel, discord.TextChannel)
        guild = ctx.guild
        channel = ctx.channel

        game = await self._get_game(guild, channel.id)
        if not game:
            await ctx.send(embed=self._announce_embed("No game", "No ChainReaction running in this channel.", discord.Color.blurple()))
            return

        players = game.get("players", [])
        alive = [uid for uid in players if int(game["lives"].get(str(uid), 0)) > 0]
        phase = game.get("phase", "unknown")
        last_word = game.get("last_word", "") or "none"

        e = discord.Embed(title="📊 ChainReaction Status", color=discord.Color.blurple())
        e.add_field(name="Phase", value=phase, inline=True)
        e.add_field(name="Players joined", value=str(len(players)), inline=True)
        e.add_field(name="Alive", value=str(len(alive)), inline=True)
        if phase == "lobby":
            e.add_field(name="Lobby time left", value=f"{int(game.get('lobby_seconds_left', 0))}s", inline=False)
        e.add_field(name="Last accepted word", value=last_word.upper(), inline=False)
        await ctx.send(embed=e)