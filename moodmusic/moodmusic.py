import discord
import random
import re
import aiohttp

from redbot.core import commands, Config, checks
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import box, pagify

SPOTIFY_TRACK_PATTERN = re.compile(
    r"https?://open\.spotify\.com/track/([A-Za-z0-9]+)"
)

# Colour used for embeds (Spotify green)
SPOTIFY_GREEN = 0x1DB954


class MoodMusic(commands.Cog):
    """
    Curated mood-based Spotify music recommendations.

    Admins build per-mood song libraries; users request a random track
    for any mood and get a rich Discord embed with album art, title,
    artist, and a direct Spotify link.
    """

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=0x4D6F6F64,   # "Mood" in hex — unique cog identifier
            force_registration=True,
        )
        # Guild-level defaults
        self.config.register_guild(
            moods={},               # { mood_name: [ {url, track_id, title, artist, album, art_url}, ... ] }
            spotify_client_id=None,
            spotify_client_secret=None,
        )
        self._spotify_token: dict = {}   # cache: {token, expires_at}

    # ------------------------------------------------------------------ #
    #  Spotify API helpers                                                 #
    # ------------------------------------------------------------------ #

    async def _get_spotify_token(self, guild: discord.Guild) -> str | None:
        """Fetch (or return cached) a Spotify client-credentials token."""
        import time

        client_id = await self.config.guild(guild).spotify_client_id()
        client_secret = await self.config.guild(guild).spotify_client_secret()
        if not client_id or not client_secret:
            return None

        cache_key = f"{guild.id}"
        cached = self._spotify_token.get(cache_key)
        if cached and cached["expires_at"] > time.time() + 60:
            return cached["token"]

        auth_url = "https://accounts.spotify.com/api/token"
        async with aiohttp.ClientSession() as session:
            async with session.post(
                auth_url,
                data={"grant_type": "client_credentials"},
                auth=aiohttp.BasicAuth(client_id, client_secret),
            ) as resp:
                if resp.status != 200:
                    return None
                data = await resp.json()

        token = data.get("access_token")
        expires_in = data.get("expires_in", 3600)
        self._spotify_token[cache_key] = {
            "token": token,
            "expires_at": time.time() + expires_in,
        }
        return token

    async def _fetch_track_info(
        self, guild: discord.Guild, track_id: str
    ) -> dict | None:
        """Return a dict with title, artist, album, art_url for a track ID."""
        token = await self._get_spotify_token(guild)
        if not token:
            return None

        url = f"https://api.spotify.com/v1/tracks/{track_id}"
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url, headers={"Authorization": f"Bearer {token}"}
            ) as resp:
                if resp.status != 200:
                    return None
                data = await resp.json()

        images = data.get("album", {}).get("images", [])
        art_url = images[0]["url"] if images else None
        artists = ", ".join(a["name"] for a in data.get("artists", []))

        return {
            "title": data.get("name", "Unknown Title"),
            "artist": artists or "Unknown Artist",
            "album": data.get("album", {}).get("name", "Unknown Album"),
            "art_url": art_url,
            "preview_url": data.get("preview_url"),
        }

    # ------------------------------------------------------------------ #
    #  Embed builder                                                       #
    # ------------------------------------------------------------------ #

    def _build_embed(self, track: dict, mood: str) -> discord.Embed:
        embed = discord.Embed(
            title=track.get("title", "Unknown Title"),
            url=track["url"],
            description=f"**{track.get('artist', 'Unknown Artist')}**\n*{track.get('album', '')}*",
            color=SPOTIFY_GREEN,
        )
        embed.set_author(
            name=f"🎵 Mood Music — {mood.title()}",
            icon_url="https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_RGB_Green.png",
        )
        if track.get("art_url"):
            embed.set_thumbnail(url=track["art_url"])
        embed.set_footer(text="Open in Spotify ↗")
        return embed

    # ------------------------------------------------------------------ #
    #  Top-level command group                                             #
    # ------------------------------------------------------------------ #

    @commands.group(invoke_without_command=True)
    @commands.guild_only()
    async def moodmusic(self, ctx: commands.Context, *, mood: str = None):
        """
        Get a song recommendation for a mood.

        **Usage:** `[p]moodmusic <mood>`
        **Example:** `[p]moodmusic happy`

        Use `[p]moodmusic moods` to see all available moods.
        """
        if mood is None:
            await ctx.send_help()
            return

        mood = mood.lower().strip()
        moods = await self.config.guild(ctx.guild).moods()

        if mood not in moods or not moods[mood]:
            available = ", ".join(f"`{m}`" for m in sorted(moods)) or "*(none yet)*"
            await ctx.send(
                f"❌ No songs found for mood **{mood}**.\n"
                f"Available moods: {available}"
            )
            return

        track = random.choice(moods[mood])
        embed = self._build_embed(track, mood)
        await ctx.send(embed=embed)

    # ------------------------------------------------------------------ #
    #  User commands                                                       #
    # ------------------------------------------------------------------ #

    @moodmusic.command(name="moods")
    @commands.guild_only()
    async def moodmusic_moods(self, ctx: commands.Context):
        """List all available mood categories and their song counts."""
        moods = await self.config.guild(ctx.guild).moods()
        if not moods:
            await ctx.send("No mood categories have been set up yet.")
            return

        lines = [
            f"**{m.title()}** — {len(songs)} song{'s' if len(songs) != 1 else ''}"
            for m, songs in sorted(moods.items())
        ]
        embed = discord.Embed(
            title="🎶 Available Moods",
            description="\n".join(lines),
            color=SPOTIFY_GREEN,
        )
        await ctx.send(embed=embed)

    @moodmusic.command(name="list")
    @commands.guild_only()
    async def moodmusic_list(self, ctx: commands.Context, *, mood: str):
        """
        List all songs in a mood category.

        **Usage:** `[p]moodmusic list <mood>`
        """
        mood = mood.lower().strip()
        moods = await self.config.guild(ctx.guild).moods()

        if mood not in moods or not moods[mood]:
            await ctx.send(f"❌ No songs found for mood **{mood}**.")
            return

        lines = []
        for i, track in enumerate(moods[mood], 1):
            title = track.get("title", "Unknown")
            artist = track.get("artist", "Unknown")
            lines.append(f"`{i}.` [{title} — {artist}]({track['url']})")

        embed = discord.Embed(
            title=f"🎵 {mood.title()} — Song List",
            description="\n".join(lines),
            color=SPOTIFY_GREEN,
        )
        embed.set_footer(text=f"{len(lines)} song{'s' if len(lines) != 1 else ''}")
        await ctx.send(embed=embed)

    # ------------------------------------------------------------------ #
    #  Admin commands                                                      #
    # ------------------------------------------------------------------ #

    @moodmusic.command(name="add")
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    async def moodmusic_add(
        self, ctx: commands.Context, mood: str, *, spotify_url: str
    ):
        """
        Add a Spotify track to a mood category.

        **Usage:** `[p]moodmusic add <mood> <spotify_url>`
        **Example:** `[p]moodmusic add happy https://open.spotify.com/track/...`

        Creates the mood category automatically if it doesn't exist.
        Spotify API credentials must be set for rich embeds — see `[p]moodmusic setcreds`.
        """
        mood = mood.lower().strip()

        match = SPOTIFY_TRACK_PATTERN.search(spotify_url)
        if not match:
            await ctx.send(
                "❌ That doesn't look like a valid Spotify track URL.\n"
                "Expected format: `https://open.spotify.com/track/TRACK_ID`"
            )
            return

        track_id = match.group(1)
        clean_url = f"https://open.spotify.com/track/{track_id}"

        async with self.config.guild(ctx.guild).moods() as moods:
            if mood not in moods:
                moods[mood] = []

            # Duplicate check
            existing_ids = {t["track_id"] for t in moods[mood]}
            if track_id in existing_ids:
                await ctx.send(
                    f"⚠️ That track is already in the **{mood}** playlist."
                )
                return

            # Try to fetch Spotify metadata for the rich entry
            async with ctx.typing():
                info = await self._fetch_track_info(ctx.guild, track_id)

            entry = {"url": clean_url, "track_id": track_id}
            if info:
                entry.update(info)

            moods[mood].append(entry)

        if info:
            embed = discord.Embed(
                title="✅ Track Added",
                description=(
                    f"**{info['title']}** by {info['artist']}\n"
                    f"Added to **{mood.title()}**"
                ),
                color=SPOTIFY_GREEN,
            )
            if info.get("art_url"):
                embed.set_thumbnail(url=info["art_url"])
            await ctx.send(embed=embed)
        else:
            await ctx.send(
                f"✅ Track added to **{mood.title()}**.\n"
                f"*(Set Spotify API credentials with `{ctx.clean_prefix}moodmusic setcreds` "
                f"for rich embeds with album art.)*"
            )

    @moodmusic.command(name="remove")
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    async def moodmusic_remove(
        self, ctx: commands.Context, mood: str, *, spotify_url: str
    ):
        """
        Remove a Spotify track from a mood category.

        **Usage:** `[p]moodmusic remove <mood> <spotify_url>`

        You can also use `[p]moodmusic removenum <mood> <number>` to remove by list position.
        """
        mood = mood.lower().strip()
        match = SPOTIFY_TRACK_PATTERN.search(spotify_url)
        if not match:
            await ctx.send("❌ That doesn't look like a valid Spotify track URL.")
            return

        track_id = match.group(1)

        async with self.config.guild(ctx.guild).moods() as moods:
            if mood not in moods:
                await ctx.send(f"❌ No mood category named **{mood}** exists.")
                return

            original_len = len(moods[mood])
            moods[mood] = [t for t in moods[mood] if t["track_id"] != track_id]

            if len(moods[mood]) == original_len:
                await ctx.send(f"❌ That track wasn't found in **{mood}**.")
                return

        await ctx.send(f"✅ Track removed from **{mood.title()}**.")

    @moodmusic.command(name="removenum")
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    async def moodmusic_removenum(
        self, ctx: commands.Context, mood: str, number: int
    ):
        """
        Remove a track from a mood by its list number.

        **Usage:** `[p]moodmusic removenum <mood> <number>`

        Use `[p]moodmusic list <mood>` to see the numbers.
        """
        mood = mood.lower().strip()

        async with self.config.guild(ctx.guild).moods() as moods:
            if mood not in moods or not moods[mood]:
                await ctx.send(f"❌ No songs found for mood **{mood}**.")
                return

            if number < 1 or number > len(moods[mood]):
                await ctx.send(
                    f"❌ Invalid number. Choose between 1 and {len(moods[mood])}."
                )
                return

            removed = moods[mood].pop(number - 1)

        title = removed.get("title", removed["url"])
        artist = removed.get("artist", "")
        label = f"**{title}**" + (f" by {artist}" if artist else "")
        await ctx.send(f"✅ Removed {label} from **{mood.title()}**.")

    @moodmusic.command(name="deletemood")
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    async def moodmusic_deletemood(self, ctx: commands.Context, *, mood: str):
        """
        Delete an entire mood category and all its songs.

        **Usage:** `[p]moodmusic deletemood <mood>`
        """
        mood = mood.lower().strip()

        async with self.config.guild(ctx.guild).moods() as moods:
            if mood not in moods:
                await ctx.send(f"❌ No mood category named **{mood}** exists.")
                return
            count = len(moods.pop(mood))

        await ctx.send(
            f"🗑️ Deleted mood **{mood.title()}** and its {count} song{'s' if count != 1 else ''}."
        )

    @moodmusic.command(name="setcreds")
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    async def moodmusic_setcreds(
        self, ctx: commands.Context, client_id: str, client_secret: str
    ):
        """
        Set your Spotify API credentials for rich embed support.

        **Usage:** `[p]moodmusic setcreds <client_id> <client_secret>`

        Get credentials at: https://developer.spotify.com/dashboard
        Create an app, then copy the Client ID and Client Secret.

        ⚠️ Run this command in a private channel — your secrets will be visible!
        """
        await self.config.guild(ctx.guild).spotify_client_id.set(client_id)
        await self.config.guild(ctx.guild).spotify_client_secret.set(client_secret)
        # Clear token cache for this guild
        self._spotify_token.pop(str(ctx.guild.id), None)

        try:
            await ctx.message.delete()
        except discord.Forbidden:
            pass

        await ctx.send(
            "✅ Spotify credentials saved. Album art and track info will now appear in embeds.\n"
            "*(Your message was deleted to protect your credentials.)*"
        )

    @moodmusic.command(name="refresh")
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    async def moodmusic_refresh(self, ctx: commands.Context, *, mood: str = None):
        """
        Re-fetch Spotify metadata for all tracks (updates art, titles, artists).

        **Usage:**
        - `[p]moodmusic refresh` — refresh all moods
        - `[p]moodmusic refresh <mood>` — refresh one mood
        """
        moods = await self.config.guild(ctx.guild).moods()

        if mood:
            mood = mood.lower().strip()
            if mood not in moods:
                await ctx.send(f"❌ No mood category named **{mood}** exists.")
                return
            target_moods = {mood: moods[mood]}
        else:
            target_moods = moods

        msg = await ctx.send("🔄 Refreshing Spotify metadata...")
        updated = 0
        failed = 0

        async with self.config.guild(ctx.guild).moods() as live_moods:
            for m, tracks in target_moods.items():
                for i, track in enumerate(tracks):
                    info = await self._fetch_track_info(ctx.guild, track["track_id"])
                    if info:
                        live_moods[m][i].update(info)
                        updated += 1
                    else:
                        failed += 1

        status = f"✅ Refreshed metadata for **{updated}** track{'s' if updated != 1 else ''}."
        if failed:
            status += f"\n⚠️ Could not fetch info for **{failed}** track(s) (check credentials)."
        await msg.edit(content=status)
