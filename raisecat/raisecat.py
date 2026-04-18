import asyncio
import random
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import discord
from redbot.core import Config, commands
from redbot.core.bot import Red
from redbot.core.data_manager import bundled_data_path


# ─── Life Stages ────────────────────────────────────────────────────────────────

LIFE_STAGES = [
    {"name": "kitten", "min_xp": 0, "label": "🐱 Kitten", "gif": "kitten.gif"},
    {"name": "young", "min_xp": 100, "label": "🐈 Young Cat", "gif": "young.gif"},
    {"name": "adult", "min_xp": 500, "label": "🐈‍⬛ Adult Cat", "gif": "adult.gif"},
    {"name": "elder", "min_xp": 1500, "label": "👑 Elder Cat", "gif": "elder.gif"},
]

DEFAULT_NAMES = [
    "Whiskers", "Mittens", "Shadow", "Luna", "Mochi",
    "Biscuit", "Noodle", "Pickle", "Bean", "Cleo",
    "Gizmo", "Tofu", "Pepper", "Waffles", "Ziggy",
]

BREED_LIST = [
    "Tabby", "Tuxedo", "Calico", "Orange Tabby", "Siamese",
    "Maine Coon", "Russian Blue", "Void (Black Cat)", "Tortoiseshell",
    "Scottish Fold", "Ragdoll", "Sphynx", "Munchkin", "Bengal",
]

PERSONALITY_TRAITS = [
    "mischievous", "lazy", "curious", "affectionate", "sassy",
    "chaotic", "regal", "derpy", "adventurous", "dramatic",
]

AVAILABLE_TRICKS = [
    {"name": "Sit", "xp_required": 0, "difficulty": 1},
    {"name": "High Five", "xp_required": 50, "difficulty": 2},
    {"name": "Roll Over", "xp_required": 100, "difficulty": 3},
    {"name": "Fetch", "xp_required": 200, "difficulty": 4},
    {"name": "Play Dead", "xp_required": 350, "difficulty": 5},
    {"name": "Backflip", "xp_required": 500, "difficulty": 6},
    {"name": "Open Doors", "xp_required": 750, "difficulty": 7},
    {"name": "Hack the Mainframe", "xp_required": 1000, "difficulty": 8},
    {"name": "File Taxes", "xp_required": 1500, "difficulty": 9},
]

COOLDOWNS = {
    "feed": 1800,
    "play": 1200,
    "groom": 3600,
    "vet": 7200,
    "train": 2400,
}

FEED_MESSAGES = [
    "{cat} munches on the {food} happily! 😋",
    "{cat} sniffs the {food}... then devours it!",
    "{cat} does a little dance before eating the {food}!",
    "{cat} purrs loudly while eating the {food}.",
    "{cat} knocks the {food} off the table first, then eats it off the floor. Classic.",
]

FOOD_ITEMS = [
    "tuna", "kibble", "salmon", "chicken", "fancy feast",
    "sardines", "shrimp", "turkey", "cheese (just a nibble)",
    "mysterious wet food", "catnip-infused treats",
]

PLAY_MESSAGES = [
    "{cat} chases the {toy} around the room! 🎾",
    "{cat} pounces on the {toy} with deadly precision!",
    "{cat} bats the {toy} under the couch. It's gone forever now.",
    "{cat} does zoomies after playing with the {toy}!",
    "{cat} pretends to be uninterested in the {toy}... then ATTACKS!",
]

PLAY_TOYS = [
    "laser pointer", "feather wand", "crinkle ball", "cardboard box",
    "hair tie", "mouse toy", "paper bag", "your shoelaces",
    "invisible bug on the wall", "their own tail",
]

GROOM_MESSAGES = [
    "{cat} purrs while being brushed! ✨",
    "{cat} tolerates the grooming... barely.",
    "{cat} looks so fluffy after the grooming session!",
    "{cat} tries to eat the brush. Typical.",
    "{cat} falls asleep mid-grooming. So peaceful!",
]

VET_MESSAGES = [
    "{cat} got a clean bill of health! 🏥",
    "{cat} was NOT happy about the vet visit but feels better now.",
    "The vet says {cat} is in great shape!",
    "{cat} hid in the carrier the whole time but is all patched up.",
    "{cat} charmed the entire vet's office. Star patient!",
]

TRAIN_SUCCESS = [
    "{cat} learned {trick}! What a genius! 🎓",
    "After much bribery, {cat} can now do {trick}!",
    "{cat} nails {trick} on the first try! Prodigy!",
]

TRAIN_FAIL = [
    "{cat} stared at you blankly. Maybe next time.",
    "{cat} yawned and walked away. Training session over.",
    "{cat} attempted {trick} but got distracted by a dust particle.",
    "{cat} gave you a look that said 'absolutely not.'",
]


class RaiseCat(commands.Cog):
    """Raise a shared server cat together!"""

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=7274837291, force_registration=True)

        default_guild = {
            "cat": None,
            "leaderboard": {},
        }
        default_member = {
            "cooldowns": {},
        }

        self.config.register_guild(**default_guild)
        self.config.register_member(**default_member)

    # ─── Helpers ────────────────────────────────────────────────────────────

    def _get_data_path(self) -> Path:
        return bundled_data_path(self)

    def _get_cat_gif(self, stage_name: str) -> Path:
        return self._get_data_path() / f"{stage_name}.gif"

    def _get_life_stage(self, xp: int) -> dict:
        stage = LIFE_STAGES[0]
        for s in LIFE_STAGES:
            if xp >= s["min_xp"]:
                stage = s
        return stage

    def _next_stage(self, xp: int) -> Optional[dict]:
        current = self._get_life_stage(xp)
        idx = LIFE_STAGES.index(current)
        if idx + 1 < len(LIFE_STAGES):
            return LIFE_STAGES[idx + 1]
        return None

    def _stat_bar(self, value: int, max_val: int = 100, length: int = 10) -> str:
        filled = round((value / max_val) * length)
        empty = length - filled
        return f"[{'█' * filled}{'░' * empty}] {value}/{max_val}"

    async def _check_cooldown(self, member: discord.Member, action: str) -> Optional[int]:
        cooldowns = await self.config.member(member).cooldowns()
        last_used = cooldowns.get(action, 0)
        elapsed = time.time() - last_used
        remaining = COOLDOWNS[action] - elapsed
        if remaining > 0:
            return int(remaining)
        return None

    async def _set_cooldown(self, member: discord.Member, action: str):
        async with self.config.member(member).cooldowns() as cooldowns:
            cooldowns[action] = time.time()

    async def _add_leaderboard(self, guild: discord.Guild, user_id: int, action: str, points: int):
        uid = str(user_id)
        async with self.config.guild(guild).leaderboard() as lb:
            if uid not in lb:
                lb[uid] = {"feed": 0, "play": 0, "groom": 0, "vet": 0, "train": 0, "total": 0}
            lb[uid][action] = lb[uid].get(action, 0) + points
            lb[uid]["total"] = lb[uid].get("total", 0) + points

    async def _get_cat(self, guild: discord.Guild) -> Optional[dict]:
        return await self.config.guild(guild).cat()

    async def _ensure_cat(self, ctx: commands.Context) -> Optional[dict]:
        cat = await self._get_cat(ctx.guild)
        if cat is None:
            await ctx.send("🐱 This server doesn't have a cat yet! Use `[p]cat adopt` to get one!")
            return None
        return cat

    async def _send_with_gif(self, ctx: commands.Context, embed: discord.Embed, stage_name: str):
        gif_path = self._get_cat_gif(stage_name)
        if gif_path.exists():
            file = discord.File(str(gif_path), filename=f"{stage_name}.gif")
            embed.set_thumbnail(url=f"attachment://{stage_name}.gif")
            await ctx.send(embed=embed, file=file)
        else:
            await ctx.send(embed=embed)

    def _build_status_embed(self, cat: dict, guild: discord.Guild) -> discord.Embed:
        stage = self._get_life_stage(cat["xp"])
        next_stage = self._next_stage(cat["xp"])

        embed = discord.Embed(
            title=f"{stage['label']} {cat['name']}",
            description=f"*{cat['breed']} · {cat['personality']}*",
            color=discord.Color.from_rgb(255, 183, 77),
        )

        embed.add_field(
            name="📊 Stats",
            value=(
                f"🍗 Hunger:      {self._stat_bar(cat['hunger'])}\n"
                f"😸 Happiness:   {self._stat_bar(cat['happiness'])}\n"
                f"✨ Cleanliness: {self._stat_bar(cat['cleanliness'])}\n"
                f"❤️ Health:       {self._stat_bar(cat['health'])}"
            ),
            inline=False,
        )

        if next_stage:
            xp_str = f"⭐ XP: {cat['xp']} / {next_stage['min_xp']} (next: {next_stage['label']})"
        else:
            xp_str = f"⭐ XP: {cat['xp']} (MAX STAGE)"
        embed.add_field(name="📈 Growth", value=xp_str, inline=False)

        if cat.get("tricks"):
            tricks_str = ", ".join(cat["tricks"])
        else:
            tricks_str = "None yet! Use `[p]cat train` to teach tricks."
        embed.add_field(name="🎓 Tricks Learned", value=tricks_str, inline=False)

        embed.set_footer(text=f"Born: {cat['born']} | Server: {guild.name}")
        return embed

    async def _handle_stage_evolution(
        self, ctx: commands.Context, cat: dict, old_xp: int, action_msg: str, stat_msg: str
    ):
        old_stage = self._get_life_stage(old_xp)
        new_stage = self._get_life_stage(cat["xp"])

        if old_stage["name"] != new_stage["name"]:
            embed = discord.Embed(
                title=f"🎉 {cat['name']} has grown into a {new_stage['label']}!",
                description=f"{action_msg}\n{stat_msg}",
                color=discord.Color.gold(),
            )
            await self._send_with_gif(ctx, embed, new_stage["name"])
        else:
            await ctx.send(f"{action_msg}\n{stat_msg}")

    # ─── Commands ───────────────────────────────────────────────────────────

    @commands.group(name="cat", invoke_without_command=True)
    @commands.guild_only()
    async def cat_group(self, ctx: commands.Context):
        """🐱 Raise your server's cat! Use `[p]cat status` to check on them."""
        cat = await self._get_cat(ctx.guild)
        if cat is None:
            await ctx.send(
                "🐱 This server doesn't have a cat yet!\n"
                "Use `[p]cat adopt` to adopt one!"
            )
        else:
            await ctx.invoke(self.cat_status)

    @cat_group.command(name="adopt")
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def cat_adopt(self, ctx: commands.Context, *, name: str = None):
        """Adopt a cat for the server! Admins only.

        Optionally provide a name, or let the cat name itself.
        """
        existing = await self._get_cat(ctx.guild)
        if existing is not None:
            await ctx.send(
                f"🐱 This server already has a cat named **{existing['name']}**! "
                "Use `[p]cat status` to check on them."
            )
            return

        cat_name = name or random.choice(DEFAULT_NAMES)
        breed = random.choice(BREED_LIST)
        personality = random.choice(PERSONALITY_TRAITS)

        cat = {
            "name": cat_name,
            "breed": breed,
            "personality": personality,
            "hunger": 50,
            "happiness": 50,
            "cleanliness": 50,
            "health": 50,
            "xp": 0,
            "tricks": [],
            "born": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "adopted_by": ctx.author.id,
        }

        await self.config.guild(ctx.guild).cat.set(cat)

        embed = discord.Embed(
            title="🎉 A New Cat Has Been Adopted!",
            description=(
                f"Everyone, meet **{cat_name}**!\n\n"
                f"**Breed:** {breed}\n"
                f"**Personality:** {personality}\n\n"
                "Take care of them together using `[p]cat` commands!"
            ),
            color=discord.Color.green(),
        )
        await self._send_with_gif(ctx, embed, "kitten")

    @cat_group.command(name="status")
    @commands.guild_only()
    async def cat_status(self, ctx: commands.Context):
        """Check on the server's cat."""
        cat = await self._ensure_cat(ctx)
        if cat is None:
            return
        stage = self._get_life_stage(cat["xp"])
        embed = self._build_status_embed(cat, ctx.guild)
        await self._send_with_gif(ctx, embed, stage["name"])

    @cat_group.command(name="feed")
    @commands.guild_only()
    async def cat_feed(self, ctx: commands.Context):
        """Feed the server's cat. 🍗"""
        cat = await self._ensure_cat(ctx)
        if cat is None:
            return

        remaining = await self._check_cooldown(ctx.author, "feed")
        if remaining:
            mins, secs = divmod(remaining, 60)
            await ctx.send(f"⏳ You can feed {cat['name']} again in **{mins}m {secs}s**.")
            return

        food = random.choice(FOOD_ITEMS)
        msg = random.choice(FEED_MESSAGES).format(cat=cat["name"], food=food)

        hunger_gain = random.randint(8, 15)
        xp_gain = random.randint(3, 7)
        old_xp = cat["xp"]

        cat["hunger"] = min(100, cat["hunger"] + hunger_gain)
        cat["xp"] += xp_gain

        await self.config.guild(ctx.guild).cat.set(cat)
        await self._set_cooldown(ctx.author, "feed")
        await self._add_leaderboard(ctx.guild, ctx.author.id, "feed", xp_gain)

        stat_msg = f"🍗 Hunger: +{hunger_gain} | ⭐ XP: +{xp_gain}"
        await self._handle_stage_evolution(ctx, cat, old_xp, msg, stat_msg)

    @cat_group.command(name="play")
    @commands.guild_only()
    async def cat_play(self, ctx: commands.Context):
        """Play with the server's cat. 🎾"""
        cat = await self._ensure_cat(ctx)
        if cat is None:
            return

        remaining = await self._check_cooldown(ctx.author, "play")
        if remaining:
            mins, secs = divmod(remaining, 60)
            await ctx.send(f"⏳ You can play with {cat['name']} again in **{mins}m {secs}s**.")
            return

        toy = random.choice(PLAY_TOYS)
        msg = random.choice(PLAY_MESSAGES).format(cat=cat["name"], toy=toy)

        happiness_gain = random.randint(8, 15)
        xp_gain = random.randint(3, 7)
        old_xp = cat["xp"]

        cat["happiness"] = min(100, cat["happiness"] + happiness_gain)
        cat["xp"] += xp_gain

        await self.config.guild(ctx.guild).cat.set(cat)
        await self._set_cooldown(ctx.author, "play")
        await self._add_leaderboard(ctx.guild, ctx.author.id, "play", xp_gain)

        stat_msg = f"😸 Happiness: +{happiness_gain} | ⭐ XP: +{xp_gain}"
        await self._handle_stage_evolution(ctx, cat, old_xp, msg, stat_msg)

    @cat_group.command(name="groom")
    @commands.guild_only()
    async def cat_groom(self, ctx: commands.Context):
        """Groom the server's cat. ✨"""
        cat = await self._ensure_cat(ctx)
        if cat is None:
            return

        remaining = await self._check_cooldown(ctx.author, "groom")
        if remaining:
            mins, secs = divmod(remaining, 60)
            await ctx.send(f"⏳ You can groom {cat['name']} again in **{mins}m {secs}s**.")
            return

        msg = random.choice(GROOM_MESSAGES).format(cat=cat["name"])

        clean_gain = random.randint(10, 18)
        xp_gain = random.randint(2, 5)
        old_xp = cat["xp"]

        cat["cleanliness"] = min(100, cat["cleanliness"] + clean_gain)
        cat["xp"] += xp_gain

        await self.config.guild(ctx.guild).cat.set(cat)
        await self._set_cooldown(ctx.author, "groom")
        await self._add_leaderboard(ctx.guild, ctx.author.id, "groom", xp_gain)

        stat_msg = f"✨ Cleanliness: +{clean_gain} | ⭐ XP: +{xp_gain}"
        await self._handle_stage_evolution(ctx, cat, old_xp, msg, stat_msg)

    @cat_group.command(name="vet")
    @commands.guild_only()
    async def cat_vet(self, ctx: commands.Context):
        """Take the cat to the vet. 🏥"""
        cat = await self._ensure_cat(ctx)
        if cat is None:
            return

        remaining = await self._check_cooldown(ctx.author, "vet")
        if remaining:
            mins, secs = divmod(remaining, 60)
            await ctx.send(f"⏳ You can take {cat['name']} to the vet again in **{mins}m {secs}s**.")
            return

        msg = random.choice(VET_MESSAGES).format(cat=cat["name"])

        health_gain = random.randint(12, 20)
        xp_gain = random.randint(4, 8)
        old_xp = cat["xp"]

        cat["health"] = min(100, cat["health"] + health_gain)
        cat["xp"] += xp_gain

        await self.config.guild(ctx.guild).cat.set(cat)
        await self._set_cooldown(ctx.author, "vet")
        await self._add_leaderboard(ctx.guild, ctx.author.id, "vet", xp_gain)

        stat_msg = f"❤️ Health: +{health_gain} | ⭐ XP: +{xp_gain}"
        await self._handle_stage_evolution(ctx, cat, old_xp, msg, stat_msg)

    @cat_group.command(name="train")
    @commands.guild_only()
    async def cat_train(self, ctx: commands.Context):
        """Try to teach the cat a new trick. 🎓"""
        cat = await self._ensure_cat(ctx)
        if cat is None:
            return

        remaining = await self._check_cooldown(ctx.author, "train")
        if remaining:
            mins, secs = divmod(remaining, 60)
            await ctx.send(f"⏳ You can train {cat['name']} again in **{mins}m {secs}s**.")
            return

        learned = set(cat.get("tricks", []))
        available = [t for t in AVAILABLE_TRICKS if t["name"] not in learned and cat["xp"] >= t["xp_required"]]

        if not available:
            locked = [t for t in AVAILABLE_TRICKS if t["name"] not in learned and cat["xp"] < t["xp_required"]]
            if locked:
                next_trick = locked[0]
                await ctx.send(
                    f"🎓 {cat['name']} has learned all available tricks!\n"
                    f"Next trick **{next_trick['name']}** unlocks at **{next_trick['xp_required']} XP** "
                    f"(currently {cat['xp']} XP)."
                )
            else:
                await ctx.send(f"🎓 {cat['name']} has learned ALL the tricks! What a prodigy! 🏆")
            return

        trick = available[0]
        success_chance = max(0.3, 1.0 - (trick["difficulty"] * 0.08))
        success = random.random() < success_chance

        xp_gain = random.randint(5, 10)
        old_xp = cat["xp"]
        cat["xp"] += xp_gain

        if success:
            cat["tricks"] = cat.get("tricks", []) + [trick["name"]]
            msg = random.choice(TRAIN_SUCCESS).format(cat=cat["name"], trick=trick["name"])
            xp_gain += trick["difficulty"] * 3
        else:
            msg = random.choice(TRAIN_FAIL).format(cat=cat["name"], trick=trick["name"])

        await self.config.guild(ctx.guild).cat.set(cat)
        await self._set_cooldown(ctx.author, "train")
        await self._add_leaderboard(ctx.guild, ctx.author.id, "train", xp_gain)

        stat_msg = f"⭐ XP: +{xp_gain}"
        await self._handle_stage_evolution(ctx, cat, old_xp, msg, stat_msg)

    @cat_group.command(name="tricks")
    @commands.guild_only()
    async def cat_tricks(self, ctx: commands.Context):
        """See all tricks and which ones the cat has learned."""
        cat = await self._ensure_cat(ctx)
        if cat is None:
            return

        learned = set(cat.get("tricks", []))
        lines = []
        for trick in AVAILABLE_TRICKS:
            if trick["name"] in learned:
                status = "✅"
            elif cat["xp"] >= trick["xp_required"]:
                status = "📖"
            else:
                status = "🔒"
            lines.append(f"{status} **{trick['name']}** (requires {trick['xp_required']} XP)")

        embed = discord.Embed(
            title=f"🎓 {cat['name']}'s Trick Book",
            description="\n".join(lines),
            color=discord.Color.purple(),
        )
        embed.set_footer(text="✅ = Learned | 📖 = Ready to learn | 🔒 = Locked")

        stage = self._get_life_stage(cat["xp"])
        await self._send_with_gif(ctx, embed, stage["name"])

    @cat_group.command(name="leaderboard", aliases=["lb"])
    @commands.guild_only()
    async def cat_leaderboard(self, ctx: commands.Context):
        """See who's taken the best care of the cat! 🏆"""
        cat = await self._ensure_cat(ctx)
        if cat is None:
            return

        lb_data = await self.config.guild(ctx.guild).leaderboard()
        if not lb_data:
            await ctx.send("No one has interacted with the cat yet! Be the first!")
            return

        sorted_lb = sorted(lb_data.items(), key=lambda x: x[1].get("total", 0), reverse=True)

        lines = []
        medals = ["🥇", "🥈", "🥉"]
        for i, (user_id, data) in enumerate(sorted_lb[:10]):
            medal = medals[i] if i < 3 else f"**{i + 1}.**"
            member = ctx.guild.get_member(int(user_id))
            name = member.display_name if member else f"User {user_id}"
            total = data.get("total", 0)
            breakdown = (
                f"🍗{data.get('feed', 0)} "
                f"🎾{data.get('play', 0)} "
                f"✨{data.get('groom', 0)} "
                f"🏥{data.get('vet', 0)} "
                f"🎓{data.get('train', 0)}"
            )
            lines.append(f"{medal} **{name}** — {total} pts\n　{breakdown}")

        embed = discord.Embed(
            title=f"🏆 {cat['name']}'s Best Caretakers",
            description="\n".join(lines),
            color=discord.Color.gold(),
        )

        stage = self._get_life_stage(cat["xp"])
        await self._send_with_gif(ctx, embed, stage["name"])

    @cat_group.command(name="rename")
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def cat_rename(self, ctx: commands.Context, *, new_name: str):
        """Rename the server's cat. Admins only."""
        cat = await self._ensure_cat(ctx)
        if cat is None:
            return

        if len(new_name) > 32:
            await ctx.send("That name is too long! Keep it under 32 characters.")
            return

        old_name = cat["name"]
        cat["name"] = new_name
        await self.config.guild(ctx.guild).cat.set(cat)
        await ctx.send(f"✏️ **{old_name}** is now known as **{new_name}**!")

    @cat_group.command(name="release")
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def cat_release(self, ctx: commands.Context):
        """Release the server's cat. This cannot be undone! Admins only."""
        cat = await self._ensure_cat(ctx)
        if cat is None:
            return

        await ctx.send(
            f"⚠️ Are you sure you want to release **{cat['name']}**? "
            "This will delete all progress and leaderboard data!\n"
            "Type `yes` to confirm or anything else to cancel."
        )

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            msg = await self.bot.wait_for("message", check=check, timeout=30.0)
        except asyncio.TimeoutError:
            await ctx.send("Release cancelled — timed out.")
            return

        if msg.content.lower() == "yes":
            await self.config.guild(ctx.guild).cat.set(None)
            await self.config.guild(ctx.guild).leaderboard.set({})
            await ctx.send(
                f"😿 **{cat['name']}** has been released into the wild. "
                "They'll remember you fondly.\n"
                "Use `[p]cat adopt` to adopt a new cat!"
            )
        else:
            await ctx.send("Release cancelled. The cat stays! 🎉")

    @cat_group.command(name="art")
    @commands.guild_only()
    async def cat_art(self, ctx: commands.Context):
        """Show the cat's pixel art portrait (full size)."""
        cat = await self._ensure_cat(ctx)
        if cat is None:
            return

        stage = self._get_life_stage(cat["xp"])
        gif_path = self._get_cat_gif(stage["name"])

        if gif_path.exists():
            file = discord.File(str(gif_path), filename=f"{stage['name']}.gif")
            embed = discord.Embed(
                title=f"{stage['label']} {cat['name']}",
                color=discord.Color.from_rgb(255, 183, 77),
            )
            embed.set_image(url=f"attachment://{stage['name']}.gif")
            await ctx.send(embed=embed, file=file)
        else:
            await ctx.send(f"**{cat['name']}** — {stage['label']}")
