# 🐊 Swamp Race

A multiplayer swamp creature racing game for [Red-DiscordBot V3](https://github.com/Cog-Creators/Red-DiscordBot). Players join a lobby, get assigned a random swamp creature, then watch as their creature sprints through the muck in a live-updating race track. Features betting, prize pooling, placement stats, and animated GIF visuals. Inspired by Redjumpman's original Race cog from Jumper-Plugins.

---

## Features

- **Live race board** — a text track that edits every 1.5 seconds showing each creature's position
- **16 unique swamp creatures** — each with a name, icon, and speed tier (1–10)
- **Lobby system** — configurable wait time before the race starts; up to 14 human racers
- **Betting** — spectators and players can bet on a racer to win
- **Prize pooling** — optional 60/30/10% split for top 3 in larger races
- **Placement stats** — tracks 1st, 2nd, 3rd, and losses per user
- **Bot fill-in** — if only one human joins, the bot races alongside them so the race still runs
- **Fully configurable** — wait time, prize amounts, bet limits, pooling toggle, payout minimums
- GDPR-compliant user data deletion support

---

## Installation

```
[p]repo add hbicofbiology-cogs https://github.com/hbicofbiology/hbicofbiology-cogs
[p]cog install hbicofbiology-cogs race
[p]load race
```

Requires **Red-DiscordBot 3.5.0+**. No additional pip dependencies.

---

## How to Play

1. Someone starts a race with `[p]race start` — a lobby embed appears with a countdown
2. Other players join with `[p]race enter` during the wait period
3. Spectators can bet on a racer with `[p]race bet <amount> <@player>`
4. When the timer expires, each player is assigned a random swamp creature
5. The race board appears and updates live every 1.5 seconds as creatures advance
6. Results are posted with placements, medals, and any prize or bet payouts

If only one human enters, the bot fills in as a second racer so the race always runs.

---

## The Creatures

16 swamp creatures compete, each with a speed tier affecting their movement rolls:

| Creature | Icon | Speed |
|---|---|---|
| Slime Sprinter | 🟢 | 9 |
| Fen Phantom | 👻 | 8 |
| Murk Serpent | 🐍 | 8 |
| Mire Stalker | 🐸 | 7 |
| Toad Terror | 🐸 | 7 |
| Bog Lurker | 🐊 | 6 |
| Gator Ghoul | 🐲 | 6 |
| Fungal Fury | 🍄 | 6 |
| Mud Crawler | 🦎 | 5 |
| Bayou Beast | 🦖 | 5 |
| Quicksand Quill | 🦔 | 5 |
| Mangrove Mauler | 🌴 | 5 |
| Swamp Fiend | 👹 | 4 |
| Vine Wraith | 🌾 | 4 |
| Moss Creeper | 🌿 | 3 |
| Leech Lord | 🪱 | 3 |

Speed affects both base movement rolls and bonus roll probability — but every race is still random. Never count out the Leech Lord.

---

## User Commands

| Command | Description |
|---|---|
| `[p]race start` | Start a new race lobby |
| `[p]race enter` | Join an active lobby before it starts |
| `[p]race bet <amount> <@player>` | Bet on a player to win — must be placed before the race starts |
| `[p]race stats [user]` | View placement stats for yourself or another user |
| `[p]race version` | Show the cog version |

---

## Admin Commands

All `setrace` commands require **Administrator** permission.

### General

| Command | Description |
|---|---|
| `[p]setrace wait <seconds>` | Set the lobby wait time before the race starts (minimum 10s, default 60s) |
| `[p]setrace prize <amount>` | Set the prize for winning (0 to disable) |
| `[p]setrace togglepool` | Toggle prize pooling — splits prize 60/30/10% across top 3 (requires 4+ racers) |
| `[p]setrace payoutmin <players>` | Minimum extra human players needed for prizes to pay out (0 = always) |
| `[p]setrace wipe` | ⚠️ Wipe all race settings and stats for this server |

### Betting

| Command | Description |
|---|---|
| `[p]setrace bet toggle` | Enable or disable betting |
| `[p]setrace bet min <amount>` | Set the minimum bet amount (default 10) |
| `[p]setrace bet max <amount>` | Set the maximum bet amount (default 50) |
| `[p]setrace bet multiplier <value>` | Set the bet payout multiplier (default 2x) |

### Debug

| Command | Description |
|---|---|
| `[p]race clear` | Force-clear a stuck race (admin only, hidden) |

---

## Default Settings

| Setting | Default |
|---|---|
| Lobby wait time | 60 seconds |
| Prize | 100 credits |
| Prize pooling | Off |
| Payout minimum | 0 (always pays) |
| Betting | Enabled |
| Bet minimum | 10 |
| Bet maximum | 50 |
| Bet multiplier | 2x |
| Max racers | 14 |

---

## Data Storage

The following is stored per user per server:

- 1st, 2nd, and 3rd place finish counts
- Loss count (finishing 4th or lower)

Server-level data: total games played, all race settings.

User data can be deleted on request via Red's `red_delete_data_for_user` handler.

---

## Credits

Original Race concept by **Redjumpman** ([Jumper-Plugins](https://github.com/redjumpman/Jumper-Plugins)).
Swamp creature recreation by **hbicofbiology**.
