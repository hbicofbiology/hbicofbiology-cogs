# 🎰 Casino

A fully-featured casino cog for [Red-DiscordBot V3](https://github.com/Cog-Creators/Red-DiscordBot) with nine playable games, economy integration, per-game configuration, cooldowns, and stat tracking. Inspired by Redjumpman's original Casino cog from Jumper-Plugins.

---

## Features

- Nine casino games with Discord embed output
- Fully integrated with Red's economy (`bank` system)
- Per-game configurable minimums, maximums, multipliers, and cooldowns
- Per-game open/close toggle
- Optional server-wide payout cap
- Per-user win/loss/profit stat tracking
- GDPR-compliant user data deletion support (`red_delete_data_for_user`)

---

## Installation

```
[p]repo add hbicofbiology-cogs https://github.com/hbicofbiology/hbicofbiology-cogs
[p]cog install hbicofbiology-cogs casino
[p]load casino
```

Requires **Red-DiscordBot 3.5.0+**. No additional pip dependencies.

---

## Games

| Command | Aliases | Description |
|---|---|---|
| `[p]coin` | — | Flip a coin — pick heads or tails |
| `[p]cups` | — | Guess which of three cups hides the coin |
| `[p]dice` | — | Roll two dice — win on 2, 7, 11, or 12 |
| `[p]hilo` | `[p]hl` | Pick High (8–12), Low (2–6), or Seven — Seven pays a bonus multiplier |
| `[p]craps` | — | Pass-line craps — natural 7 pays 7x, point-and-roll resolution |
| `[p]blackjack` | `[p]bj`, `[p]21` | Hit, stand, or double down against a dealer who stands on 17 |
| `[p]war` | — | Your card vs the dealer's — ties trigger a War round |
| `[p]allin` | — | Bet your entire balance with a chosen multiplier and matching odds |
| `[p]double` | `[p]don`, `[p]x2` | Interactive double-or-nothing with a 55/45 edge — cash out any time |

### Game Details

**Coin Flip** — `[p]coin <bet> <heads|tails>`
Pick heads or tails (or `h`/`t`). Default multiplier: 1.5x.

**Cups** — `[p]cups <bet> <1|2|3>`
One of three cups hides a coin. Default multiplier: 2.5x (best odds of a single-choice game).

**Dice** — `[p]dice <bet>`
Roll two dice. Winning totals: 2, 7, 11, 12. Default multiplier: 2.0x.

**Hi-Lo** — `[p]hilo <bet> <high|low|seven>`
Two dice are rolled. Pick `high` (8–12), `low` (2–6), or `seven` (7). Seven pays at `multiplier + 2x` for the extra risk.

**Craps** — `[p]craps <bet>`
Come-out roll: 7 pays 7x, 11 wins at the normal multiplier, 2/3/12 is an instant loss. Any other total sets a point — keep rolling until the point comes up (win) or a 7 appears (lose).

**Blackjack** — `[p]blackjack <bet>`
Standard blackjack vs a dealer who stands on 17. Actions: `hit` (`h`), `stand` (`s`), `double` (`d`). A natural blackjack pays 2.5x. Double down is available on the first action only. 60-second input timeout.

**War** — `[p]war <bet>`
Both you and the dealer draw a card. Higher card wins. On a tie, both draw again for a War round — player wins ties in the War round.

**All-In** — `[p]allin <multiplier>`
Wagers your entire current balance. Choose any multiplier ≥ 2; the win chance is 1 in `(multiplier + 1)`. Payout is `balance × multiplier`.

**Double or Nothing** — `[p]double <bet>`
Interactive multi-round game. Each round has a 55% success rate. Type `double` (`d`) to risk it again or `cash` (`c`) to collect. Busting forfeits the entire pot. Auto-cashes out on a 30-second timeout.

---

## User Commands

| Command | Description |
|---|---|
| `[p]casino info` | Show all games with their current settings and status |
| `[p]casino stats [user]` | Show win/loss/profit stats for yourself or another member |
| `[p]casino version` | Display the cog version and author |

---

## Admin Commands

All `casinoset` commands require **Administrator** permission.

| Command | Description |
|---|---|
| `[p]casinoset name <name>` | Set the casino's display name (max 30 characters) |
| `[p]casinoset min <game> <amount>` | Set the minimum bet for a game |
| `[p]casinoset max <game> <amount>` | Set the maximum bet for a game |
| `[p]casinoset multiplier <game> <value>` | Set the payout multiplier for a game (minimum 1.0) |
| `[p]casinoset cooldown <game> <seconds>` | Set the per-user cooldown for a game |
| `[p]casinoset toggle <game>` | Open or close a game |
| `[p]casinoset payoutlimit <amount>` | Set a server-wide payout cap (0 to disable) |
| `[p]casinoset resetuser <@user>` | Reset a specific user's stats and cooldowns |
| `[p]casinoset reset` | Reset all casino settings to defaults (user data is preserved) |
| `[p]casinoset wipe` | ⚠️ Bot owner only — wipe all casino data for this server |

Game names are case-insensitive for `casinoset` subcommands: `blackjack`, `coin`, `cups`, `dice`, `hilo`, `craps`, `war`, `allin`, `double`.

---

## Default Game Settings

| Game | Min | Max | Multiplier | Cooldown |
|---|---|---|---|---|
| Coin | 50 | 10,000 | 1.5x | 5s |
| Cups | 50 | 10,000 | 2.5x | 5s |
| Dice | 50 | 10,000 | 2.0x | 5s |
| Hi-Lo | 50 | 10,000 | 2.0x | 5s |
| Craps | 50 | 10,000 | 2.0x | 5s |
| Blackjack | 50 | 10,000 | 2.0x | 5s |
| War | 50 | 10,000 | 2.0x | 5s |
| All-In | — | — | 2.0x | 30s |
| Double | 50 | 10,000 | 2.0x | 5s |

---

## Data Storage

This cog stores the following data per user per server:

- Discord user ID
- Game statistics: wins, losses, total wagered, total won
- Per-game cooldown timestamps

User data can be deleted on request via Red's `red_delete_data_for_user` handler.

---

## Credits

Original concept by **Redjumpman** ([Jumper-Plugins](https://github.com/redjumpman/Jumper-Plugins)).
Recreation and modernisation for Red V3 by **hbicofbiology**.
