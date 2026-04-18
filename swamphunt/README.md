# 🐊 SwampHunt

A passive encounter cog for [Red-DiscordBot V3](https://github.com/Cog-Creators/Red-DiscordBot). As members chat, swamp creatures randomly emerge from the muck. The first person to type `snag` claims the creature and earns credits from Red's economy — or loses them if they grab the wrong thing.

No commands required for players. It just happens.

---

## Features

- **Fully passive** — triggers on normal chat messages, no user command needed
- **6 swamp creatures** — each with weighted spawn rates, reward ranges, and flavour text
- **One cursed encounter** — the Will-o'-Wisp steals credits instead of giving them
- **Configurable spawn chance, cooldown, and timeout** per server
- **Channel restrictions** — limit encounters to specific channels, or let them spawn anywhere
- **Custom emojis** — swap any creature's emoji for a custom server emoji
- **Admin force-spawn** — `[p]swampspawn` for testing without waiting for RNG

---

## Installation

```
[p]repo add hbicofbiology-cogs https://github.com/hbicofbiology/hbicofbiology-cogs
[p]cog install hbicofbiology-cogs swamphunt
[p]load swamphunt
```

Requires **Red-DiscordBot 3.5.0+**. No additional pip dependencies.

---

## How It Works

1. A non-bot, non-command message is sent in an eligible channel
2. The cog rolls against the spawn chance (default 6%)
3. If the guild-wide cooldown has passed, a creature spawns
4. The first person to type `snag` within the timeout window wins
5. Credits are deposited (or withdrawn for the Will-o'-Wisp) and a result message is sent
6. If nobody types `snag` in time, the creature slinks back into the swamp

Only one encounter can be active per server at a time.

---

## Creatures

| Creature | Emoji | Spawn Weight | Reward | Effect |
|---|---|---|---|---|
| Frog | 🐸 | Common | 25–70 credits | ✅ Gain |
| Snake | 🐍 | Common | 45–110 credits | ✅ Gain |
| Mudskipper | 🐟 | Common | 35–90 credits | ✅ Gain |
| Snapping Turtle | 🐢 | Uncommon | 65–130 credits | ✅ Gain |
| Alligator | 🐊 | Rare | 90–180 credits | ✅ Gain |
| Will-o'-Wisp | ✨ | Very Rare | 60–140 credits | ❌ Lose |

Higher reward creatures spawn less frequently. The Will-o'-Wisp drains up to its roll amount from your current balance — it can't take more than you have.

---

## Admin Commands

All `swamphuntset` commands require **Administrator** or **Manage Guild** permission.

### Settings Overview

Run `[p]swamphuntset` with no subcommand to see the current configuration.

### General

| Command | Description |
|---|---|
| `[p]swamphuntset toggle <true/false>` | Enable or disable passive encounters |
| `[p]swamphuntset chance <percent>` | Set spawn chance per message (e.g. `6` = 6%) |
| `[p]swamphuntset cooldown <seconds>` | Minimum seconds between spawns server-wide |
| `[p]swamphuntset timeout <seconds>` | How long players have to type `snag` (minimum 3s) |

### Channels

| Command | Description |
|---|---|
| `[p]swamphuntset channel add <#channel>` | Restrict encounters to a specific channel |
| `[p]swamphuntset channel remove <#channel>` | Remove a channel from the allow-list |
| `[p]swamphuntset channel clear` | Remove all restrictions — encounters spawn anywhere |

If no channels are set, encounters can spawn in any text channel.

### Emojis

| Command | Description |
|---|---|
| `[p]swamphuntset emoji <creature> <emoji>` | Set a custom emoji for a creature |
| `[p]swamphuntset emojis` | Show all current creature emojis |

Valid creature keys: `frog`, `mudskipper`, `alligator`, `snapping_turtle`, `snake`, `willowisp`

Aliases also accepted: `turtle`, `wisp`, `will-o-wisp`.

### Testing

| Command | Description |
|---|---|
| `[p]swampspawn` | Force an encounter in the current channel immediately |

---

## Default Settings

| Setting | Default |
|---|---|
| Enabled | ✅ Yes |
| Spawn chance | 6% per message |
| Spawn cooldown | 45 seconds |
| Encounter timeout | 12 seconds |
| Channel restriction | None (all channels) |

---

## Data Storage

No user data is stored. All settings are stored at the guild level (enabled state, spawn config, channel list, custom emojis). Encounter state is held in memory only and resets on bot restart.

---

*Made by hbicofbiology*
