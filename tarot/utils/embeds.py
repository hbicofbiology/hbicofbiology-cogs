"""
Embed builder utilities for the Tarot cog.
All Discord embed construction lives here.
"""

import discord
from typing import Optional, List, Tuple, Dict
from datetime import datetime, timezone


# ------------------------------------------------------------------ #
#  Colour palette — one per arcana / suit
# ------------------------------------------------------------------ #

COLOURS = {
    "major": 0x6A0572,   # deep violet
    "wands": 0xD4380D,   # fiery orange-red
    "cups": 0x1677FF,    # deep ocean blue
    "swords": 0x87CEEB,  # steel blue
    "pentacles": 0x52C41A,  # earthy green
}


def _card_colour(card: dict) -> int:
    if card["arcana"] == "major":
        return COLOURS["major"]
    return COLOURS.get(card.get("suit", ""), 0x7B68EE)


def _orientation(card: dict) -> str:
    return "🔃 Reversed" if card["reversed"] else "☀️ Upright"


def _keywords(card: dict) -> str:
    keys = card["keywords_reversed"] if card["reversed"] else card["keywords"]
    return " · ".join(keys)


def _meaning_short(card: dict) -> str:
    return card["meaning_short"]


def _meaning_long(card: dict) -> str:
    return card["meaning_reversed"] if card["reversed"] else card["meaning_upright"]


def _arcana_label(card: dict) -> str:
    if card["arcana"] == "major":
        return f"Major Arcana · {card['number']}"
    suit = card.get("suit", "").title()
    return f"Minor Arcana · {suit}"


# ------------------------------------------------------------------ #
#  Single card embed
# ------------------------------------------------------------------ #

def build_card_embed(
    card: dict,
    *,
    question: Optional[str] = None,
    flavour: str = "",
    detailed: bool = False,
    lookup_mode: bool = False,
) -> discord.Embed:

    title = card["name"]
    if not lookup_mode:
        title += f"  —  {_orientation(card)}"

    embed = discord.Embed(
        title=title,
        color=_card_colour(card),
    )

    if flavour and not lookup_mode:
        embed.description = f"*{flavour}*"

    if question:
        embed.add_field(name="✦ Your Question", value=f"> {question}", inline=False)

    embed.add_field(
        name=_arcana_label(card),
        value=f"**Keywords:** {_keywords(card)}",
        inline=False,
    )

    if detailed or lookup_mode:
        # Full interpretation
        if lookup_mode:
            embed.add_field(
                name="☀️ Upright Meaning",
                value=card["meaning_upright"],
                inline=False,
            )
            embed.add_field(
                name="🔃 Reversed Meaning",
                value=card["meaning_reversed"],
                inline=False,
            )
        else:
            label = "🔃 Reversed Interpretation" if card["reversed"] else "☀️ Interpretation"
            embed.add_field(
                name=label,
                value=_meaning_long(card),
                inline=False,
            )

        # Correspondences
        corr_parts = []
        if card.get("element"):
            corr_parts.append(f"**Element:** {card['element']}")
        if card.get("planet"):
            corr_parts.append(f"**Astrology:** {card['planet']}")
        if corr_parts:
            embed.add_field(
                name="✦ Correspondences",
                value="\n".join(corr_parts),
                inline=True,
            )
    else:
        # Short meaning only
        embed.add_field(
            name="✦ Reading",
            value=f"*{_meaning_short(card)}*",
            inline=False,
        )

    if card.get("image_url"):
        embed.set_thumbnail(url=card["image_url"])

    embed.set_footer(text="React 🔍 for deeper interpretation" if not detailed and not lookup_mode else "Tarot · Rider-Waite")

    return embed


# ------------------------------------------------------------------ #
#  Spread embeds
# ------------------------------------------------------------------ #

def build_spread_embed(
    spread: dict,
    paired: List[Tuple[dict, dict]],  # [(position, card), ...]
    *,
    question: Optional[str] = None,
    flavour: str = "",
) -> List[discord.Embed]:
    """
    Build a list of embeds for a spread.
    - First embed: spread title + optional question + flavour
    - Subsequent embeds: one per card (to avoid field limits on large spreads)
    """
    embeds = []

    # Header embed
    header = discord.Embed(
        title=f"✦ {spread['name']}",
        description=(
            (f"*{flavour}*\n\n" if flavour else "")
            + spread["description"]
        ),
        color=0x6A0572,
    )
    if question:
        header.add_field(name="Your Question", value=f"> {question}", inline=False)
    header.add_field(
        name=f"{len(paired)} cards drawn",
        value="\u200b",
        inline=False,
    )
    embeds.append(header)

    # Card embeds — batch up to 5 positions per embed to stay within limits
    BATCH = 5
    batch_embed = None

    for i, (position, card) in enumerate(paired):
        if i % BATCH == 0:
            batch_embed = discord.Embed(color=_card_colour(card))
            embeds.append(batch_embed)

        orient = _orientation(card)
        pos_name = position["name"]
        pos_desc = position.get("description", "")

        field_name = f"**{i+1}. {pos_name}** — {card['name']} {orient}"
        field_val = ""
        if pos_desc:
            field_val += f"*{pos_desc}*\n"
        field_val += f"**Keywords:** {_keywords(card)}\n"
        field_val += f"*{_meaning_short(card)}*"

        batch_embed.add_field(
            name=field_name,
            value=field_val,
            inline=False,
        )

    if embeds:
        embeds[-1].set_footer(text="Tarot · Rider-Waite  ·  Use [p]tarot card <name> for full card details")

    return embeds


# ------------------------------------------------------------------ #
#  Daily card embed
# ------------------------------------------------------------------ #

def build_daily_embed(
    card: dict,
    user: discord.User,
    *,
    flavour: str = "",
) -> discord.Embed:
    embed = discord.Embed(
        title=f"🌅 Daily Card for {user.display_name}",
        description=(
            (f"*{flavour}*\n\n" if flavour else "")
            + f"**{card['name']}**  —  {_orientation(card)}"
        ),
        color=_card_colour(card),
        timestamp=datetime.now(timezone.utc),
    )
    embed.add_field(
        name=_arcana_label(card),
        value=f"**Keywords:** {_keywords(card)}",
        inline=False,
    )
    embed.add_field(
        name="✦ Reflection for Today",
        value=f"*{_meaning_short(card)}*",
        inline=False,
    )
    embed.add_field(
        name="☀️ Carry This With You",
        value=_meaning_long(card),
        inline=False,
    )
    if card.get("image_url"):
        embed.set_thumbnail(url=card["image_url"])
    embed.set_footer(text="Your next daily card will be available in ~20 hours.")
    return embed


# ------------------------------------------------------------------ #
#  History embed
# ------------------------------------------------------------------ #

def build_history_embed(
    entries: List[dict],
    user: discord.User,
    page: int,
    total_pages: int,
) -> discord.Embed:
    embed = discord.Embed(
        title=f"📖 {user.display_name}'s Reading History",
        color=0x4B0082,
    )

    for entry in entries:
        dt = datetime.fromisoformat(entry["timestamp"])
        date_str = dt.strftime("%d %b %Y")
        spread_name = entry.get("spread", "Unknown")
        question = entry.get("question")
        cards = entry.get("cards", [])

        card_strs = []
        for c in cards:
            rev = " (R)" if c.get("reversed") else ""
            card_strs.append(f"{c['name']}{rev}")

        val = f"**Spread:** {spread_name}\n"
        if question:
            val += f"**Question:** {question}\n"
        val += f"**Cards:** {', '.join(card_strs)}"

        embed.add_field(
            name=f"📅 {date_str}",
            value=val,
            inline=False,
        )

    embed.set_footer(text=f"Page {page} of {total_pages}  ·  Use [p]tarot history <page> for more")
    return embed


# ------------------------------------------------------------------ #
#  Help embed
# ------------------------------------------------------------------ #

def build_help_embed(prefix: str) -> discord.Embed:
    p = prefix
    embed = discord.Embed(
        title="✦ Tarot — Command Reference",
        description="A full tarot system for Red Discord Bot.",
        color=0x6A0572,
    )
    embed.add_field(
        name="🃏 Readings",
        value=(
            f"`{p}tarot` or `{p}tarot draw [question]` — Single card draw\n"
            f"`{p}tarot three [question]` — Past · Present · Future\n"
            f"`{p}tarot celtic [question]` — Celtic Cross (10 cards)\n"
            f"`{p}tarot spread <name> [question]` — Named spread\n"
            f"`{p}tarot daily` — Your card of the day (cooldown applies)"
        ),
        inline=False,
    )
    embed.add_field(
        name="📚 Spreads",
        value=(
            "`three_card` · `celtic_cross` · `relationship` · "
            "`decision` · `shadow_work` · `year_ahead`"
        ),
        inline=False,
    )
    embed.add_field(
        name="🔍 Card Lookup",
        value=(
            f"`{p}tarot card <name>` — Full card details (upright + reversed)\n"
            f"`{p}tarot list [filter]` — List cards by filter\n"
            f"**Filters:** `all` · `major` · `minor` · `wands` · `cups` · `swords` · `pentacles`"
        ),
        inline=False,
    )
    embed.add_field(
        name="📖 History",
        value=(
            f"`{p}tarot history [page]` — View your reading journal\n"
            f"`{p}tarot clearhistory` — Clear your journal"
        ),
        inline=False,
    )
    embed.add_field(
        name="⚙️ Admin (Manage Server required)",
        value=(
            f"`{p}tarot set` — View current settings\n"
            f"`{p}tarot set cooldown <hours>` — Daily card cooldown (1–48h)\n"
            f"`{p}tarot set reversals <true/false>` — Toggle reversed cards\n"
            f"`{p}tarot set filter <filter>` — Default card pool\n"
            f"`{p}tarot set flavour <true/false>` — Toggle flavour text\n"
            f"`{p}tarot set historylimit <n>` — Max readings stored per user"
        ),
        inline=False,
    )
    embed.set_footer(text="React 🔍 after a single draw for deeper interpretation.")
    return embed
