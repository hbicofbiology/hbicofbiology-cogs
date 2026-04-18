# 🤫 Confessions

An anonymous confession cog for [Red-DiscordBot V3](https://github.com/Cog-Creators/Red-DiscordBot). Members submit confessions via a Discord modal — triggered by a slash command or a persistent button panel. Confessions are posted as numbered embeds to a configured channel. No identity is ever stored or logged.

---

## Features

- **Fully anonymous** — no user IDs, names, or metadata are stored or logged anywhere
- **Two submission methods** — `/confess` slash command or a persistent button panel
- **Persistent button** — the panel survives bot restarts, no re-posting needed
- **Numbered confessions** — each post is labelled `Anonymous Confession #n`
- **Per-server toggle** — enable or disable submissions without removing the panel
- **Configurable output channel** — post the panel anywhere, confessions go somewhere else
- No external dependencies

---

## Installation

```
[p]repo add hbicofbiology-cogs https://github.com/hbicofbiology/hbicofbiology-cogs
[p]cog install hbicofbiology-cogs confessions
[p]load confessions
```

Requires **Red-DiscordBot 3.5.0+** and **Python 3.8+**. No additional pip dependencies.

---

## Setup

**1. Set the confession output channel**
```
[p]confessions setchannel #confessions
```

**2. Post a button panel wherever you want members to submit from**
```
[p]confessions postpanel #general
```

That's it. Members can now click the button or use `/confess` — a modal pops up, they type their confession, and it appears in the configured channel.

---

## How It Works

1. Member clicks **📝 Submit a Confession** or runs `/confess`
2. A Discord modal appears — they type their confession (10–1000 characters)
3. On submit, the confession is posted as a numbered embed to the confession channel
4. The member gets an ephemeral confirmation — no one else sees that they submitted

---

## User Commands

| Command | Description |
|---|---|
| `/confess` | Open the confession modal (slash command) |

The button panel works the same way — no command needed once it's posted.

---

## Admin Commands

All commands require **Administrator** or **Manage Guild** permission.

| Command | Description |
|---|---|
| `[p]confessions setchannel <#channel>` | Set the channel where confessions are posted |
| `[p]confessions unsetchannel` | Clear the confession channel — pauses submissions |
| `[p]confessions enable` | Enable the confession system |
| `[p]confessions disable` | Disable the confession system — button and slash command show a message instead |
| `[p]confessions postpanel [#channel]` | Post a button panel — defaults to the current channel |
| `[p]confessions resetcount` | Reset the confession counter back to 0 |
| `[p]confessions status` | Show current configuration (enabled state, channel, total count) |

---

## Notes

- The bot needs **Send Messages** and **Embed Links** permissions in the confession channel.
- If the confession channel is deleted or unset, the button and slash command will notify the user instead of erroring silently.
- The button panel can be posted in a different channel from where confessions appear — common setup is panel in `#general`, confessions in `#confession-box`.

---

## Data Storage

No user data is stored. Per server: confession channel ID, enabled state, and confession count. Confession text is never retained after posting.

---

*Made by hbicofbiology.*
