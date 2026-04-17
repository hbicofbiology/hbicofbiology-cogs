import discord
import datetime
from redbot.core import commands, Config


class ConfessModal(discord.ui.Modal, title="💌 Anonymous Confession"):
    target = discord.ui.TextInput(
        label="User ID",
        placeholder="123456789",
        required=True
    )
    message = discord.ui.TextInput(
        label="Your message",
        style=discord.TextStyle.paragraph
    )

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    async def on_submit(self, interaction: discord.Interaction):
        try:
            user = await self.bot.fetch_user(int(self.target.value))
        except Exception:
            return await interaction.response.send_message(
                "❌ Invalid user ID.", ephemeral=True
            )

        embed = discord.Embed(
            title="💘 You've received an anonymous confession!",
            description=self.message.value,
            color=discord.Color.magenta(),
            timestamp=datetime.datetime.now()
        )

        try:
            await user.send(embed=embed)
            await interaction.response.send_message(
                "📨 Sent!", ephemeral=True
            )
        except discord.Forbidden:
            await interaction.response.send_message(
                "❌ Couldn't DM them.", ephemeral=True
            )


class ConfessView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=60)
        self.bot = bot

    @discord.ui.button(label="💌 Confess Anonymously", style=discord.ButtonStyle.primary)
    async def confess(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(ConfessModal(self.bot))


class LoveConfessions(commands.Cog):
    """Send spicy or sweet anonymous confessions 💌"""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=999999123123)

    @commands.command()
    async def confess(self, ctx, member: discord.Member, *, message: str):
        """Send a public confession."""
        try:
            await ctx.message.delete()
        except:
            pass

        embed = discord.Embed(
            title="💘 You've received a confession!",
            description=message,
            color=discord.Color.red(),
            timestamp=datetime.datetime.now()
        )
        embed.set_footer(text=f"From {ctx.author.display_name}")

        try:
            await member.send(embed=embed)
            await ctx.send("📨 Delivered!", delete_after=5)
        except:
            await ctx.send("❌ Couldn't DM them.", delete_after=5)

    @commands.command()
    async def confessanon(self, ctx):
        """Anonymous confession UI."""
        try:
            await ctx.message.delete()
        except:
            pass

        await ctx.send(
            "Click to confess anonymously:",
            view=ConfessView(self.bot),
            delete_after=60
        )