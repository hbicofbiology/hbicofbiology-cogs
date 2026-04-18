from __future__ import annotations
from redbot.core import commands, Config
from redbot.core.bot import Red
import discord
import asyncio
from typing import Optional, List


class RoleSelect(discord.ui.Select):
    def __init__(self, options: List[discord.SelectOption], placeholder: str):
        super().__init__(
            placeholder=placeholder,
            min_values=0,
            max_values=len(options),
            options=options,
            custom_id="roledropdown:select",
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        member = interaction.user
        guild = interaction.guild
        if guild is None:
            return

        dropdown_role_ids = {int(opt.value) for opt in self.options}
        selected_ids = {int(v) for v in self.values}

        added, removed = [], []
        for role_id in dropdown_role_ids:
            role = guild.get_role(role_id)
            if role is None:
                continue
            if role_id in selected_ids and role not in member.roles:
                await member.add_roles(role, reason="Role dropdown")
                added.append(role.name)
            elif role_id not in selected_ids and role in member.roles:
                await member.remove_roles(role, reason="Role dropdown")
                removed.append(role.name)

        parts = []
        if added:
            parts.append(f"Added: {', '.join(f'**{r}**' for r in added)}")
        if removed:
            parts.append(f"Removed: {', '.join(f'**{r}**' for r in removed)}")
        msg = "\n".join(parts) if parts else "No changes made."
        await interaction.followup.send(msg, ephemeral=True)


class RoleDropdownView(discord.ui.View):
    def __init__(self, options: List[discord.SelectOption], placeholder: str):
        super().__init__(timeout=None)
        self.add_item(RoleSelect(options, placeholder))


class RoleDropdown(commands.Cog):
    """Simple role selection dropdowns."""

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=9182736450, force_registration=True)
        self.config.register_guild(dropdowns={})
        self.bot.loop.create_task(self._restore_views())

    async def _restore_views(self):
        """Re-register persistent views after bot restart."""
        await self.bot.wait_until_ready()
        all_guilds = await self.config.all_guilds()
        for guild_id, data in all_guilds.items():
            for msg_id, dd in data.get("dropdowns", {}).items():
                options = self._build_options(dd["roles"])
                if options:
                    view = RoleDropdownView(options, dd.get("placeholder", "Select roles..."))
                    self.bot.add_view(view, message_id=int(msg_id))

    def _build_options(self, roles: List[dict]) -> List[discord.SelectOption]:
        options = []
        for r in roles:
            opt = discord.SelectOption(
                label=r["label"],
                value=str(r["id"]),
                description=r.get("description") or None,
            )
            if r.get("emoji"):
                opt.emoji = r["emoji"]
            options.append(opt)
        return options

    # -------------------------------------------------------------------------
    # Commands
    # -------------------------------------------------------------------------

    @commands.group(invoke_without_command=True)
    @commands.guild_only()
    @commands.admin_or_permissions(manage_roles=True)
    async def roledropdown(self, ctx: commands.Context):
        """Manage role selection dropdowns."""
        await ctx.send_help()

    @roledropdown.command(name="create")
    @commands.guild_only()
    @commands.admin_or_permissions(manage_roles=True)
    async def create(
        self,
        ctx: commands.Context,
        channel: discord.TextChannel,
        *,
        title: str = "Pick your roles!",
    ):
        """Post a new (empty) role dropdown in a channel.

        Example: `[p]roledropdown create #roles Pick your roles!`
        """
        placeholder = "Select roles..."
        view = RoleDropdownView(
            [discord.SelectOption(label="(No roles yet)", value="placeholder")],
            placeholder,
        )
        msg = await channel.send(f"**{title}**", view=view)

        async with self.config.guild(ctx.guild).dropdowns() as dropdowns:
            dropdowns[str(msg.id)] = {
                "channel_id": channel.id,
                "title": title,
                "placeholder": placeholder,
                "roles": [],
            }

        await ctx.send(f"Dropdown created! Message ID: `{msg.id}`\nUse `[p]roledropdown add {msg.id} @Role` to add roles.")

    @roledropdown.command(name="add")
    @commands.guild_only()
    @commands.admin_or_permissions(manage_roles=True)
    async def add_role(
        self,
        ctx: commands.Context,
        message_id: int,
        role: discord.Role,
        label: Optional[str] = None,
        description: Optional[str] = None,
        emoji: Optional[str] = None,
    ):
        """Add a role to an existing dropdown.

        - `label` defaults to the role name
        - `description` is optional short text shown under the label
        - `emoji` is optional (e.g. 🎮)

        Example: `[p]roledropdown add 1234567890 @Gamer Gamer "For gamers" 🎮`
        """
        async with self.config.guild(ctx.guild).dropdowns() as dropdowns:
            dd = dropdowns.get(str(message_id))
            if dd is None:
                await ctx.send("No dropdown found with that message ID.")
                return

            if any(r["id"] == role.id for r in dd["roles"]):
                await ctx.send(f"{role.name} is already in that dropdown.")
                return

            if len(dd["roles"]) >= 25:
                await ctx.send("Discord limits dropdowns to 25 options.")
                return

            dd["roles"].append({
                "id": role.id,
                "label": label or role.name,
                "description": description,
                "emoji": emoji,
            })

        await self._refresh_message(ctx.guild, message_id)
        await ctx.send(f"Added **{role.name}** to the dropdown.")

    @roledropdown.command(name="remove")
    @commands.guild_only()
    @commands.admin_or_permissions(manage_roles=True)
    async def remove_role(self, ctx: commands.Context, message_id: int, role: discord.Role):
        """Remove a role from a dropdown.

        Example: `[p]roledropdown remove 1234567890 @Gamer`
        """
        async with self.config.guild(ctx.guild).dropdowns() as dropdowns:
            dd = dropdowns.get(str(message_id))
            if dd is None:
                await ctx.send("No dropdown found with that message ID.")
                return

            before = len(dd["roles"])
            dd["roles"] = [r for r in dd["roles"] if r["id"] != role.id]
            if len(dd["roles"]) == before:
                await ctx.send(f"{role.name} wasn't in that dropdown.")
                return

        await self._refresh_message(ctx.guild, message_id)
        await ctx.send(f"Removed **{role.name}** from the dropdown.")

    @roledropdown.command(name="delete")
    @commands.guild_only()
    @commands.admin_or_permissions(manage_roles=True)
    async def delete(self, ctx: commands.Context, message_id: int):
        """Delete a dropdown message entirely.

        Example: `[p]roledropdown delete 1234567890`
        """
        async with self.config.guild(ctx.guild).dropdowns() as dropdowns:
            dd = dropdowns.pop(str(message_id), None)
            if dd is None:
                await ctx.send("No dropdown found with that message ID.")
                return
            channel = ctx.guild.get_channel(dd["channel_id"])
            if channel:
                try:
                    msg = await channel.fetch_message(message_id)
                    await msg.delete()
                except (discord.NotFound, discord.Forbidden):
                    pass

        await ctx.send("Dropdown deleted.")

    @roledropdown.command(name="list")
    @commands.guild_only()
    @commands.admin_or_permissions(manage_roles=True)
    async def list_dropdowns(self, ctx: commands.Context):
        """List all dropdowns in this server."""
        dropdowns = await self.config.guild(ctx.guild).dropdowns()
        if not dropdowns:
            await ctx.send("No dropdowns set up yet.")
            return

        lines = []
        for msg_id, dd in dropdowns.items():
            channel = ctx.guild.get_channel(dd["channel_id"])
            ch_mention = channel.mention if channel else f"(deleted channel {dd['channel_id']})"
            role_names = [r["label"] for r in dd["roles"]] or ["(none)"]
            lines.append(f"**{dd['title']}** — {ch_mention}\n  ID: `{msg_id}` | Roles: {', '.join(role_names)}")

        await ctx.send("\n\n".join(lines))

    # -------------------------------------------------------------------------
    # Helpers
    # -------------------------------------------------------------------------

    async def _refresh_message(self, guild: discord.Guild, message_id: int):
        """Rebuild the dropdown view and edit the message."""
        dropdowns = await self.config.guild(guild).dropdowns()
        dd = dropdowns.get(str(message_id))
        if dd is None:
            return

        channel = guild.get_channel(dd["channel_id"])
        if channel is None:
            return

        try:
            msg = await channel.fetch_message(message_id)
        except (discord.NotFound, discord.Forbidden):
            return

        options = self._build_options(dd["roles"])
        if not options:
            options = [discord.SelectOption(label="(No roles yet)", value="placeholder")]

        view = RoleDropdownView(options, dd.get("placeholder", "Select roles..."))
        self.bot.add_view(view, message_id=message_id)
        await msg.edit(view=view)