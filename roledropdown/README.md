# 🎭 RoleDropdown

A utility cog for [Red-DiscordBot V3](https://github.com/Cog-Creators/Red-DiscordBot) that lets admins post persistent Discord select-menu dropdowns for self-assignable roles. Members pick their roles from a dropdown — no commands needed. Changes apply instantly and are shown only to the user who interacted.

---

## Features

- **Persistent dropdowns** — views are re-registered on bot restart, no re-posting needed
- **Multi-select** — members can pick multiple roles at once from a single dropdown
- **Instant role sync** — selecting or deselecting an option adds or removes the role immediately
- **Custom labels, descriptions, and emojis** per role option
- **Up to 25 roles** per dropdown (Discord limit)
- **Multiple dropdowns** — create as many as you need across different channels
- No external dependencies

---

## Installation

```
[p]repo add hbicofbiology-cogs https://github.com/hbicofbiology/hbicofbiology-cogs
[p]cog install hbicofbiology-cogs roledropdown
[p]load roledropdown
```

Requires **Red-DiscordBot 3.5.0+**. No additional pip dependencies.

---

## Quick Start

```
[p]roledropdown create #roles Pick your roles!
```

This posts a dropdown message in `#roles`. Copy the message ID from the response, then add roles to it:

```
[p]roledropdown add <message_id> @Gamer
[p]roledropdown add <message_id> @Artist "I make art" 🎨
[p]roledropdown add <message_id> @Musician Musician "I play music" 🎵
```

The dropdown updates live as you add roles — no need to re-post it.

---

## Commands

All commands require **Administrator** or **Manage Roles** permission.

| Command | Description |
|---|---|
| `[p]roledropdown create <#channel> [title]` | Post a new dropdown in a channel |
| `[p]roledropdown add <message_id> <@role> [label] [description] [emoji]` | Add a role to a dropdown |
| `[p]roledropdown remove <message_id> <@role>` | Remove a role from a dropdown |
| `[p]roledropdown delete <message_id>` | Delete the dropdown message and remove it from config |
| `[p]roledropdown list` | List all dropdowns in this server |

### Adding roles — argument details

```
[p]roledropdown add <message_id> @Role [label] [description] [emoji]
```

- **label** — display name in the dropdown (defaults to the role name)
- **description** — optional short line shown under the label
- **emoji** — optional emoji shown next to the label (e.g. `🎮`)

All three are optional. Examples:

```
[p]roledropdown add 1234567890 @Gamer
[p]roledropdown add 1234567890 @Artist Artist "I make art" 🎨
```

---

## Notes

- The bot needs **Manage Roles** permission and must be higher in the role hierarchy than any role it assigns.
- Dropdowns support a maximum of **25 options** (Discord limit).
- Role changes are ephemeral — only the user who interacted sees the confirmation message.
- If a dropdown message is manually deleted from Discord, remove it from config with `[p]roledropdown delete <message_id>` to keep things clean.

---

## Data Storage

Per server: dropdown message IDs, channel IDs, titles, placeholder text, and role configurations (ID, label, description, emoji). No user data is stored.

---

*Made by hbicofbiology*
