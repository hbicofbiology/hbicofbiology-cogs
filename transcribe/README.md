# 🎙️ Transcribe

A utility cog for [Red-DiscordBot V3](https://github.com/Cog-Creators/Red-DiscordBot) that automatically transcribes Discord voice messages using the [OpenAI Whisper API](https://platform.openai.com/docs/guides/speech-to-text). When a member sends a voice message, the bot replies with a clean embed showing the transcription — no commands required from users.

---

## Features

- **Fully passive** — triggers automatically on voice messages, no user interaction needed
- **OpenAI Whisper** — accurate transcription supporting a wide range of languages
- **Per-server toggle** — enable or disable transcription independently on each server
- **Channel restrictions** — optionally limit transcription to specific channels
- **Clean embed output** — reply includes the sender's name, avatar, and transcribed text
- **No data stored** — audio is sent directly to the Whisper API and nothing is retained

---

## Installation

```
[p]repo add <your-repo-name> <your-github-url>
[p]cog install <your-repo-name> transcribe
[p]load transcribe
```

Requires **Red-DiscordBot 3.5.0+** and `aiohttp` (usually already present in Red).

---

## Setup

**1. Get an OpenAI API key**

Sign up at [platform.openai.com](https://platform.openai.com) and create an API key. Whisper usage is billed per minute of audio — check [OpenAI's pricing](https://openai.com/pricing) for current rates.

**2. Set the API key (bot owner only)**

```
[p]transcribeset apikey sk-...
```

The bot immediately deletes your message to protect the key. Run this in a private channel just in case.

**3. Enable transcription on your server**

```
[p]transcribeset enable
```

That's it — the bot will now reply to any voice message in the server with a transcription.

---

## Admin Commands

All commands require **Administrator** or **Manage Guild** permission unless noted.

| Command | Description |
|---|---|
| `[p]transcribeset enable` | Enable auto-transcription in this server |
| `[p]transcribeset disable` | Disable auto-transcription in this server |
| `[p]transcribeset status` | Show current settings (enabled state, API key status, channels) |
| `[p]transcribeset addchannel <#channel>` | Restrict transcription to a specific channel |
| `[p]transcribeset removechannel <#channel>` | Remove a channel from the allowlist |
| `[p]transcribeset clearchannels` | Clear all restrictions — transcribe in all channels |
| `[p]transcribeset apikey <key>` | *(Owner only)* Set the OpenAI API key |

If no channels are added to the allowlist, all channels in the server are transcribed.

---

## Notes

- Only Discord **voice messages** are transcribed — regular audio file attachments are ignored. Voice messages are the ones recorded in-app with the microphone button.
- If the API key is not set, voice messages are silently ignored — no error is shown to users.
- The API key is stored globally per bot instance — each person who installs this cog sets their own key and is billed on their own OpenAI account. Red stores it in plaintext in its Config JSON, so keep your bot's data directory private.
- Audio is sent to OpenAI's servers for processing. Do not use this in servers where voice message content is sensitive.

---

## Data Storage

No user data is stored. The only persistent data is the OpenAI API key (global) and per-server settings (enabled state, channel list).

---

*Made by Bio.*
