"""
Tarot Cog for Red-DiscordBot
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Full 78-card Rider-Waite-Smith deck with:
  • Single draw, 3-card spread, Celtic Cross, and custom named spreads
  • Upright / reversed support
  • Rich hybrid readings (short by default, full on request)
  • User reading history / journal
  • Daily card with per-user cooldown
  • Per-server cooldowns and admin configuration
  • Suit / arcana filtering
  • Atmospheric flavour text and embedded card art
"""

import asyncio
import random
from datetime import datetime, timezone

import discord
from redbot.core import Config, checks, commands
from redbot.core.bot import Red
from redbot.core.utils.menus import DEFAULT_CONTROLS, menu

from .card_data import CARDS, SUIT_MAP
from .spreads import SPREADS, FLAVOUR_INTROS

# ─── Spread definitions ───────────────────────────────────────────────────────

# Map command aliases to the richer spread definitions in spreads.py
BUILT_IN_SPREADS = {
    "ppf": SPREADS["three_card"],
    "celtic": SPREADS["celtic_cross"],
}


def _pos_name(pos) -> str:
    """Extract position name from either a plain string or a dict."""
    if isinstance(pos, dict):
        return pos["name"]
    return pos


def _pos_desc(pos) -> str:
    """Extract position description from a dict, or empty string."""
    if isinstance(pos, dict):
        return pos.get("description", "")
    return ""

# ─── Visual helpers ───────────────────────────────────────────────────────────

SUIT_COLOURS = {
    "wands": 0xE8532A,
    "cups": 0x4A90D9,
    "swords": 0x8E9BAE,
    "pentacles": 0x8B6914,
    None: 0x6B3FA0,
}

SUIT_EMOJI = {
    "wands": "🔥",
    "cups": "🌊",
    "swords": "⚡",
    "pentacles": "🌿",
    None: "☽",
}

ATMOSPHERIC_OPENERS = FLAVOUR_INTROS


# ─── Utility functions ────────────────────────────────────────────────────────

def draw_cards(n: int, pool: list, allow_reversed: bool = True) -> list:
    chosen = random.sample(pool, min(n, len(pool)))
    return [
        {**card, "reversed": allow_reversed and random.random() < 0.33}
        for card in chosen
    ]


def card_colour(card: dict) -> int:
    return SUIT_COLOURS.get(card.get("suit"), 0x6B3FA0)


def card_short_text(card: dict) -> str:
    return card["meaning_reversed_short"] if card.get("reversed") else card["meaning_short"]


def card_full_text(card: dict) -> str:
    return card["meaning_reversed_full"] if card.get("reversed") else card["meaning_full"]


def keywords_str(card: dict) -> str:
    kws = card["keywords_reversed"] if card.get("reversed") else card["keywords_upright"]
    return " · ".join(kws)


def make_single_embed(card: dict, position: str = None, detail: bool = False) -> discord.Embed:
    colour = card_colour(card)
    title = card["name"]
    if card.get("reversed"):
        title += " *(reversed)*"
    if position:
        title = f"{position}: {title}"

    description = (
        f"*{card['flavour']}*\n\n"
        f"*{keywords_str(card)}*\n\n"
        + (card_full_text(card) if detail else card_short_text(card))
    )

    embed = discord.Embed(title=title, description=description, colour=colour)
    if card.get("image_url"):
        embed.set_image(url=card["image_url"])
    embed.set_footer(
        text=f"{card['arcana'].capitalize()} Arcana"
        + (f" · {card['suit'].capitalize()}" if card["suit"] else "")
    )
    return embed


def record_to_history_entry(cards: list, spread_name: str, question: str = None) -> dict:
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "spread": spread_name,
        "question": question,
        "cards": [
            {"id": c["id"], "name": c["name"], "reversed": c.get("reversed", False)}
            for c in cards
        ],
    }


# ─── The Cog ─────────────────────────────────────────────────────────────────

class Tarot(commands.Cog):
    """
    A full-featured Tarot reading cog for Red-DiscordBot.

    Draws from the complete 78-card Rider-Waite-Smith deck with reversals,
    multiple spread types, a reading journal, daily card, and admin controls.
    """

    default_guild = {
        "enabled": True,
        "allow_reversals": True,
        "spread_cooldown": 60,
        "daily_cooldown": 79200,
        "custom_spreads": {},
        "allowed_channels": [],
    }

    default_user = {
        "history": [],
        "last_spread_time": 0.0,
        "last_daily_time": 0.0,
        "history_limit": 50,
    }

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=0x5441524F54, force_registration=True)
        self.config.register_guild(**self.default_guild)
        self.config.register_user(**self.default_user)

    # ── Helpers ───────────────────────────────────────────────────────────────

    async def _check_cooldown(self, ctx, key: str, config_key: str) -> tuple:
        last = getattr(await self.config.user(ctx.author).all(), key, 0)
        last = (await self.config.user(ctx.author).all())[key]
        cd = (await self.config.guild(ctx.guild).all())[config_key]
        elapsed = datetime.now(timezone.utc).timestamp() - last
        if elapsed < cd:
            return False, int(cd - elapsed)
        return True, 0

    async def _set_time(self, ctx, attr: str):
        await getattr(self.config.user(ctx.author), attr).set(
            datetime.now(timezone.utc).timestamp()
        )

    async def _save_reading(self, ctx, cards: list, spread_name: str, question: str = None):
        entry = record_to_history_entry(cards, spread_name, question)
        async with self.config.user(ctx.author).history() as hist:
            limit = await self.config.user(ctx.author).history_limit()
            hist.append(entry)
            if len(hist) > limit:
                del hist[: len(hist) - limit]

    async def _get_pool(self, ctx, filter_arg: str = None) -> list:
        if filter_arg:
            key = filter_arg.lower()
            if key in SUIT_MAP:
                return SUIT_MAP[key]
            await ctx.send(
                f"Unknown filter `{filter_arg}`. Valid: `major`, `minor`, `wands`, `cups`, `swords`, `pentacles`"
            )
            return []
        return CARDS

    async def _gate(self, ctx) -> bool:
        """Return True if we should proceed."""
        if not await self.config.guild(ctx.guild).enabled():
            await ctx.send("Tarot is not enabled on this server.")
            return False
        allowed = await self.config.guild(ctx.guild).allowed_channels()
        if allowed and ctx.channel.id not in allowed:
            await ctx.send("Tarot readings are not allowed in this channel.")
            return False
        return True

    # ── Core draw ─────────────────────────────────────────────────────────────

    async def _do_draw(self, ctx, n_cards: int, spread_name: str, positions: list,
                       question: str = None, filter_arg: str = None, detail: bool = False):
        if not await self._gate(ctx):
            return

        ok, remaining = await self._check_cooldown(ctx, "last_spread_time", "spread_cooldown")
        if not ok:
            m, s = divmod(remaining, 60)
            return await ctx.send(
                f"🌙 The cards need a moment. Try again in "
                f"{'**' + str(m) + 'm ' if m else ''}**{s}s**."
            )

        pool = await self._get_pool(ctx, filter_arg)
        if not pool:
            return

        if len(pool) < n_cards:
            return await ctx.send(
                f"Not enough cards in that pool ({len(pool)}) for a {n_cards}-card spread."
            )

        allow_rev = await self.config.guild(ctx.guild).allow_reversals()
        cards = draw_cards(n_cards, pool, allow_reversed=allow_rev)

        await self._set_time(ctx, "last_spread_time")
        await self._save_reading(ctx, cards, spread_name, question)

        opener = random.choice(ATMOSPHERIC_OPENERS)

        if n_cards == 1:
            embed = make_single_embed(cards[0], detail=detail)
            embed.set_author(name=f"{opener} — {spread_name}")
            if question:
                embed.add_field(name="Your question", value=f"*{question}*", inline=False)
            if not detail:
                embed.set_footer(
                    text=(embed.footer.text or "") + " · Use `!tarot detail` for the full reading."
                )
            return await ctx.send(embed=embed)

        # Multi-card: paginated
        pages = []
        card_lines = "\n".join(
            f"**{_pos_name(pos)}** — {SUIT_EMOJI.get(cards[i].get('suit'), '☽')} **{cards[i]['name']}**"
            + (" *(reversed)*" if cards[i].get("reversed") else "")
            + f"\n> {card_short_text(cards[i])}"
            for i, pos in enumerate(positions)
        )
        overview = discord.Embed(
            title=f"✦ {spread_name}",
            description=(
                f"*{opener}*\n\n"
                + (f"**Question:** *{question}*\n\n" if question else "")
                + card_lines
            ),
            colour=0x6B3FA0,
        )
        overview.set_footer(text="Scroll ▶ for each card · !tarot detail for full readings")
        pages.append(overview)

        for i, (card, pos) in enumerate(zip(cards, positions), 1):
            pos_name = _pos_name(pos)
            embed = make_single_embed(card, position=pos_name, detail=detail)
            pos_description = _pos_desc(pos)
            if pos_description:
                embed.insert_field_at(0, name="✦ Position", value=f"*{pos_description}*", inline=False)
            embed.set_author(name=f"Card {i} of {n_cards} · {spread_name}")
            pages.append(embed)

        await menu(ctx, pages, DEFAULT_CONTROLS)

    # ── Commands ──────────────────────────────────────────────────────────────

    @commands.group(name="tarot", invoke_without_command=True)
    @commands.guild_only()
    async def tarot(self, ctx: commands.Context, *, question: str = None):
        """
        Draw a single tarot card.

        **Usage:**
        `!tarot` — draw a card
        `!tarot What should I focus on today?` — draw with a question
        `!tarot wands` / `!tarot major` — draw from a specific pool

        Use `!tarot help` for a full list of commands.
        """
        filter_arg = None
        if question and question.lower() in SUIT_MAP:
            filter_arg = question.lower()
            question = None

        await self._do_draw(ctx, 1, "Single Card", ["Your Card"], question, filter_arg)

    @tarot.command(name="detail")
    @commands.guild_only()
    async def tarot_detail(self, ctx: commands.Context, *, question: str = None):
        """Draw a single card with the full detailed reading."""
        filter_arg = None
        if question and question.lower() in SUIT_MAP:
            filter_arg = question.lower()
            question = None

        await self._do_draw(ctx, 1, "Single Card (Detailed)", ["Your Card"],
                            question, filter_arg, detail=True)

    @tarot.command(name="ppf", aliases=["three", "past"])
    @commands.guild_only()
    async def tarot_ppf(self, ctx: commands.Context, *, question: str = None):
        """
        Past · Present · Future — a three-card spread.

        `!tarot ppf How will this situation resolve?`
        """
        s = BUILT_IN_SPREADS["ppf"]
        await self._do_draw(ctx, 3, s["name"], s["positions"], question)

    @tarot.command(name="celtic", aliases=["cross", "full"])
    @commands.guild_only()
    async def tarot_celtic(self, ctx: commands.Context, *, question: str = None):
        """
        Full ten-card Celtic Cross spread.

        Use for significant questions. Paginated embeds — scroll through each card.
        """
        s = BUILT_IN_SPREADS["celtic"]
        await self._do_draw(ctx, 10, s["name"], s["positions"], question)

    @tarot.command(name="daily")
    @commands.guild_only()
    async def tarot_daily(self, ctx: commands.Context):
        """Draw your daily card. One per user every 22 hours."""
        if not await self._gate(ctx):
            return

        ok, remaining = await self._check_cooldown(ctx, "last_daily_time", "daily_cooldown")
        if not ok:
            h, rem = divmod(remaining, 3600)
            m = rem // 60
            return await ctx.send(
                f"🌙 Your daily card is resting. Come back in **{h}h {m}m**."
            )

        allow_rev = await self.config.guild(ctx.guild).allow_reversals()
        card = draw_cards(1, CARDS, allow_reversed=allow_rev)[0]

        await self._set_time(ctx, "last_daily_time")
        await self._save_reading(ctx, [card], "Daily Card")

        embed = make_single_embed(card, detail=False)
        embed.set_author(
            name=f"Your Daily Card · {datetime.now(timezone.utc).strftime('%A, %d %B %Y')}"
        )
        await ctx.send(embed=embed)

    @tarot.command(name="spread")
    @commands.guild_only()
    async def tarot_spread(self, ctx: commands.Context, spread_name: str, *, question: str = None):
        """
        Draw a custom spread by name.

        `!tarot spread <name> [question]`
        See `!tarot spreads` for available custom spreads.
        """
        custom = await self.config.guild(ctx.guild).custom_spreads()
        key = spread_name.lower()
        if key not in custom:
            available = ", ".join(f"`{k}`" for k in custom) or "None yet."
            return await ctx.send(
                f"No custom spread named `{spread_name}`.\n"
                f"Available: {available}\nCreate one with `!tarotset spread add`."
            )
        s = custom[key]
        await self._do_draw(ctx, len(s["positions"]), s["name"], s["positions"], question)

    @tarot.command(name="spreads")
    @commands.guild_only()
    async def tarot_spreads(self, ctx: commands.Context):
        """List all available spreads — built-in and custom."""
        custom = await self.config.guild(ctx.guild).custom_spreads()
        embed = discord.Embed(title="Available Tarot Spreads", colour=0x6B3FA0)

        bi = "\n".join(
            f"**`!tarot {k}`** — {s['name']} ({len(s['positions'])} cards)\n> {s['description']}"
            for k, s in BUILT_IN_SPREADS.items()
        )
        embed.add_field(name="Built-in Spreads", value=bi, inline=False)

        if custom:
            cs = "\n".join(
                f"**`!tarot spread {k}`** — {v['name']} ({len(v['positions'])} cards)\n"
                f"> {v.get('description', 'No description.')}"
                for k, v in custom.items()
            )
            embed.add_field(name="Custom Spreads", value=cs, inline=False)
        else:
            embed.add_field(
                name="Custom Spreads",
                value="None yet. Admins: `!tarotset spread add`",
                inline=False,
            )
        await ctx.send(embed=embed)

    # ── Card lookup ───────────────────────────────────────────────────────────

    @tarot.command(name="card")
    @commands.guild_only()
    async def tarot_card(self, ctx: commands.Context, *, card_name: str):
        """
        Look up any card by name — shows both upright and reversed meanings.

        `!tarot card The Moon`
        `!tarot card ace of cups`
        """
        name_lower = card_name.lower().strip()
        match = None
        for card in CARDS:
            if card["name"].lower() == name_lower:
                match = card
                break
            if card["name"].lower().replace("the ", "") == name_lower.replace("the ", ""):
                match = card
                break

        if not match:
            candidates = [c for c in CARDS if name_lower in c["name"].lower()]
            if len(candidates) == 1:
                match = candidates[0]
            elif candidates:
                names = ", ".join(f"`{c['name']}`" for c in candidates[:5])
                return await ctx.send(f"Multiple matches: {names}. Be more specific.")
            else:
                return await ctx.send(
                    f"No card found for `{card_name}`. Check the spelling or use the full name."
                )

        colour = card_colour(match)
        embed = discord.Embed(
            title=f"{SUIT_EMOJI.get(match.get('suit'), '☽')} {match['name']}",
            description=f"*{match['flavour']}*",
            colour=colour,
        )
        embed.add_field(
            name=f"✦ Upright · {' · '.join(match['keywords_upright'])}",
            value=match["meaning_full"],
            inline=False,
        )
        embed.add_field(
            name=f"↩ Reversed · {' · '.join(match['keywords_reversed'])}",
            value=match["meaning_reversed_full"],
            inline=False,
        )
        if match.get("image_url"):
            embed.set_thumbnail(url=match["image_url"])
        embed.set_footer(
            text=f"{match['arcana'].capitalize()} Arcana"
            + (f" · {match['suit'].capitalize()}" if match["suit"] else "")
            + f" · #{match['number']}"
        )
        await ctx.send(embed=embed)

    # ── Journal ───────────────────────────────────────────────────────────────

    @tarot.command(name="history", aliases=["journal"])
    @commands.guild_only()
    async def tarot_history(self, ctx: commands.Context, page: int = 1):
        """
        View your reading journal.

        `!tarot history` — most recent readings
        `!tarot history 2` — older readings
        """
        history = list(reversed(await self.config.user(ctx.author).history()))
        if not history:
            return await ctx.send("You have no reading history yet. Try `!tarot` or `!tarot ppf`!")

        per_page = 5
        pages = [history[i: i + per_page] for i in range(0, len(history), per_page)]

        if page < 1 or page > len(pages):
            return await ctx.send(f"Page {page} doesn't exist. You have {len(pages)} page(s).")

        embed = discord.Embed(
            title=f"📖 {ctx.author.display_name}'s Reading Journal",
            description=f"Page {page} of {len(pages)}  ·  {len(history)} total readings",
            colour=0x6B3FA0,
        )
        for entry in pages[page - 1]:
            ts = datetime.fromisoformat(entry["timestamp"])
            date_str = ts.strftime("%d %b %Y, %H:%M UTC")
            cards_str = "\n".join(
                f"{'↩ ' if c['reversed'] else ''}*{c['name']}*"
                + (" *(reversed)*" if c["reversed"] else "")
                for c in entry["cards"]
            )
            title = f"{entry['spread']} — {date_str}"
            if entry.get("question"):
                title += f"\n*\"{entry['question']}\"*"
            embed.add_field(name=title, value=cards_str or "—", inline=False)

        embed.set_footer(text="!tarot history <page> to navigate · !tarot clearhistory to reset")
        await ctx.send(embed=embed)

    @tarot.command(name="clearhistory")
    @commands.guild_only()
    async def tarot_clearhistory(self, ctx: commands.Context):
        """Clear your personal reading history."""
        await self.config.user(ctx.author).history.set([])
        await ctx.send("🌙 Your reading history has been cleared.")

    # ── Admin ─────────────────────────────────────────────────────────────────

    @commands.group(name="tarotset")
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    async def tarotset(self, ctx: commands.Context):
        """Configure the Tarot cog for this server."""
        if ctx.invoked_subcommand is None:
            await ctx.send_help()

    @tarotset.command(name="enable")
    async def tarotset_enable(self, ctx: commands.Context, enabled: bool):
        """Enable or disable tarot. `!tarotset enable true/false`"""
        await self.config.guild(ctx.guild).enabled.set(enabled)
        await ctx.send(f"Tarot is now **{'enabled ✦' if enabled else 'disabled'}**.")

    @tarotset.command(name="reversals")
    async def tarotset_reversals(self, ctx: commands.Context, enabled: bool):
        """Enable or disable reversed cards. `!tarotset reversals true/false`"""
        await self.config.guild(ctx.guild).allow_reversals.set(enabled)
        await ctx.send(f"Reversals are now **{'enabled' if enabled else 'disabled'}**.")

    @tarotset.command(name="cooldown")
    async def tarotset_cooldown(self, ctx: commands.Context, seconds: int):
        """Set seconds between readings per user. `!tarotset cooldown 120`"""
        if seconds < 0:
            return await ctx.send("Must be 0 or greater.")
        await self.config.guild(ctx.guild).spread_cooldown.set(seconds)
        await ctx.send(f"Spread cooldown set to **{seconds}s**.")

    @tarotset.command(name="dailycooldown")
    async def tarotset_dailycooldown(self, ctx: commands.Context, hours: int):
        """Set daily card cooldown in hours. `!tarotset dailycooldown 22`"""
        if hours < 1:
            return await ctx.send("Must be at least 1 hour.")
        await self.config.guild(ctx.guild).daily_cooldown.set(hours * 3600)
        await ctx.send(f"Daily card cooldown set to **{hours}h**.")

    @tarotset.command(name="channel")
    async def tarotset_channel(self, ctx: commands.Context, *channels: discord.TextChannel):
        """
        Restrict tarot to specific channels. No arguments = allow everywhere.

        `!tarotset channel #tarot #general`
        """
        if not channels:
            await self.config.guild(ctx.guild).allowed_channels.set([])
            return await ctx.send("Tarot is now allowed in **all channels**.")
        ids = [c.id for c in channels]
        await self.config.guild(ctx.guild).allowed_channels.set(ids)
        await ctx.send(f"Tarot restricted to: {' '.join(c.mention for c in channels)}")

    @tarotset.group(name="spread")
    async def tarotset_spread(self, ctx: commands.Context):
        """Manage custom spreads."""
        if ctx.invoked_subcommand is None:
            await ctx.send_help()

    @tarotset_spread.command(name="add")
    async def tarotset_spread_add(self, ctx: commands.Context):
        """
        Interactively create a custom spread.

        `!tarotset spread add` — guided wizard
        """
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            await ctx.send(
                "**Custom Spread Wizard** ✦\nType `cancel` at any time to abort.\n\n"
                "**Step 1:** What should this spread be called? (e.g. `Mind Body Spirit`)"
            )
            msg = await self.bot.wait_for("message", check=check, timeout=60)
            if msg.content.lower() == "cancel":
                return await ctx.send("Cancelled.")
            display_name = msg.content.strip()
            key = display_name.lower().replace(" ", "_")

            await ctx.send(
                "**Step 2:** Enter the position names, comma-separated.\n"
                "(e.g. `Mind, Body, Spirit`) — up to 10 positions."
            )
            msg = await self.bot.wait_for("message", check=check, timeout=120)
            if msg.content.lower() == "cancel":
                return await ctx.send("Cancelled.")
            positions = [p.strip() for p in msg.content.split(",") if p.strip()]
            if not 1 <= len(positions) <= 10:
                return await ctx.send("Please provide between 1 and 10 positions.")

            await ctx.send("**Step 3:** Provide a short description for this spread.")
            msg = await self.bot.wait_for("message", check=check, timeout=60)
            if msg.content.lower() == "cancel":
                return await ctx.send("Cancelled.")
            description = msg.content.strip()

        except asyncio.TimeoutError:
            return await ctx.send("Timed out. Spread creation cancelled.")

        async with self.config.guild(ctx.guild).custom_spreads() as spreads:
            spreads[key] = {
                "name": display_name,
                "positions": positions,
                "description": description,
            }

        pos_preview = "\n".join(f"  {i+1}. {p}" for i, p in enumerate(positions))
        await ctx.send(
            f"✦ Custom spread **{display_name}** created!\n"
            f"Use it with: `!tarot spread {key}`\n\n"
            f"**Positions:**\n{pos_preview}"
        )

    @tarotset_spread.command(name="remove")
    async def tarotset_spread_remove(self, ctx: commands.Context, spread_name: str):
        """Remove a custom spread. `!tarotset spread remove <name>`"""
        async with self.config.guild(ctx.guild).custom_spreads() as spreads:
            key = spread_name.lower()
            if key not in spreads:
                return await ctx.send(f"No custom spread named `{spread_name}`.")
            removed = spreads.pop(key)
        await ctx.send(f"Removed: **{removed['name']}**.")

    @tarotset_spread.command(name="list")
    async def tarotset_spread_list(self, ctx: commands.Context):
        """List all custom spreads."""
        custom = await self.config.guild(ctx.guild).custom_spreads()
        if not custom:
            return await ctx.send("No custom spreads configured.")
        lines = [
            f"**{v['name']}** (key: `{k}`, {len(v['positions'])} cards)"
            for k, v in custom.items()
        ]
        await ctx.send("**Custom Spreads:**\n" + "\n".join(lines))

    @tarotset.command(name="settings")
    async def tarotset_settings(self, ctx: commands.Context):
        """Show current tarot configuration."""
        cfg = await self.config.guild(ctx.guild).all()
        allowed = cfg["allowed_channels"]
        channels_str = " ".join(f"<#{cid}>" for cid in allowed) if allowed else "All channels"

        embed = discord.Embed(title="Tarot Settings", colour=0x6B3FA0)
        embed.add_field(name="Enabled", value="✅" if cfg["enabled"] else "❌", inline=True)
        embed.add_field(name="Reversals", value="✅" if cfg["allow_reversals"] else "❌", inline=True)
        embed.add_field(name="Spread Cooldown", value=f"{cfg['spread_cooldown']}s", inline=True)
        embed.add_field(name="Daily Cooldown", value=f"{cfg['daily_cooldown'] // 3600}h", inline=True)
        embed.add_field(name="Custom Spreads", value=str(len(cfg["custom_spreads"])), inline=True)
        embed.add_field(name="Allowed Channels", value=channels_str, inline=False)
        await ctx.send(embed=embed)
