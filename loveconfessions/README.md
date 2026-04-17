# 💌 LoveConfessions

A simple confession cog for [Red-DiscordBot V3](https://github.com/Cog-Creators/Red-DiscordBot). Send sweet (or spicy) messages to other users — either publicly with your name attached, or completely anonymously via a Discord modal UI.

---

## Features

- **Public confessions** — DMs the target with your display name in the footer
- **Anonymous confessions** — modal-based UI; the recipient has no idea who sent it
- Command messages are automatically deleted to keep things discreet
- No external dependencies, no data stored

---

## Installation

```
[p]repo add hbicofbiology-cogs https://github.com/hbicofbiology/hbicofbiology-cogs
[p]cog install hbicofbiology-cogs loveconfessions
[p]load loveconfessions
```

Requires **Red-DiscordBot 3.5.0+**. No additional pip dependencies.

---

## Commands

| Command | Description |
|---|---|
| `[p]confess <@user> <message>` | Send a public confession — recipient is DM'd with your display name |
| `[p]confessanon` | Open an anonymous confession modal — enter a User ID and your message |

### Usage

**Public confession:**
```
[p]confess @Alex you make every lab meeting better
```
The command message is deleted. Alex receives a DM embed with your display name in the footer.

**Anonymous confession:**
```
[p]confessanon
```
A button appears (visible for 60 seconds). Click **💌 Confess Anonymously**, fill in the target's User ID and your message, and submit. The recipient gets a DM with no sender information. All responses are ephemeral.

---

## Notes

- Both commands require the target user to have DMs open. If DMs are closed, the bot will respond with an error (ephemeral / auto-deleting).
- The anonymous modal requires the sender to know the target's **User ID** (not username). Users can find this via Developer Mode → right-click → Copy User ID.
- The `[p]confessanon` button expires after **60 seconds**.
- No message content is stored — confessions are sent directly and not logged anywhere.

---

*Made by hbicofbiology*
