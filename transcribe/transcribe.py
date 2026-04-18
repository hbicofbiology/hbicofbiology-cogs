import io
import aiohttp
import discord
from redbot.core import commands, Config
from redbot.core.bot import Red

WHISPER_URL = "https://api.openai.com/v1/audio/transcriptions"


class Transcribe(commands.Cog):
    """Automatically transcribe Discord voice messages using OpenAI Whisper."""

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=5647382910, force_registration=True)
        self.config.register_global(api_key=None)
        self.config.register_guild(enabled=False, channels=[])  # empty = all channels

    # -------------------------------------------------------------------------
    # Listener
    # -------------------------------------------------------------------------

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.guild is None or message.author.bot:
            return

        guild_data = await self.config.guild(message.guild).all()
        if not guild_data["enabled"]:
            return

        allowed_channels = guild_data["channels"]
        if allowed_channels and message.channel.id not in allowed_channels:
            return

        # Discord voice messages: audio attachment with the voice message flag
        voice_attachment = next(
            (
                a for a in message.attachments
                if a.content_type and a.content_type.startswith("audio/")
                and getattr(message.flags, "voice", False)
            ),
            None,
        )
        if voice_attachment is None:
            return

        api_key = await self.config.api_key()
        if not api_key:
            return  # silently skip if not configured

        async with message.channel.typing():
            transcription = await self._transcribe(voice_attachment, api_key)

        if transcription is None:
            return

        embed = discord.Embed(
            description=transcription,
            color=discord.Color.blurple(),
        )
        embed.set_author(
            name=message.author.display_name,
            icon_url=message.author.display_avatar.url,
        )
        embed.set_footer(text="Voice message transcription")
        await message.reply(embed=embed, mention_author=False)

    # -------------------------------------------------------------------------
    # Transcription helper
    # -------------------------------------------------------------------------

    async def _transcribe(self, attachment: discord.Attachment, api_key: str) -> str | None:
        async with aiohttp.ClientSession() as session:
            # Download the audio
            async with session.get(attachment.url) as resp:
                if resp.status != 200:
                    return None
                audio_bytes = await resp.read()

            # Determine a sensible filename extension for Whisper
            content_type = attachment.content_type or "audio/ogg"
            ext = content_type.split("/")[-1].split(";")[0].strip()
            filename = f"voice.{ext}"

            form = aiohttp.FormData()
            form.add_field("model", "whisper-1")
            form.add_field(
                "file",
                io.BytesIO(audio_bytes),
                filename=filename,
                content_type=content_type,
            )

            async with session.post(
                WHISPER_URL,
                headers={"Authorization": f"Bearer {api_key}"},
                data=form,
            ) as resp:
                if resp.status != 200:
                    return None
                data = await resp.json()
                return data.get("text")

    # -------------------------------------------------------------------------
    # Admin commands
    # -------------------------------------------------------------------------

    @commands.group()
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def transcribeset(self, ctx: commands.Context):
        """Configure the Transcribe cog."""

    @transcribeset.command(name="apikey")
    @commands.is_owner()
    async def transcribeset_apikey(self, ctx: commands.Context, api_key: str):
        """[Owner] Set the OpenAI API key used for transcription."""
        await self.config.api_key.set(api_key)
        await ctx.message.delete()  # delete the message so the key isn't visible
        await ctx.send("API key saved.", delete_after=5)

    @transcribeset.command(name="enable")
    async def transcribeset_enable(self, ctx: commands.Context):
        """Enable auto-transcription in this server."""
        await self.config.guild(ctx.guild).enabled.set(True)
        await ctx.send("Auto-transcription enabled.")

    @transcribeset.command(name="disable")
    async def transcribeset_disable(self, ctx: commands.Context):
        """Disable auto-transcription in this server."""
        await self.config.guild(ctx.guild).enabled.set(False)
        await ctx.send("Auto-transcription disabled.")

    @transcribeset.command(name="addchannel")
    async def transcribeset_addchannel(self, ctx: commands.Context, channel: discord.TextChannel):
        """Restrict transcription to specific channels. Run with no channels set to allow all."""
        async with self.config.guild(ctx.guild).channels() as channels:
            if channel.id not in channels:
                channels.append(channel.id)
        await ctx.send(f"Transcription enabled in {channel.mention}.")

    @transcribeset.command(name="removechannel")
    async def transcribeset_removechannel(self, ctx: commands.Context, channel: discord.TextChannel):
        """Remove a channel from the transcription allowlist."""
        async with self.config.guild(ctx.guild).channels() as channels:
            if channel.id in channels:
                channels.remove(channel.id)
                await ctx.send(f"{channel.mention} removed from the allowlist.")
            else:
                await ctx.send(f"{channel.mention} wasn't in the allowlist.")

    @transcribeset.command(name="clearchannels")
    async def transcribeset_clearchannels(self, ctx: commands.Context):
        """Clear the channel allowlist so all channels are transcribed."""
        await self.config.guild(ctx.guild).channels.set([])
        await ctx.send("Channel allowlist cleared — all channels will be transcribed.")

    @transcribeset.command(name="status")
    async def transcribeset_status(self, ctx: commands.Context):
        """Show the current transcription settings for this server."""
        data = await self.config.guild(ctx.guild).all()
        api_key = await self.config.api_key()

        channel_list = (
            ", ".join(f"<#{cid}>" for cid in data["channels"]) if data["channels"] else "all channels"
        )
        embed = discord.Embed(title="Transcribe Settings", color=discord.Color.blurple())
        embed.add_field(name="Enabled", value="Yes" if data["enabled"] else "No", inline=True)
        embed.add_field(name="API Key", value="Set" if api_key else "Not set", inline=True)
        embed.add_field(name="Channels", value=channel_list, inline=False)
        await ctx.send(embed=embed)
