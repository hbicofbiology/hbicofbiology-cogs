from __future__ import annotations

import asyncio
import random
import time
from typing import Dict, Optional

import discord
from redbot.core import Config, bank, commands
from redbot.core.bot import Red


class SwampHunt(commands.Cog):
    """Passive swamp creature encounters."""

    CREATURES = {
        "frog": {
            "name": "Frog",
            "default_emoji": "🐸",
            "weight": 30,
            "reward_min": 25,
            "reward_max": 70,
            "bad": False,
            "spawn_text": "A {emoji} **Frog** splashes out of the reeds! Type `snag` to grab it!",
            "win_text": "{user} snagged the {emoji} **Frog** and earned **{amount} {currency}**!",
        },
        "mudskipper": {
            "name": "Mudskipper",
            "default_emoji": "🐟",
            "weight": 24,
            "reward_min": 35,
            "reward_max": 90,
            "bad": False,
            "spawn_text": "A slippery {emoji} **Mudskipper** flops through the muck! Type `snag`!",
            "win_text": "{user} yoinked the {emoji} **Mudskipper** and got **{amount} {currency}**!",
        },
        "alligator": {
            "name": "Alligator",
            "default_emoji": "🐊",
            "weight": 10,
            "reward_min": 90,
            "reward_max": 180,
            "bad": False,
            "spawn_text": "A lurking {emoji} **Alligator** rises from the swamp... type `snag` if you're brave.",
            "win_text": "{user} wrestled the {emoji} **Alligator** and earned **{amount} {currency}**!",
        },
        "snapping_turtle": {
            "name": "Snapping Turtle",
            "default_emoji": "🐢",
            "weight": 14,
            "reward_min": 65,
            "reward_max": 130,
            "bad": False,
            "spawn_text": "A grumpy {emoji} **Snapping Turtle** surfaces in the sludge! Type `snag`!",
            "win_text": "{user} carefully snagged the {emoji} **Snapping Turtle** and got **{amount} {currency}**!",
        },
        "snake": {
            "name": "Snake",
            "default_emoji": "🐍",
            "weight": 18,
            "reward_min": 45,
            "reward_max": 110,
            "bad": False,
            "spawn_text": "A slithering {emoji} **Snake** coils near the waterline... type `snag`!",
            "win_text": "{user} grabbed the {emoji} **Snake** and earned **{amount} {currency}**!",
        },
        "willowisp": {
            "name": "Will-o'-Wisp",
            "default_emoji": "✨",
            "weight": 4,
            "reward_min": 60,
            "reward_max": 140,
            "bad": True,
            "spawn_text": "A glowing {emoji} **Will-o'-Wisp** flickers over the bog. Type `snag`... this seems bad.",
            "win_text": "{user} reached for the {emoji} **Will-o'-Wisp** and lost **{amount} {currency}**...",
        },
    }

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=540271980221, force_registration=True)

        default_guild = {
            "enabled": True,
            "channels": [],  # if empty, all channels are valid
            "spawn_chance": 0.06,  # 6% chance per normal message
            "spawn_cooldown": 45,  # seconds between spawns per guild
            "encounter_timeout": 12,  # seconds to type snag
            "emojis": {
                "frog": "🐸",
                "mudskipper": "🐟",
                "alligator": "🐊",
                "snapping_turtle": "🐢",
                "snake": "🐍",
                "willowisp": "✨",
            },
        }
        self.config.register_guild(**default_guild)

        self._active_encounters: Dict[int, bool] = {}
        self._last_spawn: Dict[int, float] = {}
        self._guild_locks: Dict[int, asyncio.Lock] = {}

    def _get_lock(self, guild_id: int) -> asyncio.Lock:
        lock = self._guild_locks.get(guild_id)
        if lock is None:
            lock = asyncio.Lock()
            self._guild_locks[guild_id] = lock
        return lock

    async def _message_is_command(self, message: discord.Message) -> bool:
        prefixes = await self.bot.get_valid_prefixes(message.guild)
        return any(message.content.startswith(prefix) for prefix in prefixes)

    async def _pick_creature(self) -> str:
        keys = list(self.CREATURES.keys())
        weights = [self.CREATURES[k]["weight"] for k in keys]
        return random.choices(keys, weights=weights, k=1)[0]

    async def _resolve_emoji(self, guild: discord.Guild, creature_key: str) -> str:
        emojis = await self.config.guild(guild).emojis()
        return emojis.get(creature_key, self.CREATURES[creature_key]["default_emoji"])

    async def _can_spawn_here(self, channel: discord.TextChannel) -> bool:
        allowed_channels = await self.config.guild(channel.guild).channels()
        if not allowed_channels:
            return True
        return channel.id in allowed_channels

    async def _handle_encounter(self, channel: discord.TextChannel) -> None:
        guild = channel.guild
        guild_id = guild.id
        creature_key = await self._pick_creature()
        creature = self.CREATURES[creature_key]
        emoji = await self._resolve_emoji(guild, creature_key)
        currency = await bank.get_currency_name(guild)

        self._active_encounters[guild_id] = True
        self._last_spawn[guild_id] = time.monotonic()

        spawn_text = creature["spawn_text"].format(emoji=emoji)
        await channel.send(spawn_text)

        def check(m: discord.Message) -> bool:
            return (
                m.guild is not None
                and m.guild.id == guild_id
                and m.channel.id == channel.id
                and not m.author.bot
                and m.content.lower().strip() == "snag"
            )

        timeout = await self.config.guild(guild).encounter_timeout()

        try:
            snag_msg = await self.bot.wait_for("message", timeout=timeout, check=check)
        except asyncio.TimeoutError:
            self._active_encounters[guild_id] = False
            await channel.send("The swamp goes still. Whatever it was, it vanished back into the muck.")
            return

        amount = random.randint(creature["reward_min"], creature["reward_max"])

        if creature["bad"]:
            balance = await bank.get_balance(snag_msg.author)
            stolen = min(balance, amount)
            if stolen > 0:
                await bank.withdraw_credits(snag_msg.author, stolen)
            amount = stolen
        else:
            await bank.deposit_credits(snag_msg.author, amount)

        result = creature["win_text"].format(
            user=snag_msg.author.mention,
            emoji=emoji,
            amount=amount,
            currency=currency,
        )
        await channel.send(result)
        self._active_encounters[guild_id] = False

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if message.guild is None:
            return
        if message.author.bot:
            return
        if not isinstance(message.channel, discord.TextChannel):
            return

        guild = message.guild
        guild_id = guild.id

        if not await self.config.guild(guild).enabled():
            return

        if not await self._can_spawn_here(message.channel):
            return

        if await self._message_is_command(message):
            return

        lock = self._get_lock(guild_id)
        async with lock:
            if self._active_encounters.get(guild_id, False):
                return

            cooldown = await self.config.guild(guild).spawn_cooldown()
            last_spawn = self._last_spawn.get(guild_id, 0.0)
            if time.monotonic() - last_spawn < cooldown:
                return

            chance = await self.config.guild(guild).spawn_chance()
            if random.random() > chance:
                return

            self.bot.loop.create_task(self._handle_encounter(message.channel))

    @commands.group()
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def swamphuntset(self, ctx: commands.Context) -> None:
        """Configure passive swamp encounters."""
        if ctx.invoked_subcommand is None:
            channels = await self.config.guild(ctx.guild).channels()
            chance = await self.config.guild(ctx.guild).spawn_chance()
            cooldown = await self.config.guild(ctx.guild).spawn_cooldown()
            timeout = await self.config.guild(ctx.guild).encounter_timeout()
            enabled = await self.config.guild(ctx.guild).enabled()

            channel_mentions = ", ".join(f"<#{cid}>" for cid in channels) if channels else "All channels"
            await ctx.send(
                f"**SwampHunt settings**\n"
                f"Enabled: `{enabled}`\n"
                f"Spawn chance: `{chance:.2%}` per normal message\n"
                f"Spawn cooldown: `{cooldown}` seconds\n"
                f"Encounter timeout: `{timeout}` seconds\n"
                f"Allowed channels: {channel_mentions}"
            )

    @swamphuntset.command(name="toggle")
    async def swamphuntset_toggle(self, ctx: commands.Context, value: bool) -> None:
        """Enable or disable passive encounters."""
        await self.config.guild(ctx.guild).enabled.set(value)
        await ctx.send(f"SwampHunt enabled set to `{value}`.")

    @swamphuntset.group(name="channel")
    async def swamphuntset_channel(self, ctx: commands.Context) -> None:
        """Manage allowed channels."""
        if ctx.invoked_subcommand is None:
            channels = await self.config.guild(ctx.guild).channels()
            if not channels:
                await ctx.send("No channel restriction is set. Encounters can spawn in all text channels.")
                return
            mentions = ", ".join(f"<#{cid}>" for cid in channels)
            await ctx.send(f"Allowed channels: {mentions}")

    @swamphuntset_channel.command(name="add")
    async def swamphuntset_channel_add(
        self, ctx: commands.Context, channel: discord.TextChannel
    ) -> None:
        """Allow encounters in a channel."""
        async with self.config.guild(ctx.guild).channels() as channels:
            if channel.id not in channels:
                channels.append(channel.id)
        await ctx.send(f"Added {channel.mention} to allowed SwampHunt channels.")

    @swamphuntset_channel.command(name="remove")
    async def swamphuntset_channel_remove(
        self, ctx: commands.Context, channel: discord.TextChannel
    ) -> None:
        """Remove a channel from the allow-list."""
        async with self.config.guild(ctx.guild).channels() as channels:
            if channel.id in channels:
                channels.remove(channel.id)
        await ctx.send(f"Removed {channel.mention} from allowed SwampHunt channels.")

    @swamphuntset_channel.command(name="clear")
    async def swamphuntset_channel_clear(self, ctx: commands.Context) -> None:
        """Clear channel restrictions."""
        await self.config.guild(ctx.guild).channels.set([])
        await ctx.send("Channel restriction cleared. Encounters can now spawn in all text channels.")

    @swamphuntset.command(name="chance")
    async def swamphuntset_chance(self, ctx: commands.Context, percent: float) -> None:
        """
        Set spawn chance per message.

        Example: `[p]swamphuntset chance 6`
        """
        if percent <= 0 or percent > 100:
            await ctx.send("Give me a number greater than 0 and at most 100.")
            return
        chance = percent / 100.0
        await self.config.guild(ctx.guild).spawn_chance.set(chance)
        await ctx.send(f"Spawn chance set to `{percent:.2f}%` per normal message.")

    @swamphuntset.command(name="cooldown")
    async def swamphuntset_cooldown(self, ctx: commands.Context, seconds: int) -> None:
        """Set the guild-wide time between spawns."""
        if seconds < 0:
            await ctx.send("Cooldown can't be negative.")
            return
        await self.config.guild(ctx.guild).spawn_cooldown.set(seconds)
        await ctx.send(f"Spawn cooldown set to `{seconds}` seconds.")

    @swamphuntset.command(name="timeout")
    async def swamphuntset_timeout(self, ctx: commands.Context, seconds: int) -> None:
        """Set how long users have to type snag."""
        if seconds < 3:
            await ctx.send("That's too short. Use at least 3 seconds.")
            return
        await self.config.guild(ctx.guild).encounter_timeout.set(seconds)
        await ctx.send(f"Encounter timeout set to `{seconds}` seconds.")

    @swamphuntset.command(name="emoji")
    async def swamphuntset_emoji(
        self, ctx: commands.Context, creature: str, *, emoji: str
    ) -> None:
        """
        Set a custom emoji for a creature.

        Valid creature keys:
        frog, mudskipper, alligator, snapping_turtle, snake, willowisp
        """
        creature = creature.lower().strip()
        aliases = {
            "turtle": "snapping_turtle",
            "snappingturtle": "snapping_turtle",
            "snapping_turtle": "snapping_turtle",
            "wisp": "willowisp",
            "willowisp": "willowisp",
            "will-o-wisp": "willowisp",
        }
        creature = aliases.get(creature, creature)

        if creature not in self.CREATURES:
            valid = ", ".join(self.CREATURES.keys())
            await ctx.send(f"Invalid creature. Valid keys: `{valid}`")
            return

        async with self.config.guild(ctx.guild).emojis() as emojis:
            emojis[creature] = emoji

        await ctx.send(f"Emoji for `{creature}` updated to {emoji}")

    @swamphuntset.command(name="emojis")
    async def swamphuntset_emojis(self, ctx: commands.Context) -> None:
        """Show current configured emojis."""
        emojis = await self.config.guild(ctx.guild).emojis()
        lines = []
        for key, data in self.CREATURES.items():
            lines.append(f"`{key}` → {emojis.get(key, data['default_emoji'])}")
        await ctx.send("\n".join(lines))

    @commands.command()
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def swampspawn(self, ctx: commands.Context) -> None:
        """Force a manual encounter for testing."""
        guild_id = ctx.guild.id
        if self._active_encounters.get(guild_id, False):
            await ctx.send("There's already an active encounter.")
            return
        self.bot.loop.create_task(self._handle_encounter(ctx.channel))