# 💍 Marriage

A relationship and social cog for [Red-DiscordBot V3](https://github.com/Cog-Creators/Red-DiscordBot). Marry other members, track contentment, send gifts, perform actions, confess your feelings, and keep tabs on your exes. Supports optional multi-spouse mode and full admin customization of gifts and actions.

---

## Features

- **Marriage system** — propose, accept, and divorce with economy costs
- **Contentment bar** — a ❤️ meter per user that rises with gifts and actions
- **Gifts** — send items to boost someone's contentment, costs currency
- **Actions** — perform emote-style interactions; some require consent
- **Profile system** — view marriage status, spouses, exes, contentment, and gifts received
- **Optional multi-spouse mode** — admins can allow polygamous marriages
- **Fully customizable** — add/remove custom gifts and actions per server
- Integrates with Red's economy (`bank`)

---

## Installation

```
[p]repo add hbicofbiology-cogs https://github.com/hbicofbiology/hbicofbiology-cogs
[p]cog install hbicofbiology-cogs marriage
[p]load marriage
```

Requires **Red-DiscordBot 3.5.0+**. No additional pip dependencies.

---

## Commands

### Marriage

| Command | Description |
|---|---|
| `[p]marry <@user>` | Propose to someone — they must accept within 60 seconds. Both parties pay the marriage price |
| `[p]divorce <@user>` | Divorce a spouse — costs the marriage price × divorce multiplier |
| `[p]about [user]` | View a user's full marriage profile (status, spouses, exes, contentment, gifts) |
| `[p]spouses [user]` | View a user's current spouses and their contentment |
| `[p]exes [user]` | View a user's ex list |

### Gifts

| Command | Description |
|---|---|
| `[p]gift` | Show all available gifts |
| `[p]gift <@user> <gift>` | Send a gift to someone — costs currency, boosts their contentment |

**Default gifts:**

| Gift | Contentment | Cost |
|---|---|---|
| 🌸 Flower | +5 | 10 |
| 🍫 Chocolate | +8 | 15 |
| 💍 Ring | +20 | 250 |
| 🐶 Puppy | +30 | 500 |
| 🏰 Castle | +60 | 10,000 |

### Actions

| Command | Description |
|---|---|
| `[p]perform <action> <@user>` | Perform an action on someone — some require their consent |

**Default actions:**

| Action | Contentment | Consent Required |
|---|---|---|
| 😏 flirt | +5 | No |
| 💋 kiss | +10 | Yes |

---

## Admin Commands

All `marryset` commands are **bot owner only**.

### General Settings

| Command | Description |
|---|---|
| `[p]marryset` | Show the settings group |

> Note: enable/disable, multi-spouse toggle, and price configuration subcommands are available — check `[p]help marryset` for the full list.

### Custom Gifts

| Command | Description |
|---|---|
| `[p]marryset gifts add <name> <contentment> <price> [emoji]` | Add a custom gift |
| `[p]marryset gifts remove <name>` | Remove a custom gift |
| `[p]marryset gifts list` | List all custom gifts |

### Custom Actions

| Command | Description |
|---|---|
| `[p]marryset actions add <name> <contentment> <price> <require_consent> <description> [%% <consent_prompt>]` | Add a custom action |
| `[p]marryset actions remove <name>` | Remove a custom action |
| `[p]marryset actions list` | List all custom actions |

For actions that require consent, separate the action description and the consent prompt with `%%`:
```
[p]marryset actions add hug 8 0 True {author} hugs {target} warmly. %% {author} wants to hug you! Do you accept?
```
Use `{author}` and `{target}` as placeholders in descriptions — they are replaced with member mentions at runtime.

---

## Default Settings

| Setting | Default |
|---|---|
| Marriage enabled | ✅ Yes |
| Multi-spouse mode | ❌ No |
| Marriage price | 1,500 credits |
| Divorce multiplier | 2x (costs `price × 2`) |

---

## Data Storage

The following is stored per user per server:

- Marriage status, current spouses, and ex list
- Contentment value (0–100)
- Marriage and divorce counts
- Crush (stored but not currently displayed separately from profile)
- Gifts received and their quantities

---

*Made by hbicofbiology*
