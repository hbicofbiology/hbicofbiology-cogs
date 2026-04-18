# 🧬 hbicofbiology-cogs

Custom cogs for [Red-DiscordBot V3](https://github.com/Cog-Creators/Red-DiscordBot). A collection of games, social systems, utilities, and community tools built for phagebot.

---

## Installation

```
[p]repo add hbicofbiology-cogs https://github.com/hbicofbiology/hbicofbiology-cogs
```

Then install any cog:

```
[p]cog install hbicofbiology-cogs <cogname>
[p]load <cogname>
```

---

## Cogs

### 🎮 Games & Economy

| Cog | Description |
|---|---|
| [Casino](casino/README.md) | Nine casino games — Blackjack, Coin Flip, Cups, Dice, Hi-Lo, Craps, War, All-In, and Double or Nothing. Configurable per game with stats tracking and economy integration. |
| [Race](race/README.md) | Multiplayer swamp creature racing. Join a lobby, get assigned a creature, and watch a live race track update in real time. Supports betting and prize pooling. |
| [SwampHunt](swamphunt/README.md) | Passive swamp creature encounters. Creatures randomly appear in chat — type `snag` to catch them and earn credits. One of them will drain your wallet instead. |
| [ChainReaction](chainreaction/README.md) | Turn-based word game with a join lobby, rotating rules, real word validation, and a 3-life elimination system. Last one standing wins. |

### 🐾 Community & Social

| Cog | Description |
|---|---|
| [RaiseCat](raisecat/README.md) | Raise a shared server cat together. Feed, play, groom, vet, and train it through four pixel art life stages — from kitten to crowned elder. |
| [Marriage](marriage/README.md) | Marriage system with economy costs, contentment tracking, gifts, consent-based actions, and profile pages showing spouses, exes, and relationship stats. |
| [LoveConfessions](loveconfessions/README.md) | Send anonymous or public confessions to other members via DM. Anonymous mode uses a Discord modal so the sender is never revealed. |

### 🎴 Fun & Flavour

| Cog | Description |
|---|---|
| [Tarot](tarot/README.md) | Full 78-card Rider-Waite tarot system. Single draws, three-card spreads, Celtic Cross, daily card, card lookup, reading journal, and custom server spreads. |
| [MoodMusic](moodmusic/README.md) | Curated mood-based Spotify recommendations. Admins build playlists per mood; users request a random track and get a rich embed with album art and a Spotify link. |

### 🔧 Utility

| Cog | Description |
|---|---|
| [RoleDropdown](roledropdown/README.md) | Persistent Discord select-menu dropdowns for self-assignable roles. Members pick and remove roles from a dropdown — no commands needed. |
| [Transcribe](transcribe/README.md) | Auto-transcribes Discord voice messages using OpenAI Whisper. Replies to voice messages with a clean embed showing the transcription. Requires your own OpenAI API key. |

---

## Requirements

All cogs require **Red-DiscordBot 3.5.0+** and **Python 3.8+**.

| Cog | Extra Dependencies |
|---|---|
| ChainReaction | `pip install wordfreq` |
| MoodMusic | `aiohttp` (included with Red) |
| Transcribe | `aiohttp` (included with Red) + OpenAI API key |
| All others | None |

---

## Credits

- **Casino** and **Race** inspired by [Redjumpman's Jumper-Plugins](https://github.com/redjumpman/Jumper-Plugins)
- Everything else original

---

*Made with ☕ and too many late nights by hbicofbiology*
