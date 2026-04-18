import discord
from discord import app_commands
from redbot.core import commands, Config, checks
from redbot.core.bot import Red
import asyncio


# ──────────────────────────────────────────────
#  Persistent Button View
# ──────────────────────────────────────────────

class ConfessButtonView(discord.ui.View):
    """Persistent view — survives bot restarts via custom_id."""

    def __init__(self):
        super().__init__(timeout=None)  # persistent

    @discord.ui.button(
        label="📝  Submit a Confession",
        style=discord.ButtonStyle.primary,
        custom_id="confessions:open_modal",
    )
    async def open_modal(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.guild is None:
            await interaction.response.send_message(
                "This can only be used in a server.", ephemeral=True
            )
            return

        cog: "Confessions" = interaction.client.get_cog("Confessions")
        if cog is None:
            await interaction.response.send_message(
                "The confession system is currently unavailable.", ephemeral=True
            )
            return

        enabled = await cog.config.guild(interaction.guild).enabled()
        if not enabled:
            await interaction.response.send_message(
                "The confession system is currently disabled.", ephemeral=True
            )
            return

        channel_id = await cog.config.guild(interaction.guild).confession_channel()
        if not channel_id:
            await interaction.response.send_message(
                "⚠️ No confession channel has been configured yet.", ephemeral=True
            )
            return

        await interaction.response.send_modal(ConfessionModal(cog, interaction.guild))


# ──────────────────────────────────────────────
#  Modal
# ──────────────────────────────────────────────

class ConfessionModal(discord.ui.Modal, title="Anonymous Confession"):
    confession = discord.ui.TextInput(
        label="Your confession",
        style=discord.TextStyle.paragraph,
        placeholder="Type your confession here… it will be posted anonymously.",
        min_length=10,
        max_length=1000,
        required=True,
    )

    def __init__(self, cog: "Confessions", guild: discord.Guild):
        super().__init__()
        self.cog = cog
        self.guild = guild

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        channel_id = await self.cog.config.guild(self.guild).confession_channel()
        if not channel_id:
            await interaction.followup.send(
                "⚠️ No confession channel has been set up yet. Ask an admin to run `[p]confessions setchannel`.",
                ephemeral=True,
            )
            return

        channel = self.guild.get_channel(channel_id)
        if channel is None:
            await interaction.followup.send(
                "⚠️ The configured confession channel no longer exists. Ask an admin to reconfigure it.",
                ephemeral=True,
            )
            return

        async with self.cog.config.guild(self.guild).confession_count() as count:
            count += 1
            number = count

        embed = discord.Embed(
            description=self.confession.value,
            color=discord.Color.from_str("#5865F2"),
        )
        embed.set_author(name=f"Anonymous Confession #{number}")
        embed.set_footer(text="Click the button in #confessions to submit your own.")

        try:
            await channel.send(embed=embed)
        except discord.Forbidden:
            await interaction.followup.send(
                "⚠️ I don't have permission to post in the confession channel.",
                ephemeral=True,
            )
            return

        await interaction.followup.send(
            "✅ Your confession was posted anonymously. Your identity is never stored.",
            ephemeral=True,
        )

    async def on_error(self, interaction: discord.Interaction, error: Exception):
        await interaction.response.send_message(
            "Something went wrong submitting your confession. Please try again.",
            ephemeral=True,
        )
        raise error


# ──────────────────────────────────────────────
#  Cog
# ──────────────────────────────────────────────

class Confessions(commands.Cog):
    """Anonymous confession system using Discord modals."""

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=0xC0FFEE_C0FE55,
            force_registration=True,
        )
        self.config.register_guild(
            confession_channel=None,
            confession_count=0,
            enabled=True,
        )
        # Register persistent view so button works after restarts
        self.bot.add_view(ConfessButtonView())

    # ── Slash command: /confess ──────────────────

    @app_commands.command(name="confess", description="Submit an anonymous confession.")
    async def confess(self, interaction: discord.Interaction):
        """Opens a modal for anonymous confession submission."""
        if interaction.guild is None:
            await interaction.response.send_message(
                "This command can only be used in a server.", ephemeral=True
            )
            return

        enabled = await self.config.guild(interaction.guild).enabled()
        if not enabled:
            await interaction.response.send_message(
                "The confession system is currently disabled.", ephemeral=True
            )
            return

        channel_id = await self.config.guild(interaction.guild).confession_channel()
        if not channel_id:
            await interaction.response.send_message(
                "⚠️ No confession channel has been configured yet. Ask an admin to set one up.",
                ephemeral=True,
            )
            return

        await interaction.response.send_modal(
            ConfessionModal(self, interaction.guild)
        )

    # ── Admin command group ──────────────────────

    @commands.group(name="confessions", invoke_without_command=True)
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    async def confessions_group(self, ctx: commands.Context):
        """Manage the anonymous confessions system."""
        await ctx.send_help(ctx.command)

    @confessions_group.command(name="setchannel")
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    async def set_channel(self, ctx: commands.Context, channel: discord.TextChannel):
        """Set the channel where confessions will be posted.

        Example: `[p]confessions setchannel #confessions`
        """
        perms = channel.permissions_for(ctx.guild.me)
        if not perms.send_messages or not perms.embed_links:
            await ctx.send(
                f"❌ I need **Send Messages** and **Embed Links** permissions in {channel.mention}."
            )
            return

        await self.config.guild(ctx.guild).confession_channel.set(channel.id)
        await ctx.send(f"✅ Confession channel set to {channel.mention}.")

    @confessions_group.command(name="unsetchannel")
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    async def unset_channel(self, ctx: commands.Context):
        """Remove the configured confession channel (disables submissions)."""
        await self.config.guild(ctx.guild).confession_channel.set(None)
        await ctx.send("✅ Confession channel cleared. Submissions are paused until a new channel is set.")

    @confessions_group.command(name="enable")
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    async def enable(self, ctx: commands.Context):
        """Enable the confession system."""
        await self.config.guild(ctx.guild).enabled.set(True)
        await ctx.send("✅ Confession system enabled.")

    @confessions_group.command(name="disable")
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    async def disable(self, ctx: commands.Context):
        """Disable the confession system (no new submissions accepted)."""
        await self.config.guild(ctx.guild).enabled.set(False)
        await ctx.send("✅ Confession system disabled.")

    @confessions_group.command(name="resetcount")
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    async def reset_count(self, ctx: commands.Context):
        """Reset the confession counter back to 0."""
        await self.config.guild(ctx.guild).confession_count.set(0)
        await ctx.send("✅ Confession counter reset to 0.")

    @confessions_group.command(name="postpanel")
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    async def post_panel(self, ctx: commands.Context, channel: discord.TextChannel = None):
        """Post a confession panel with a submit button.

        Optionally specify a channel, otherwise posts in the current channel.
        Example: `[p]confessions postpanel #general`
        """
        target = channel or ctx.channel
        perms = target.permissions_for(ctx.guild.me)
        if not perms.send_messages or not perms.embed_links:
            await ctx.send(f"❌ I need **Send Messages** and **Embed Links** in {target.mention}.")
            return

        embed = discord.Embed(
            title="🤫  Anonymous Confessions",
            description=(
                "Have something on your mind? Click the button below to submit an anonymous confession.\n\n"
                "**Your identity is never recorded or stored.**"
            ),
            color=discord.Color.blurple(),
        )
        embed.set_footer(text="All confessions are 100% anonymous.")

        await target.send(embed=embed, view=ConfessButtonView())
        if target != ctx.channel:
            await ctx.send(f"✅ Confession panel posted in {target.mention}.", delete_after=5)

    @confessions_group.command(name="status")
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    async def status(self, ctx: commands.Context):
        """Show the current confession system configuration."""
        guild_data = await self.config.guild(ctx.guild).all()

        channel_id = guild_data["confession_channel"]
        channel_mention = (
            ctx.guild.get_channel(channel_id).mention
            if channel_id and ctx.guild.get_channel(channel_id)
            else "`not set`"
        )

        embed = discord.Embed(title="Confession System Status", color=discord.Color.blurple())
        embed.add_field(name="Enabled", value="✅ Yes" if guild_data["enabled"] else "❌ No", inline=True)
        embed.add_field(name="Channel", value=channel_mention, inline=True)
        embed.add_field(name="Total Confessions", value=str(guild_data["confession_count"]), inline=True)
        await ctx.send(embed=embed)