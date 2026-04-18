# 🎵 MoodMusic

A curated mood-based music recommendation cog for [Red-DiscordBot V3](https://github.com/Cog-Creators/Red-DiscordBot). Admins build per-mood Spotify song libraries; users request a random track for any mood and receive a rich Discord embed with album art, track title, artist, and a direct Spotify link.

---

## Features

- **Mood-based playlists** — admins create and manage named mood categories (e.g. `happy`, `chill`, `focus`)
- **Random track picks** — users get a random song from any mood on demand
- **Rich Spotify embeds** — album art, track title, artist, and clickable Spotify link (requires API credentials)
- **Duplicate detection** — prevents the same track being added to a mood twice
- **Metadata refresh** — re-fetch album art and track info for all stored tracks
- **No rich embeds? No problem** — works without Spotify credentials, just without album art

---

## Installation

```
[p]repo add hbicofbiology-cogs https://github.com/hbicofbiology/hbicofbiology-cogs
[p]cog install hbicofbiology-cogs moodmusic
[p]load moodmusic
```

Then set your Spotify credentials for full embed support:
```
[p]moodmusic setcreds <client_id> <client_secret>
```

Requires **Red-DiscordBot 3.5.0+** and the `aiohttp` pip package (usually already present in Red).

---

## Spotify API Setup

Rich embeds (album art, track title, artist) require a free Spotify API app:

1. Go to [developer.spotify.com/dashboard](https://developer.spotify.com/dashboard)
2. Create an app — name and description can be anything
3. Copy your **Client ID** and **Client Secret**
4. Run `[p]moodmusic setcreds <client_id> <client_secret>` in a **private channel**

> ⚠️ The bot automatically deletes your `setcreds` message to protect your credentials. Still, run it somewhere private just in case.

The cog works without credentials — tracks will still be recommended, just without album art or track metadata in the embed.

---

## User Commands

| Command | Description |
|---|---|
| `[p]moodmusic <mood>` | Get a random song recommendation for a mood |
| `[p]moodmusic moods` | List all available mood categories and their song counts |
| `[p]moodmusic list <mood>` | List all songs in a mood category with titles and artists |

### Example

```
[p]moodmusic chill
[p]moodmusic moods
[p]moodmusic list focus
```

---

## Admin Commands

Require **Administrator** or **Manage Guild** permission.

| Command | Description |
|---|---|
| `[p]moodmusic add <mood> <spotify_url>` | Add a Spotify track to a mood — creates the mood if it doesn't exist |
| `[p]moodmusic remove <mood> <spotify_url>` | Remove a track from a mood by URL |
| `[p]moodmusic removenum <mood> <number>` | Remove a track by its position in `[p]moodmusic list` |
| `[p]moodmusic deletemood <mood>` | Delete an entire mood category and all its songs |
| `[p]moodmusic setcreds <client_id> <client_secret>` | Set Spotify API credentials for rich embeds |
| `[p]moodmusic refresh [mood]` | Re-fetch Spotify metadata for all tracks, or just one mood |

### Adding tracks

```
[p]moodmusic add happy https://open.spotify.com/track/4uLU6hMCjMI75M1A2tKUQC
```

Mood names are case-insensitive. If Spotify credentials are set, the embed will immediately preview the added track with album art.

---

## Data Storage

The following is stored per server:

- Mood category names and their track lists (URL, track ID, title, artist, album, album art URL)
- Spotify API credentials (client ID and client secret)

No user data is stored.

---

*Made by hbicofbiology*
