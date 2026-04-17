import discord
import asyncio
import random
import datetime
from typing import Optional, Union

from redbot.core import commands, Config, checks, bank
from redbot.core.utils.chat_formatting import humanize_list


class Marriage(commands.Cog):
    """
    Marry, gift, and vibe with other members using chaotic love energy.
    """

    __version__ = "3.0.0"

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=7283947289374, force_registration=True)

        # Default user/member values
        user_defaults = {
            "married": False,
            "current": [],
            "divorced": False,
            "exes": [],
            "about": "I'm mysterious.",
            "crush": None,
            "marcount": 0,
            "dircount": 0,
            "contentment": 100,
            "gifts": {},
        }

        guild_defaults = {
            "enabled": True,
            "multi": False,
            "marprice": 1500,
            "divprice": 2,
            "gift_text": ":gift: {author} gave {item} to {target}!",
            "actions": {},  # custom actions
            "gifts": {},    # custom gifts
            "removed_actions": [],
            "removed_gifts": [],
        }

        self.config.register_user(**user_defaults)
        self.config.register_member(**user_defaults)
        self.config.register_guild(**guild_defaults)

    # ========== Internal Defaults ==========

    def default_actions(self):
        return {
            "flirt": {
                "contentment": 5,
                "price": 0,
                "emoji": "😏",
                "require_consent": False,
                "description": "{author} flirts shamelessly with {target}..." },
            "kiss": {
                "contentment": 10,
                "price": 0,
                "emoji": "💋",
                "require_consent": True,
                "description": "{author} kisses {target} tenderly.",
                "consent_description": "{author} wants to kiss you... Do you consent?"
            },
        }

    def default_gifts(self):
        return {
            "flower": {"contentment": 5, "price": 10, "emoji": "🌸"},
            "chocolate": {"contentment": 8, "price": 15, "emoji": "🍫"},
            "ring": {"contentment": 20, "price": 250, "emoji": "💍"},
            "puppy": {"contentment": 30, "price": 500, "emoji": "🐶"},
            "castle": {"contentment": 60, "price": 10000, "emoji": "🏰"},
        }

    # ========== Helper Methods ==========

    async def _conf(self, guild: discord.Guild):
        return self.config.guild(guild)
    
    async def _user(self, user: Union[discord.Member, discord.User]):
        return self.config.member(user)

    def contentment_bar(self, value: int) -> str:
        full = "❤️" * (value // 10)
        empty = "🖤" * (10 - value // 10)
        return f"{full}{empty} ({value}/100)"

    def embed_base(self, user: Union[discord.User, discord.Member], *, title: Optional[str] = None) -> discord.Embed:
        embed = discord.Embed(color=user.color, timestamp=datetime.datetime.now())
        embed.set_author(name=title or f"{user.display_name}", icon_url=user.display_avatar.url)
        return embed

    async def get_action_data(self, ctx: commands.Context, name: str):
        name = name.lower()
        conf = await self._conf(ctx.guild)
        return (await conf.actions()).get(name) or self.default_actions().get(name)

    async def get_gift_data(self, ctx: commands.Context, name: str):
        name = name.lower()
        conf = await self._conf(ctx.guild)
        return (await conf.gifts()).get(name) or self.default_gifts().get(name)

    async def list_all_actions(self, ctx: commands.Context):
        conf = await self._conf(ctx.guild)
        removed = await conf.removed_actions()
        defaults = set(self.default_actions().keys()) - set(removed)
        customs = set((await conf.actions()).keys())
        return sorted(defaults.union(customs))

    async def list_all_gifts(self, ctx: commands.Context):
        conf = await self._conf(ctx.guild)
        removed = await conf.removed_gifts()
        defaults = set(self.default_gifts().keys()) - set(removed)
        customs = set((await conf.gifts()).keys())
        return sorted(defaults.union(customs))
    
    @commands.command()
    async def marry(self, ctx: commands.Context, member: discord.Member):
        """Propose marriage to someone!"""
        if member.id == ctx.author.id:
            return await ctx.send("You can't marry yourself, bestie.")

        conf = await self._conf(ctx.guild)
        if not await conf.enabled():
            return await ctx.send("Marriage is not enabled here.")

        multi = await conf.multi()
        a_conf = await self._user(ctx.author)
        m_conf = await self._user(member)

        if member.id in await a_conf.current():
            return await ctx.send("You two are already married!")

        if not multi:
            if await a_conf.married():
                return await ctx.send("You're already married.")
            if await m_conf.married():
                return await ctx.send("They're already married.")

        await ctx.send(f"{member.mention}, do you accept {ctx.author.mention}'s marriage proposal? (yes/no)")

        def check(m):
            return m.author == member and m.channel == ctx.channel and m.content.lower() in ["yes", "no"]

        try:
            msg = await ctx.bot.wait_for("message", timeout=60, check=check)
        except asyncio.TimeoutError:
            return await ctx.send("They ghosted you. Maybe try flowers first next time.")

        if msg.content.lower() != "yes":
            return await ctx.send("Your proposal was rejected. Sad times.")

        price = await conf.marprice()
        author_bal = await bank.get_balance(ctx.author)
        target_bal = await bank.get_balance(member)

        if author_bal < price or target_bal < price:
            return await ctx.send("You both need enough money to get married, broke lovers!")

        await bank.withdraw_credits(ctx.author, price)
        await bank.withdraw_credits(member, price)

        await a_conf.married.set(True)
        await m_conf.married.set(True)
        await a_conf.divorced.set(False)
        await m_conf.divorced.set(False)

        async with a_conf.current() as a:
            a.append(member.id)
        async with m_conf.current() as m:
            m.append(ctx.author.id)

        await a_conf.marcount.set(await a_conf.marcount() + 1)
        await m_conf.marcount.set(await m_conf.marcount() + 1)

        await a_conf.contentment.set(100)
        await m_conf.contentment.set(100)

        embed = discord.Embed(
            title="💍 Marriage Ceremony 💍",
            description=f"{ctx.author.mention} and {member.mention} are now married! Congrats!",
            color=discord.Color.gold(),
            timestamp=datetime.datetime.now()
        )
        embed.set_footer(text=f"Each paid {price} {await bank.get_currency_name(ctx.guild)}")
        await ctx.send(embed=embed)

    @commands.command()
    async def divorce(self, ctx: commands.Context, member: discord.Member):
        """Divorce someone you're married to."""
        if member.id == ctx.author.id:
            return await ctx.send("You can't divorce yourself, drama llama.")

        conf = await self._conf(ctx.guild)
        a_conf = await self._user(ctx.author)
        m_conf = await self._user(member)

        current = await a_conf.current()
        if member.id not in current:
            return await ctx.send("You two aren't married!")

        price = await conf.marprice()
        multiplier = await conf.divprice()
        total = price * multiplier

        if await bank.get_balance(ctx.author) < total:
            return await ctx.send("You can't afford this heartbreak. Divorce is expensive.")

        await bank.withdraw_credits(ctx.author, total)

        async with a_conf.current() as a:
            a.remove(member.id)
        async with m_conf.current() as m:
            m.remove(ctx.author.id)
        async with a_conf.exes() as a:
            a.append(member.id)
        async with m_conf.exes() as m:
            m.append(ctx.author.id)

        if not await a_conf.current():
            await a_conf.married.set(False)
            await a_conf.divorced.set(True)
        if not await m_conf.current():
            await m_conf.married.set(False)
            await m_conf.divorced.set(True)

        embed = discord.Embed(
            title="💔 Divorce Decree 💔",
            description=f"{ctx.author.mention} and {member.mention} are no longer together.",
            color=discord.Color.red(),
            timestamp=datetime.datetime.now()
        )
        embed.set_footer(text=f"{ctx.author.display_name} paid {total} {await bank.get_currency_name(ctx.guild)}")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def gift(self, ctx: commands.Context, member: discord.Member = None, gift: str = None):
        """Gift something to someone. Shows available gifts if no input."""
        if not member or not gift:
            conf = await self._conf(ctx.guild)
            all_gifts = await conf.gifts()
            gift_names = list(all_gifts.keys()) + list(self.default_gifts().keys())
            gift_names = sorted(set(gift_names))
            embed = discord.Embed(
                title="🎁 Available Gifts",
                description="\n".join(gift_names),
                color=discord.Color.blurple()
            )
            return await ctx.send(embed=embed)

        conf = await self._conf(ctx.guild)
        if not await conf.enabled():
            return await ctx.send("Marriage features are disabled here.")

        gifts = await self.list_all_gifts(ctx)
        if gift.lower() not in gifts:
            return await ctx.send(f"That isn't a valid gift. Try one of: {', '.join(gifts)}")

        gdata = await self.get_gift_data(ctx, gift)
        price = gdata.get("price", 0)
        contentment = gdata.get("contentment", 0)
        emoji = gdata.get("emoji", "🎁")

        if await bank.get_balance(ctx.author) < price:
            return await ctx.send("You can't afford that gift, sweetheart.")

        await bank.withdraw_credits(ctx.author, price)

        author_conf = await self._user(ctx.author)
        member_conf = await self._user(member)

        await member_conf.contentment.set(min(await member_conf.contentment() + contentment, 100))

        gift_text = await conf.gift_text()
        description = gift_text.format(author=ctx.author.mention, item=f"{emoji} {gift.title()}", target=member.mention)

        embed = discord.Embed(
            title="🎁 Gift Given!",
            description=description,
            color=discord.Color.green(),
            timestamp=datetime.datetime.now()
        )
        embed.set_footer(text=f"Cost: {price} {await bank.get_currency_name(ctx.guild)}")
        await ctx.send(embed=embed)

    @commands.command()
    async def perform(self, ctx: commands.Context, action: str, member: discord.Member):
        """Perform a spicy or sweet action on someone."""
        if member.id == ctx.author.id:
            return await ctx.send("You can't perform an action on yourself. That's just journaling.")

        conf = await self._conf(ctx.guild)
        if not await conf.enabled():
            return await ctx.send("Marriage features are disabled here.")

        actions = await self.list_all_actions(ctx)
        if action.lower() not in actions:
            return await ctx.send(f"That isn't a valid action. Try one of: {', '.join(actions)}")

        adata = await self.get_action_data(ctx, action)
        emoji = adata.get("emoji", "💞")
        description = adata.get("description", "{author} did something weird to {target}.")
        consent_needed = adata.get("require_consent", False)
        consent_prompt = adata.get("consent_description", "Do you accept this action?")
        price = adata.get("price", 0)
        contentment = adata.get("contentment", 0)
        description = adata.get("description", "{author} did something to {target}.")
        consent_description = adata.get("consent_description", "Do you accept this?")

        formatted_description = description.format(author=ctx.author.mention, target=member.mention)
        formatted_consent_prompt = consent_description.format(author=ctx.author.mention, target=member.mention)

        if await bank.get_balance(ctx.author) < price:
            return await ctx.send("You can't afford this action, broke babe.")

        if consent_needed:
            await ctx.send(f"{member.mention}, {formatted_consent_prompt}")

            def check(m):
                return m.author == member and m.channel == ctx.channel and m.content.lower() in ["yes", "no"]

            try:
                reply = await self.bot.wait_for("message", timeout=60, check=check)
            except asyncio.TimeoutError:
                return await ctx.send("They didn’t respond in time.")

            if reply.content.lower() != "yes":
                return await ctx.send("They rejected the action. Oof.")

        await bank.withdraw_credits(ctx.author, price)

        author_conf = await self._user(ctx.author)
        member_conf = await self._user(member)

        await author_conf.contentment.set(min(await author_conf.contentment() + contentment, 100))
        await member_conf.contentment.set(min(await member_conf.contentment() + contentment, 100))

        result = description.format(author=ctx.author.mention, target=member.mention)
        embed = discord.Embed(
            title=f"{emoji} Action Performed!",
            description=result,
            color=discord.Color.purple(),
            timestamp=datetime.datetime.now()
        )
        embed.set_footer(text=f"Cost: {price} minerals")
        await ctx.send(embed=embed) 
        
    @commands.group()
    @commands.is_owner()
    async def marryset(self, ctx: commands.Context):
        """Marriage admin settings (owner only)."""
        if ctx.invoked_subcommand is None:
            pass

    @marryset.group(name="gifts")
    async def marryset_gifts(self, ctx: commands.Context):
        """Manage custom gifts."""
        if ctx.invoked_subcommand is None:
            pass

    @marryset_gifts.command(name="add")
    async def marryset_gift_add(self, ctx: commands.Context, name: str, contentment: int, price: int, emoji: Optional[str] = None):
        conf = await self._conf(ctx.guild)
        async with conf.gifts() as gifts:
            gifts[name.lower()] = {
                "contentment": contentment,
                "price": price,
                "emoji": emoji or "🎁"
            }
        await ctx.send(f"✅ Added gift: {emoji or '🎁'} {name.title()} - {contentment} contentment, {price} cost")

    @marryset_gifts.command(name="remove")
    async def marryset_gift_remove(self, ctx: commands.Context, name: str):
        conf = await self._conf(ctx.guild)
        async with conf.gifts() as gifts:
            if name.lower() in gifts:
                del gifts[name.lower()]
                await ctx.send(f"❌ Removed gift `{name}`.")
            else:
                await ctx.send("That gift wasn't found.")

    @marryset_gifts.command(name="list")
    async def marryset_gift_list(self, ctx: commands.Context):
        conf = await self._conf(ctx.guild)
        gifts = await conf.gifts()
        if not gifts:
            return await ctx.send("No custom gifts set.")
        lines = [f"{v.get('emoji','🎁')} `{k}` - {v['contentment']} contentment, {v['price']} cost" for k, v in gifts.items()]
        await ctx.send("\n".join(lines))

    @marryset.group(name="actions")
    async def marryset_actions(self, ctx: commands.Context):
        """Manage custom actions."""
        if ctx.invoked_subcommand is None:
            pass

    @marryset_actions.command(name="add")
    async def marryset_action_add(
        self,
        ctx: commands.Context,
        name: str,
        contentment: int,
        price: int,
        require_consent: bool,
        *,
        raw: str
    ):
        """
        Add a custom action.
        Format: [p]marryset actions add name contentment price require_consent action %% consent_prompt
        If consent is False, omit the %% part.
        """
        parts = [p.strip() for p in raw.split("%%")]

        if not parts or not parts[0]:
            return await ctx.send("❌ You must provide an action description.")

        if require_consent and len(parts) < 2:
            return await ctx.send("❌ You must provide a consent prompt when `require_consent` is True.")

        description = parts[0]
        consent_description = parts[1] if require_consent else ""

        conf = await self._conf(ctx.guild)
        async with conf.actions() as actions:
            actions[name.lower()] = {
                "contentment": contentment,
                "price": price,
                "require_consent": require_consent,
                "description": description,
                "consent_description": consent_description,
                "emoji": "✨"
            }

        await ctx.send(f"✅ Action `{name}` added. Consent required: `{require_consent}`.")


    @marryset_actions.command(name="remove")
    async def marryset_action_remove(self, ctx: commands.Context, name: str):
        conf = await self._conf(ctx.guild)
        async with conf.actions() as actions:
            if name.lower() in actions:
                del actions[name.lower()]
                await ctx.send(f"❌ Removed action `{name}`.")
            else:
                await ctx.send("That action wasn't found.")

    @marryset_actions.command(name="list")
    async def marryset_action_list(self, ctx: commands.Context):
        conf = await self._conf(ctx.guild)
        actions = await conf.actions()
        if not actions:
            return await ctx.send("No custom actions set.")
        lines = [
            f"{v.get('emoji','✨')} `{k}` - {v['contentment']} contentment, {v['price']} cost, Consent: {v['require_consent']}"
            for k, v in actions.items()
        ]
        await ctx.send("\n".join(lines))
        
    @commands.command()
    async def about(self, ctx: commands.Context, member: Optional[discord.Member] = None):
        """See someone's marriage profile."""
        member = member or ctx.author
        conf = await self._conf(ctx.guild)
        if not await conf.enabled():
            return await ctx.send("Marriage features are disabled here.")

        uconf = await self._user(member)
        status = "Single"
        if await uconf.married():
            status = "Married"
        elif await uconf.divorced():
            status = "Divorced"

        spouses = await uconf.current()
        exes = await uconf.exes()
        crush_id = await uconf.crush()
        gifts = await uconf.gifts()

        embed = self.embed_base(member, title=f"{member.display_name}'s Marriage Profile")
        embed.add_field(name="Status", value=status)

        if spouses:
            names = []
            for sid in spouses:
                user = ctx.guild.get_member(sid) or self.bot.get_user(sid)
                if user:
                    sconf = await self._user(user)
                    names.append(f"{user.display_name}: {self.contentment_bar(await sconf.contentment())}")
            embed.add_field(name="Spouses", value="\n".join(names), inline=False)

        if exes:
            exnames = [ctx.guild.get_member(e) or self.bot.get_user(e) for e in exes]
            embed.add_field(name="Exes", value=humanize_list([e.display_name for e in exnames if e]), inline=False)

        if crush_id:
            crush = ctx.guild.get_member(crush_id) or self.bot.get_user(crush_id)
            if crush:
                embed.add_field(name="Crush", value=crush.display_name)

        embed.add_field(name="Contentment", value=self.contentment_bar(await uconf.contentment()), inline=False)

        if gifts:
            glines = [f"{k} x{v}" for k, v in gifts.items() if v > 0]
            if glines:
                embed.add_field(name="Gifts Owned", value="\n".join(glines), inline=False)

        embed.set_footer(text=f"{member} | ID: {member.id}")
        await ctx.send(embed=embed)

    @commands.command()
    async def spouses(self, ctx: commands.Context, member: Optional[discord.Member] = None):
        """View someone's current spouses."""
        member = member or ctx.author
        conf = await self._conf(ctx.guild)
        if not await conf.enabled():
            return await ctx.send("Marriage features are disabled here.")

        uconf = await self._user(member)
        spouses = await uconf.current()
        if not spouses:
            return await ctx.send(f"{member.display_name} has no spouses.")

        lines = []
        for sid in spouses:
            sp = ctx.guild.get_member(sid) or self.bot.get_user(sid)
            if sp:
                spconf = await self._user(sp)
                lines.append(f"{sp.display_name}: {self.contentment_bar(await spconf.contentment())}")

        embed = self.embed_base(member, title=f"{member.display_name}'s Spouses")
        embed.description = "\n".join(lines)
        await ctx.send(embed=embed)

    @commands.command()
    async def exes(self, ctx: commands.Context, member: Optional[discord.Member] = None):
        """See someone's exes."""
        member = member or ctx.author
        conf = await self._conf(ctx.guild)
        if not await conf.enabled():
            return await ctx.send("Marriage features are disabled here.")

        uconf = await self._user(member)
        exes = await uconf.exes()
        if not exes:
            return await ctx.send(f"{member.display_name} has no exes. Fresh start energy ✨")

        names = [ctx.guild.get_member(e) or self.bot.get_user(e) for e in exes]
        namelist = humanize_list([n.display_name for n in names if n])
        embed = self.embed_base(member, title=f"{member.display_name}'s Exes")
        embed.description = namelist
        await ctx.send(embed=embed)