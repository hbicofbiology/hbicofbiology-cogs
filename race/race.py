# Swamp Race Cog for Red-DiscordBot V3
# Inspired by Redjumpman's original Race cog (Jumper-Plugins)
# Recreated from scratch with swamp creature theming

import asyncio
import random
from typing import Literal, Optional

import discord
from redbot.core import bank, commands, Config
from redbot.core.errors import BalanceTooHigh
from redbot.core.utils import AsyncIter
from redbot.core.utils.chat_formatting import humanize_number

from .creatures import Creature, pick_creatures, pick_start_gif, pick_finish_gif

__version__ = "1.0.0"
__author__ = "Bbygrl (inspired by Redjumpman)"

TRACK_LENGTH = 60  # characters wide
FINISH_LINE = TRACK_LENGTH


class Race(commands.Cog):
    """Race swamp creatures against your friends!

    Start a race, let players join, then watch your creatures
    sprint through the muck to the finish line.
    Inspired by Redjumpman's original Race cog.
    """

    __version__ = __version__
    __author__ = __author__

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=5074395042, force_registration=True)

        guild_defaults = {
            "wait": 60,
            "prize": 100,
            "pooling": False,
            "payout_min": 0,
            "bet_multiplier": 2,
            "bet_min": 10,
            "bet_max": 50,
            "bet_allowed": True,
            "games_played": 0,
        }
        member_defaults = {
            "wins": {"1": 0, "2": 0, "3": 0},
            "losses": 0,
        }

        self.config.register_guild(**guild_defaults)
        self.config.register_member(**member_defaults)

        # Per-guild runtime state (not persisted)
        self._active: dict[int, bool] = {}         # race lobby open?
        self._started: dict[int, bool] = {}         # race in progress?
        self._players: dict[int, list] = {}         # guild_id -> [discord.Member, ...]
        self._bets: dict[int, dict] = {}            # guild_id -> {bettor_id: {target_id: amount}}

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _is_active(self, guild_id: int) -> bool:
        return self._active.get(guild_id, False)

    def _is_started(self, guild_id: int) -> bool:
        return self._started.get(guild_id, False)

    def _teardown(self, guild_id: int):
        self._active[guild_id] = False
        self._started[guild_id] = False
        self._players.pop(guild_id, None)
        self._bets.pop(guild_id, None)

    @staticmethod
    def _draw_lane(creature: Creature, label: str, track_width: int, finished: bool) -> str:
        """Draw one lane: the creature icon slides across a fixed-width track.

        Looks like:
            BogLurker   |·····🐊··················| 🏁
            MireStalker |·············🐸··········| 🏁
            FenPhantom  |··················👻·····| 🏁 ✔
        """
        pos = min(creature.current, FINISH_LINE)
        scaled = int((pos / FINISH_LINE) * track_width)
        scaled = min(scaled, track_width)

        # Build the lane: dots before icon, icon, dots after
        before = "·" * scaled
        after = "·" * (track_width - scaled)
        icon = creature.icon
        done_mark = " ✔" if finished else ""

        # Pad the label to keep lanes aligned
        padded = label[:12].ljust(12)
        return f"`{padded}` |{before}{icon}{after}|🏁{done_mark}"

    # ------------------------------------------------------------------
    # Race engine
    # ------------------------------------------------------------------

    async def _run_race(self, ctx, players: list, creatures: list[Creature]):
        """Simulate the race, editing a message each tick. Returns ordered finishers."""

        # Map player -> creature
        assignments = list(zip(players, creatures))
        # Track width in characters (wider = more visual movement)
        # Keep it narrow enough to fit on mobile (~22 chars)
        track_width = 22

        finishers = []  # [(player, creature), ...]
        finished_set = set()  # player ids that crossed the line

        def build_board():
            lines = []
            for player, creature in assignments:
                done = player.id in finished_set
                label = player.display_name
                lines.append(self._draw_lane(creature, label, track_width, done))
            return "\n".join(lines)

        e = discord.Embed(
            title="🏁 Swamp Race — They're Off!",
            description=build_board(),
            colour=discord.Colour.dark_green(),
        )
        e.set_thumbnail(url=pick_start_gif())
        msg = await ctx.send(embed=e)

        while len(finishers) < len(assignments):
            await asyncio.sleep(1.5)

            for player, creature in assignments:
                if creature.current < FINISH_LINE:
                    creature.advance()
                    if creature.current >= FINISH_LINE and player.id not in finished_set:
                        finishers.append((player, creature))
                        finished_set.add(player.id)

            e.description = build_board()
            if finishers:
                status = " | ".join(
                    f"{'🥇🥈🥉'[i] if i < 3 else '🏅'} {p.display_name}"
                    for i, (p, _) in enumerate(finishers)
                )
                e.set_footer(text=f"Finished: {status}")

            try:
                await msg.edit(embed=e)
            except discord.HTTPException:
                pass

        return finishers

    # ------------------------------------------------------------------
    # Payout logic
    # ------------------------------------------------------------------

    async def _do_payouts(self, ctx, finishers, settings):
        """Handle prize and bet payouts. Returns a list of payout strings."""
        guild = ctx.guild
        currency = await bank.get_currency_name(guild)
        prize = settings["prize"]
        pooling = settings["pooling"]
        payout_min = settings["payout_min"]
        bet_mult = settings["bet_multiplier"]

        human_count = sum(1 for p, _ in finishers if not p.bot)
        # Exclude the race starter from the count for payout_min
        meets_min = (human_count - 1) >= payout_min

        payout_lines = []

        if prize > 0 and meets_min:
            first = finishers[0][0]
            if pooling and len(finishers) >= 4:
                prizes = {
                    0: int(prize * 0.60),
                    1: int(prize * 0.30),
                    2: int(prize * 0.10),
                }
                for place, amount in prizes.items():
                    if place < len(finishers):
                        player = finishers[place][0]
                        if not player.bot:
                            try:
                                await bank.deposit_credits(player, amount)
                            except BalanceTooHigh:
                                pass
                            medal = ["🥇", "🥈", "🥉"][place]
                            payout_lines.append(f"{medal} {player.display_name} won **{humanize_number(amount)}** {currency}")
            else:
                if not first.bot:
                    try:
                        await bank.deposit_credits(first, prize)
                    except BalanceTooHigh:
                        pass
                    payout_lines.append(f"🥇 {first.display_name} won **{humanize_number(prize)}** {currency}")

        # Bet payouts
        guild_bets = self._bets.get(guild.id, {})
        winner_ids = [finishers[0][0].id] if finishers else []
        for bettor_id, bet_info in guild_bets.items():
            for target_id, amount in bet_info.items():
                if target_id in winner_ids:
                    winnings = int(amount * bet_mult)
                    bettor = guild.get_member(bettor_id)
                    if bettor:
                        try:
                            await bank.deposit_credits(bettor, winnings)
                        except BalanceTooHigh:
                            pass
                        payout_lines.append(f"💰 {bettor.display_name} won **{humanize_number(winnings)}** {currency} from their bet!")

        return payout_lines

    # ------------------------------------------------------------------
    # Stats
    # ------------------------------------------------------------------

    async def _update_stats(self, ctx, finishers):
        players_in_race = [p for p, _ in finishers]
        for i, (player, _) in enumerate(finishers):
            if player.bot:
                continue
            if i < 3:
                current = await self.config.member(player).wins.get_raw(str(i + 1))
                await self.config.member(player).wins.set_raw(str(i + 1), value=current + 1)
            else:
                current = await self.config.member(player).losses()
                await self.config.member(player).losses.set(current + 1)

        # Everyone who didn't finish top 3 gets a loss
        for player, _ in finishers[3:]:
            if not player.bot:
                current = await self.config.member(player).losses()
                await self.config.member(player).losses.set(current + 1)

    # ==================================================================
    #  COMMANDS
    # ==================================================================

    @commands.group()
    @commands.guild_only()
    async def race(self, ctx):
        """Swamp creature race commands."""
        pass

    @race.command()
    async def start(self, ctx):
        """Start a new swamp race!

        Other players can join with `[p]race enter` during the waiting period.
        If nobody else joins, you'll race against a bot creature.
        """
        gid = ctx.guild.id
        if self._is_active(gid):
            return await ctx.send(f"A race is already in progress! Type `{ctx.prefix}race enter` to join!")

        self._active[gid] = True
        self._started[gid] = False
        self._players[gid] = [ctx.author]
        self._bets[gid] = {}

        wait = await self.config.guild(ctx.guild).wait()

        # Increment games played
        current = await self.config.guild(ctx.guild).games_played()
        await self.config.guild(ctx.guild).games_played.set(current + 1)

        e = discord.Embed(
            title="🐊 A Swamp Race Has Begun!",
            description=(
                f"The creatures are stirring in the muck...\n\n"
                f"Type `{ctx.prefix}race enter` to join!\n"
                f"The race begins in **{wait} seconds**.\n\n"
                f"**{ctx.author.display_name}** has entered the race!"
            ),
            colour=discord.Colour.dark_green(),
        )
        e.set_image(url=pick_start_gif())
        e.set_footer(text=f"Betting allowed: use {ctx.prefix}race bet <amount> <player>")
        await ctx.send(embed=e)

        await asyncio.sleep(wait)

        if not self._is_active(gid):
            return  # Race was cleared during wait

        self._started[gid] = True
        players = self._players.get(gid, [ctx.author])

        # If only one human, add a bot racer
        if len(players) < 2:
            bot_member = ctx.guild.me
            players.append(bot_member)

        # Assign creatures
        creatures = pick_creatures(len(players))

        # Announce assignments
        assignment_lines = []
        for player, creature in zip(players, creatures):
            assignment_lines.append(f"{creature.icon} **{creature.name}** — {player.display_name}")

        assign_e = discord.Embed(
            title="🏁 Creatures Assigned!",
            description="\n".join(assignment_lines),
            colour=discord.Colour.dark_green(),
        )
        assign_e.set_footer(text="The race is about to begin...")
        await ctx.send(embed=assign_e)
        await asyncio.sleep(3)

        # Run the race
        finishers = await self._run_race(ctx, players, creatures)

        # Stats
        await self._update_stats(ctx, finishers)

        # Payouts
        settings = await self.config.guild(ctx.guild).all()
        payout_lines = await self._do_payouts(ctx, finishers, settings)

        # Results embed
        results = []
        medals = ["🥇", "🥈", "🥉"]
        for i, (player, creature) in enumerate(finishers):
            medal = medals[i] if i < 3 else f"**{i+1}.**"
            results.append(f"{medal} {creature.icon} **{creature.name}** — {player.display_name}")

        result_e = discord.Embed(
            title="🐊 Swamp Race Results!",
            description="\n".join(results),
            colour=discord.Colour.gold(),
        )
        if payout_lines:
            result_e.add_field(name="💰 Payouts", value="\n".join(payout_lines), inline=False)
        result_e.set_image(url=pick_finish_gif())
        result_e.set_footer(text=f"Race #{current + 1} | {len(players)} racers")

        mentions = " ".join(
            p.mention for p, _ in finishers[:3] if not p.bot
        )
        await ctx.send(content=mentions or None, embed=result_e)

        # Teardown
        self._teardown(gid)

    @race.command()
    async def enter(self, ctx):
        """Join an active race lobby."""
        gid = ctx.guild.id
        if self._is_started(gid):
            return await ctx.send("The race already started! Wait for the next one.")
        if not self._is_active(gid):
            return await ctx.send(f"No race is open. Start one with `{ctx.prefix}race start`.")
        if ctx.author in self._players.get(gid, []):
            return await ctx.send("You've already entered!")
        if len(self._players.get(gid, [])) >= 14:
            return await ctx.send("The swamp is full! (Max 14 racers)")

        self._players[gid].append(ctx.author)
        count = len(self._players[gid])
        await ctx.send(f"🐊 **{ctx.author.display_name}** splashes into the race! ({count} racers)")

    @race.command()
    async def bet(self, ctx, amount: int, user: discord.Member):
        """Bet on a player to win the race.

        Example: `[p]race bet 50 @player`
        """
        gid = ctx.guild.id
        if not self._is_active(gid):
            return await ctx.send("There's no active race to bet on.")
        if self._is_started(gid):
            return await ctx.send("Too late — the race already started!")

        settings = await self.config.guild(ctx.guild).all()
        if not settings["bet_allowed"]:
            return await ctx.send("Betting is disabled for races on this server.")

        if amount < settings["bet_min"]:
            return await ctx.send(f"Minimum bet is **{humanize_number(settings['bet_min'])}**.")
        if amount > settings["bet_max"]:
            return await ctx.send(f"Maximum bet is **{humanize_number(settings['bet_max'])}**.")

        if user not in self._players.get(gid, []):
            return await ctx.send("That person isn't in the race!")
        if ctx.author.id in self._bets.get(gid, {}):
            return await ctx.send("You've already placed a bet for this race.")
        if not await bank.can_spend(ctx.author, amount):
            return await ctx.send("You don't have enough credits for that bet.")

        await bank.withdraw_credits(ctx.author, amount)
        self._bets.setdefault(gid, {})[ctx.author.id] = {user.id: amount}
        currency = await bank.get_currency_name(ctx.guild)
        await ctx.send(f"💰 **{ctx.author.display_name}** bet **{humanize_number(amount)}** {currency} on **{user.display_name}**!")

    @race.command()
    async def stats(self, ctx, user: Optional[discord.Member] = None):
        """Show race stats for yourself or another user."""
        user = user or ctx.author
        data = await self.config.member(user).all()
        total_wins = sum(data["wins"].values())
        total_games = total_wins + data["losses"]
        server_total = await self.config.guild(ctx.guild).games_played()

        try:
            pct = round((total_games / server_total) * 100, 1)
        except ZeroDivisionError:
            pct = 0

        e = discord.Embed(
            title=f"🐊 Race Stats — {user.display_name}",
            colour=discord.Colour.dark_green(),
        )
        e.add_field(
            name="Placements",
            value=(
                f"🥇 1st: **{data['wins']['1']}**\n"
                f"🥈 2nd: **{data['wins']['2']}**\n"
                f"🥉 3rd: **{data['wins']['3']}**"
            ),
            inline=True,
        )
        e.add_field(name="Losses", value=f"**{data['losses']}**", inline=True)
        e.set_footer(text=f"Participated in {total_games} of {server_total} server races ({pct}%)")
        await ctx.send(embed=e)

    @race.command(hidden=True)
    @commands.admin_or_permissions(administrator=True)
    async def clear(self, ctx):
        """Force-clear a stuck race (debug only)."""
        self._teardown(ctx.guild.id)
        await ctx.send("Race state cleared.")

    @race.command()
    async def version(self, ctx):
        """Show the race cog version."""
        await ctx.send(f"Swamp Race v{__version__} by {__author__}")

    # ==================================================================
    #  SETTINGS
    # ==================================================================

    @commands.group()
    @commands.guild_only()
    @commands.admin_or_permissions(administrator=True)
    async def setrace(self, ctx):
        """Configure race settings."""
        pass

    @setrace.command()
    async def wait(self, ctx, seconds: int):
        """Set the lobby wait time before a race starts (in seconds)."""
        if seconds < 10:
            return await ctx.send("Wait time must be at least 10 seconds.")
        await self.config.guild(ctx.guild).wait.set(seconds)
        await ctx.send(f"Race wait time set to **{seconds}** seconds.")

    @setrace.command()
    async def prize(self, ctx, amount: int):
        """Set the prize for winning a race.

        Set to 0 to disable prizes.
        With pooling on, prizes split 60/30/10 for 1st/2nd/3rd.
        """
        if amount < 0:
            return await ctx.send("Prize can't be negative.")
        await self.config.guild(ctx.guild).prize.set(amount)
        currency = await bank.get_currency_name(ctx.guild)
        if amount == 0:
            await ctx.send("Race prizes disabled.")
        else:
            await ctx.send(f"Race prize set to **{humanize_number(amount)}** {currency}.")

    @setrace.command(name="togglepool")
    async def toggle_pool(self, ctx):
        """Toggle prize pooling (60/30/10 split for top 3)."""
        current = await self.config.guild(ctx.guild).pooling()
        await self.config.guild(ctx.guild).pooling.set(not current)
        state = "ON" if not current else "OFF"
        await ctx.send(f"Prize pooling is now **{state}**.")

    @setrace.command(name="payoutmin")
    async def payout_min(self, ctx, players: int):
        """Set minimum human players (besides starter) required for payouts.

        Set to 0 to always pay out.
        """
        if players < 0:
            return await ctx.send("Must be 0 or higher.")
        await self.config.guild(ctx.guild).payout_min.set(players)
        if players == 0:
            await ctx.send("Races will always pay out.")
        else:
            await ctx.send(f"Races require **{players}** extra human player(s) for payouts.")

    @setrace.group(name="bet")
    async def _set_bet(self, ctx):
        """Betting settings."""
        pass

    @_set_bet.command(name="toggle")
    async def bet_toggle(self, ctx):
        """Enable or disable betting."""
        current = await self.config.guild(ctx.guild).bet_allowed()
        await self.config.guild(ctx.guild).bet_allowed.set(not current)
        await ctx.send(f"Betting is now **{'OFF' if current else 'ON'}**.")

    @_set_bet.command(name="min")
    async def bet_min(self, ctx, amount: int):
        """Set the minimum bet amount."""
        if amount < 0:
            return await ctx.send("Must be 0 or higher.")
        await self.config.guild(ctx.guild).bet_min.set(amount)
        await ctx.send(f"Minimum bet set to **{humanize_number(amount)}**.")

    @_set_bet.command(name="max")
    async def bet_max(self, ctx, amount: int):
        """Set the maximum bet amount."""
        if amount < 1:
            return await ctx.send("Must be at least 1.")
        await self.config.guild(ctx.guild).bet_max.set(amount)
        await ctx.send(f"Maximum bet set to **{humanize_number(amount)}**.")

    @_set_bet.command(name="multiplier")
    async def bet_multiplier(self, ctx, mult: float):
        """Set the bet payout multiplier."""
        if mult <= 0:
            return await ctx.send("Multiplier must be positive.")
        await self.config.guild(ctx.guild).bet_multiplier.set(mult)
        await ctx.send(f"Bet multiplier set to **{mult}x**.")

    @setrace.command()
    async def wipe(self, ctx):
        """⚠️ Wipe ALL race data (settings + stats) for this server."""
        await ctx.send(f"⚠️ This will delete all race data. Type `yes` to confirm.")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            resp = await self.bot.wait_for("message", timeout=15.0, check=check)
        except asyncio.TimeoutError:
            return await ctx.send("Cancelled.")
        if resp.content.lower() != "yes":
            return await ctx.send("Cancelled.")

        await self.config.guild(ctx.guild).clear()
        await self.config.clear_all_members(ctx.guild)
        self._teardown(ctx.guild.id)
        await ctx.send("All race data wiped.")

    # ------------------------------------------------------------------
    # Data deletion support
    # ------------------------------------------------------------------

    async def red_delete_data_for_user(
        self, *, requester: Literal["discord_deleted_user", "owner", "user", "user_strict"], user_id: int
    ):
        all_members = await self.config.all_members()
        async for guild_id, guild_data in AsyncIter(all_members.items(), steps=100):
            if user_id in guild_data:
                await self.config.member_from_ids(guild_id, user_id).clear()
