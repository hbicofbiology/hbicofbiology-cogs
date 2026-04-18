# 🐱 RaiseCat

A collaborative virtual pet cog for [Red-DiscordBot V3](https://github.com/Cog-Creators/Red-DiscordBot). The entire server works together to raise a shared cat from a tiny kitten all the way to a crowned elder. Feed it, play with it, groom it, take it to the vet, teach it tricks — and compete on the leaderboard for best caretaker.

Each life stage has its own custom pixel art GIF. 🐾

---

## Life Stages

The cat grows through four stages based on accumulated XP:

| Stage | XP Required | Label |
|---|---|---|
| 🐱 Kitten | 0 | Starting stage |
| 🐈 Young Cat | 100 | |
| 🐈‍⬛ Adult Cat | 500 | |
| 👑 Elder Cat | 1,500 | Final stage |

Each stage-up triggers a special evolution embed with the new pixel art GIF.

---

## Features

- **One cat per server** — the whole community shares and cares for it together
- **Four stats** — Hunger, Happiness, Cleanliness, and Health, each shown as a visual bar
- **XP and life stages** — care actions earn XP; enough XP triggers a stage evolution
- **9 learnable tricks** — from Sit all the way up to Filing Taxes
- **Leaderboard** — tracks every member's care contributions broken down by action
- **Per-user cooldowns** — each action has its own cooldown so no one can monopolise care
- **Random flavour** — random food items, toys, and reaction messages keep it fresh
- **Custom pixel art GIFs** — bundled stage-specific art displayed in embeds
- **14 breeds and 10 personality traits** — randomly assigned on adoption

---

## Installation

```
[p]repo add hbicofbiology-cogs https://github.com/hbicofbiology/hbicofbiology-cogs
[p]cog install hbicofbiology-cogs raisecat
[p]load raisecat
```

Requires **Red-DiscordBot 3.5.0+** and **Python 3.8+**. No additional pip dependencies.

---

## Getting Started

An admin adopts a cat for the server:
```
[p]cat adopt
[p]cat adopt Noodle
```
The cat is assigned a random breed, personality, and name (if not provided). From there, anyone in the server can care for it.

---

## Commands

### User Commands

| Command | Description | Cooldown |
|---|---|---|
| `[p]cat` | Show the cat's current status (or prompt to adopt) | — |
| `[p]cat status` | View full stats, XP, stage, and learned tricks | — |
| `[p]cat feed` | Feed the cat 🍗 — raises Hunger and earns XP | 30 min |
| `[p]cat play` | Play with the cat 🎾 — raises Happiness and earns XP | 20 min |
| `[p]cat groom` | Groom the cat ✨ — raises Cleanliness and earns XP | 60 min |
| `[p]cat vet` | Take the cat to the vet 🏥 — raises Health and earns XP | 2 hours |
| `[p]cat train` | Attempt to teach the cat a new trick 🎓 — earns XP | 40 min |
| `[p]cat tricks` | View all tricks and which ones the cat has learned | — |
| `[p]cat leaderboard` | See the top 10 caretakers and their contribution breakdown | — |
| `[p]cat art` | Display the cat's current pixel art portrait full size | — |

### Admin Commands

Require **Administrator** or **Manage Guild** permission.

| Command | Description |
|---|---|
| `[p]cat adopt [name]` | Adopt a cat for the server — optionally provide a name |
| `[p]cat rename <name>` | Rename the server's cat (max 32 characters) |
| `[p]cat release` | ⚠️ Release the cat — deletes all progress and leaderboard data |

---

## Tricks

The cat can learn 9 tricks, unlocked by XP milestones. Success isn't guaranteed — harder tricks have lower success rates. Failing a training session still earns a small XP reward.

| Trick | XP Required | Difficulty |
|---|---|---|
| Sit | 0 | 1 |
| High Five | 50 | 2 |
| Roll Over | 100 | 3 |
| Fetch | 200 | 4 |
| Play Dead | 350 | 5 |
| Backflip | 500 | 6 |
| Open Doors | 750 | 7 |
| Hack the Mainframe | 1,000 | 8 |
| File Taxes | 1,500 | 9 |

---

## Cooldowns

| Action | Cooldown |
|---|---|
| Feed | 30 minutes |
| Play | 20 minutes |
| Groom | 60 minutes |
| Vet | 2 hours |
| Train | 40 minutes |

Cooldowns are per-user — multiple members can all care for the cat independently.

---

## Data Storage

The following is stored per server:

- The cat's full state: name, breed, personality, stats, XP, tricks, birth date
- Leaderboard: per-user action counts and total care points

Per user: cooldown timestamps for each care action. No personal data beyond Discord user IDs is stored.

---

*Made by hbicofbiology*
