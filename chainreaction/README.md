# ⚡ ChainReaction

A turn-based word game for [Red-DiscordBot V3](https://github.com/Cog-Creators/Red-DiscordBot). Players join via a button during a 60-second lobby, then compete in turn order — each with 10 seconds per turn to submit a valid English word that satisfies a randomly assigned rule. Fail in time, lose a life. Last one standing wins.

---

## Features

- **Discord UI lobby** — join button with live countdown, updates every second
- **Five rotating word rules** — minimum length, contains substring, ends with letter, no repeated letters, chain prefix
- **Real word validation** — powered by [`wordfreq`](https://github.com/rspeer/wordfreq); made-up words are rejected
- **10-second turn timer** — embed updates live; players can retry as many times as they like within the window
- **3-life system** — missing a turn costs a life; running out means elimination
- **Win stat tracking** — wins are recorded per member via Red's Config
- **Hybrid commands** — works as both prefix and slash commands

---

## Installation

```
[p]repo add hbicofbiology-cogs https://github.com/hbicofbiology/hbicofbiology-cogs
[p]cog install hbicofbiology-cogs chainreaction
[p]load chainreaction
```

### Dependencies

```
pip install wordfreq
```

`wordfreq` is required and must be installed before loading the cog. Red will not install it automatically.

Requires **Red-DiscordBot 3.5.0+**.

---

## How to Play

1. An admin runs `[p]chain start` in a text channel.
2. A lobby embed appears with a **🧪 Join** button and a 60-second countdown.
3. Players click Join. The lobby embed updates live to show the turn order.
4. Once the timer expires, the game starts automatically if **at least 2 players** joined.
5. Each turn, the current player is mentioned and given a word rule to satisfy.
6. The turn embed counts down from 10 seconds. The player types their word in chat — they can retry freely until time runs out.
7. A valid accepted word is shown to the channel. A failed turn costs 1 life (❤️❤️❤️ → ❤️❤️).
8. Eliminated players (0 lives) are skipped. The last player alive wins.

---

## Word Rules

Each turn, one of the following rules is randomly assigned:

| Rule | Description | Example |
|---|---|---|
| **Minimum length** | Word must be 4, 5, or 6+ letters | 4+ letters: `"storm"` ✅ `"cat"` ❌ |
| **Contains** | Word must contain a specific substring | Contains `SH`: `"share"` ✅ `"crane"` ❌ |
| **Ends with** | Word must end with a specific letter | Ends with `N`: `"carbon"` ✅ `"atlas"` ❌ |
| **No repeats** | No letter may appear more than once | `"frolic"` ✅ `"letter"` ❌ |
| **Chain prefix** | Word must start with the last 1–3 letters of the previous word | Prev: `"lamp"` → starts with `MP`: `"impact"` ✅ |

All submissions are also checked against the `wordfreq` English lexicon — invented words are rejected regardless of rule compliance.

---

## Commands

This cog uses a hybrid command group — all commands work with both prefix (`[p]chain`) and slash (`/chain`).

### User Commands

| Command | Description |
|---|---|
| `[p]chain status` | Show current lobby/game status in this channel (phase, players alive, last accepted word) |

### Admin Commands

Require **Administrator** or **Manage Guild** permission.

| Command | Description |
|---|---|
| `[p]chain start` | Open a 60-second lobby in the current channel with a Join button |
| `[p]chain stop` | Force-stop the lobby or game in the current channel |

> Only one game can run per channel at a time. Use `[p]chain stop` to clear a stuck game before starting a new one.

---

## Data Storage

This cog stores the following per user per server:

- **wins** — number of games won
- **games_played** — total games participated in
- **eliminations** — number of times the user was eliminated

Active game state (players, lives, turn order, current rule) is stored temporarily in Red's Config and cleared automatically when a game ends.

User data can be deleted on request via Red's `red_delete_data_for_user` handler.

---

## Notes

- The lobby will not start a game if fewer than 2 players join before the 60-second window expires.
- Turn input is restricted to the current player only — other players' messages in the channel are ignored during a turn.
- The turn embed edits happen every second; occasional edit failures (rate limits, message deletion) are silently handled and won't crash the game.
- The chain prefix rule is biased toward 2-letter prefixes to keep it achievable.

---

*Made by hbicofbiology*
