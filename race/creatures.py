# Swamp creature roster for the Race cog
# Each creature has a name, an emoji/icon, a speed tier (1-10), and a GIF url.
# Speed tier affects how often the creature advances on each tick.

from dataclasses import dataclass, field
from typing import Optional
import random


@dataclass
class Creature:
    name: str
    icon: str
    speed: int          # 1 (slowest) – 10 (fastest)
    gif: str            # URL to a thematic GIF shown in embeds
    current: int = 0    # track position (runtime only)

    def advance(self) -> int:
        """Roll movement for one tick. Higher speed = better average roll."""
        # Base roll 0-3, plus a speed bonus roll
        base = random.randint(0, 3)
        bonus = 1 if random.randint(1, 10) <= self.speed else 0
        move = base + bonus
        self.current += move
        return move


# ──────────────────────────────────────────────────────────────
#  The Swamp Creature Roster
# ──────────────────────────────────────────────────────────────
# GIFs are from Tenor (public, embeddable). We use the c.tenor.com
# media URLs which are direct-linkable in Discord embeds.

CREATURE_POOL = [
    {
        "name": "Bog Lurker",
        "icon": "🐊",
        "speed": 6,
        "gif": "https://media.tenor.com/images/7c1b84e5f3cf4bc7b24e9e5ab567d0ac/tenor.gif",
    },
    {
        "name": "Mud Crawler",
        "icon": "🦎",
        "speed": 5,
        "gif": "https://media.tenor.com/images/2b8e7bf2f4c74daf859d9a7d70de6a4b/tenor.gif",
    },
    {
        "name": "Mire Stalker",
        "icon": "🐸",
        "speed": 7,
        "gif": "https://media.tenor.com/images/3a8e4bb43d5045e7b10ed2b7a19c78e1/tenor.gif",
    },
    {
        "name": "Swamp Fiend",
        "icon": "👹",
        "speed": 4,
        "gif": "https://media.tenor.com/images/e6dc0e37a8c64ef4b88e59cbf33aeeb5/tenor.gif",
    },
    {
        "name": "Fen Phantom",
        "icon": "👻",
        "speed": 8,
        "gif": "https://media.tenor.com/images/79a5c20eeabc4e9d9ebd0e7c8ff5f3d3/tenor.gif",
    },
    {
        "name": "Bayou Beast",
        "icon": "🦖",
        "speed": 5,
        "gif": "https://media.tenor.com/images/1dc6e9b78e1f4cdea0f50d0d7bb8e5a3/tenor.gif",
    },
    {
        "name": "Slime Sprinter",
        "icon": "🟢",
        "speed": 9,
        "gif": "https://media.tenor.com/images/8f5c4d3a51ec48e085d7e3f0c67d1ee3/tenor.gif",
    },
    {
        "name": "Moss Creeper",
        "icon": "🌿",
        "speed": 3,
        "gif": "https://media.tenor.com/images/d4e5f1c3a9b04e6eb2d7f8a1c3e5d7f9/tenor.gif",
    },
    {
        "name": "Gator Ghoul",
        "icon": "🐲",
        "speed": 6,
        "gif": "https://media.tenor.com/images/a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6/tenor.gif",
    },
    {
        "name": "Toad Terror",
        "icon": "🐸",
        "speed": 7,
        "gif": "https://media.tenor.com/images/f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4/tenor.gif",
    },
    {
        "name": "Vine Wraith",
        "icon": "🌾",
        "speed": 4,
        "gif": "https://media.tenor.com/images/b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7/tenor.gif",
    },
    {
        "name": "Murk Serpent",
        "icon": "🐍",
        "speed": 8,
        "gif": "https://media.tenor.com/images/c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8/tenor.gif",
    },
    {
        "name": "Quicksand Quill",
        "icon": "🦔",
        "speed": 5,
        "gif": "https://media.tenor.com/images/d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9/tenor.gif",
    },
    {
        "name": "Fungal Fury",
        "icon": "🍄",
        "speed": 6,
        "gif": "https://media.tenor.com/images/e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0/tenor.gif",
    },
    {
        "name": "Leech Lord",
        "icon": "🪱",
        "speed": 3,
        "gif": "https://media.tenor.com/images/f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1/tenor.gif",
    },
    {
        "name": "Mangrove Mauler",
        "icon": "🌴",
        "speed": 5,
        "gif": "https://media.tenor.com/images/a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2/tenor.gif",
    },
]

# These GIF URLs are used for the race start / finish announcement embeds
# They're themed around swamps and creatures running through muck
RACE_START_GIFS = [
    "https://media.tenor.com/YkBQFsMFYtIAAAAd/swamp-chasing-running.gif",
    "https://media.tenor.com/0K7pn9C7rxMAAAAC/creature-howudoin.gif",
    "https://media.tenor.com/BcJXjQv_F68AAAAC/bogmonster.gif",
]

RACE_FINISH_GIFS = [
    "https://media.tenor.com/YkBQFsMFYtIAAAAd/swamp-chasing-running.gif",
    "https://media.tenor.com/0K7pn9C7rxMAAAAC/creature-howudoin.gif",
    "https://media.tenor.com/8DqXmUb0zBkAAAAC/swamp-thing-2019.gif",
]


def pick_creatures(count: int) -> list[Creature]:
    """Return *count* unique Creature instances from the pool."""
    chosen = random.sample(CREATURE_POOL, min(count, len(CREATURE_POOL)))
    return [Creature(**c) for c in chosen]


def pick_start_gif() -> str:
    return random.choice(RACE_START_GIFS)


def pick_finish_gif() -> str:
    return random.choice(RACE_FINISH_GIFS)
