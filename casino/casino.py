# Casino Cog for Red-DiscordBot V3
# Inspired by Redjumpman's original Casino cog (Jumper-Plugins)
# Recreated from scratch for modern Red V3 compatibility

import asyncio
import random
import time
import logging
from datetime import datetime, timezone
from typing import Optional, Literal

import discord
from redbot.core import bank, commands, Config
from redbot.core.errors import BalanceTooHigh
from redbot.core.utils.chat_formatting import box, humanize_number

__version__ = "1.0.0"
__author__ = "hbicofbiology (inspired by Redjumpman)"

log = logging.getLogger("red.casino")

# ---------------------------------------------------------------------------
# Card helpers shared by Blackjack & War
# ---------------------------------------------------------------------------

SUITS = ["\u2660", "\u2665", "\u2666", "\u2663"]  # ♠♥♦♣
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
RANK_VALUES_BJ = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
    "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11,
}
RANK_VALUES_WAR = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
    "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14,
}


def new_deck(num_decks: int = 1) -> list:
    deck = [(rank, suit) for suit in SUITS for rank in RANKS] * num_decks
    random.shuffle(deck)
    return deck


def card_str(card: tuple) -> str:
    return f"{card[1]} {card[0]}"


def hand_str(hand: list) -> str:
    return "  ".join(card_str(c) for c in hand)


def bj_value(hand: list) -> int:
    total = sum(RANK_VALUES_BJ[c[0]] for c in hand)
    aces = sum(1 for c in hand if c[0] == "A")
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total


# ---------------------------------------------------------------------------
# Default game settings
# ---------------------------------------------------------------------------

DEFAULT_GAMES = {
    "Coin": {"min": 50, "max": 10000, "multiplier": 1.5, "cooldown": 5, "access": 0, "open": True},
    "Cups": {"min": 50, "max": 10000, "multiplier": 2.5, "cooldown": 5, "access": 0, "open": True},
    "Dice": {"min": 50, "max": 10000, "multiplier": 2.0, "cooldown": 5, "access": 0, "open": True},
    "Hilo": {"min": 50, "max": 10000, "multiplier": 2.0, "cooldown": 5, "access": 0, "open": True},
    "Craps": {"min": 50, "max": 10000, "multiplier": 2.0, "cooldown": 5, "access": 0, "open": True},
    "Blackjack": {"min": 50, "max": 10000, "multiplier": 2.0, "cooldown": 5, "access": 0, "open": True},
    "War": {"min": 50, "max": 10000, "multiplier": 2.0, "cooldown": 5, "access": 0, "open": True},
    "Allin": {"min": 0, "max": 0, "multiplier": 2.0, "cooldown": 30, "access": 0, "open": True},
    "Double": {"min": 50, "max": 10000, "multiplier": 2.0, "cooldown": 5, "access": 0, "open": True},
}

DEFAULT_GUILD = {
    "casino_name": "Casino",
    "games": DEFAULT_GAMES,
    "payout_limit": 0,
    "payout_limit_on": False,
}

DEFAULT_MEMBER = {
    "wins": 0,
    "losses": 0,
    "total_wagered": 0,
    "total_won": 0,
    "cooldowns": {},
}


class Casino(commands.Cog):
    """A fully featured casino with multiple games using Red's economy system.

    Inspired by Redjumpman's original Casino cog.
    """

    __version__ = __version__
    __author__ = __author__

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=5765232489, force_registration=True)
        self.config.register_guild(**DEFAULT_GUILD)
        self.config.register_member(**DEFAULT_MEMBER)
        # In-memory deck cache per guild for card games
        self._decks: dict[int, list] = {}

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _get_deck(self, guild_id: int) -> list:
        if guild_id not in self._decks or len(self._decks[guild_id]) < 10:
            self._decks[guild_id] = new_deck()
        return self._decks[guild_id]

    def _draw(self, guild_id: int, count: int = 1) -> list:
        deck = self._get_deck(guild_id)
        drawn = deck[:count]
        self._decks[guild_id] = deck[count:]
        return drawn

    async def _check_bet(self, ctx, game_name: str, bet: int) -> Optional[dict]:
        """Validate a bet.  Returns game settings dict or None (and sends error)."""
        games = await self.config.guild(ctx.guild).games()
        game = games.get(game_name)
        if not game:
            await ctx.send(f"Game **{game_name}** not found.")
            return None
        if not game["open"]:
            await ctx.send(f"**{game_name}** is currently closed.")
            return None
        if game_name != "Allin":
            if bet < game["min"]:
                await ctx.send(f"Minimum bet for **{game_name}** is **{humanize_number(game['min'])}**.")
                return None
            if bet > game["max"]:
                await ctx.send(f"Maximum bet for **{game_name}** is **{humanize_number(game['max'])}**.")
                return None
        if not await bank.can_spend(ctx.author, bet):
            bal = await bank.get_balance(ctx.author)
            await ctx.send(f"You don't have enough credits. Your balance is **{humanize_number(bal)}**.")
            return None
        # Cooldown check
        cooldowns = await self.config.member(ctx.author).cooldowns()
        last_played = cooldowns.get(game_name, 0)
        elapsed = time.time() - last_played
        if elapsed < game["cooldown"]:
            remaining = int(game["cooldown"] - elapsed)
            await ctx.send(f"**{game_name}** is on cooldown. Try again in **{remaining}s**.")
            return None
        return game

    async def _apply_result(self, ctx, game_name: str, bet: int, won: bool, payout: int):
        """Withdraw bet, deposit winnings, update stats and cooldown."""
        member_conf = self.config.member(ctx.author)

        # Always withdraw the bet first
        await bank.withdraw_credits(ctx.author, bet)

        if won and payout > 0:
            payout_limit_on = await self.config.guild(ctx.guild).payout_limit_on()
            payout_limit = await self.config.guild(ctx.guild).payout_limit()
            if payout_limit_on and payout_limit > 0 and payout > payout_limit:
                # Withhold — store as "pending" (simplified: just cap it)
                payout = payout_limit

            try:
                await bank.deposit_credits(ctx.author, payout)
            except BalanceTooHigh as e:
                await bank.set_balance(ctx.author, e.max_balance)

        # Stats
        async with member_conf.all() as data:
            if won:
                data["wins"] = data.get("wins", 0) + 1
                data["total_won"] = data.get("total_won", 0) + payout
            else:
                data["losses"] = data.get("losses", 0) + 1
            data["total_wagered"] = data.get("total_wagered", 0) + bet
            data.setdefault("cooldowns", {})[game_name] = time.time()

    def _embed(self, title: str, description: str, colour: discord.Colour = discord.Colour.gold()) -> discord.Embed:
        return discord.Embed(title=title, description=description, colour=colour)

    # ==================================================================
    #  GAMES
    # ==================================================================

    # --- Coin Flip ---------------------------------------------------

    @commands.command()
    @commands.guild_only()
    async def coin(self, ctx, bet: int, choice: str):
        """Flip a coin! Pick heads or tails.

        Example: `[p]coin 100 heads`
        """
        choice = choice.lower()
        if choice not in ("heads", "tails", "h", "t"):
            return await ctx.send("Pick **heads** or **tails** (or h/t).")
        game = await self._check_bet(ctx, "Coin", bet)
        if not game:
            return

        result = random.choice(["heads", "tails"])
        win = (choice[0] == result[0])
        payout = int(bet * game["multiplier"]) if win else 0
        net = payout - bet if win else -bet

        await self._apply_result(ctx, "Coin", bet, win, payout)

        emoji = "\U0001fa99"  # 🪙
        colour = discord.Colour.green() if win else discord.Colour.red()
        e = self._embed(
            f"{emoji} Coin Flip",
            f"The coin landed on **{result}**!",
            colour,
        )
        if win:
            e.add_field(name="Result", value=f"You won **{humanize_number(payout)}** credits!", inline=False)
        else:
            e.add_field(name="Result", value=f"You lost **{humanize_number(bet)}** credits.", inline=False)
        e.set_footer(text=f"Bet: {humanize_number(bet)} | Net: {'+' if net > 0 else ''}{humanize_number(net)}")
        await ctx.send(embed=e)

    # --- Cups --------------------------------------------------------

    @commands.command()
    @commands.guild_only()
    async def cups(self, ctx, bet: int, cup: int):
        """Guess which cup (1, 2, or 3) hides the coin.

        Example: `[p]cups 100 2`
        """
        if cup not in (1, 2, 3):
            return await ctx.send("Pick cup **1**, **2**, or **3**.")
        game = await self._check_bet(ctx, "Cups", bet)
        if not game:
            return

        answer = random.randint(1, 3)
        win = cup == answer
        payout = int(bet * game["multiplier"]) if win else 0
        net = payout - bet if win else -bet

        await self._apply_result(ctx, "Cups", bet, win, payout)

        cups_display = ["🔵", "🔵", "🔵"]
        cups_display[answer - 1] = "🪙"
        display = "  ".join(f"`{i+1}` {c}" for i, c in enumerate(cups_display))

        colour = discord.Colour.green() if win else discord.Colour.red()
        e = self._embed("🥤 Cups", f"{display}\n\nThe coin was under cup **{answer}**!", colour)
        if win:
            e.add_field(name="Result", value=f"You won **{humanize_number(payout)}** credits!", inline=False)
        else:
            e.add_field(name="Result", value=f"You lost **{humanize_number(bet)}** credits.", inline=False)
        e.set_footer(text=f"Bet: {humanize_number(bet)} | Net: {'+' if net > 0 else ''}{humanize_number(net)}")
        await ctx.send(embed=e)

    # --- Dice --------------------------------------------------------

    @commands.command()
    @commands.guild_only()
    async def dice(self, ctx, bet: int):
        """Roll two dice. Win on 2, 7, 11, or 12.

        Example: `[p]dice 100`
        """
        game = await self._check_bet(ctx, "Dice", bet)
        if not game:
            return

        d1, d2 = random.randint(1, 6), random.randint(1, 6)
        total = d1 + d2
        win = total in (2, 7, 11, 12)
        payout = int(bet * game["multiplier"]) if win else 0
        net = payout - bet if win else -bet

        await self._apply_result(ctx, "Dice", bet, win, payout)

        colour = discord.Colour.green() if win else discord.Colour.red()
        e = self._embed("🎲 Dice", f"You rolled **{d1}** + **{d2}** = **{total}**", colour)
        e.add_field(name="Winning rolls", value="2, 7, 11, 12", inline=True)
        if win:
            e.add_field(name="Result", value=f"You won **{humanize_number(payout)}** credits!", inline=False)
        else:
            e.add_field(name="Result", value=f"You lost **{humanize_number(bet)}** credits.", inline=False)
        e.set_footer(text=f"Bet: {humanize_number(bet)} | Net: {'+' if net > 0 else ''}{humanize_number(net)}")
        await ctx.send(embed=e)

    # --- Hi-Lo -------------------------------------------------------

    @commands.command(aliases=["hl"])
    @commands.guild_only()
    async def hilo(self, ctx, bet: int, choice: str):
        """Pick High (8-12), Low (2-6), or Seven (7). Seven pays extra!

        Choices: high/hi, low/lo, seven/7
        Example: `[p]hilo 100 high`
        """
        choice = choice.lower()
        mapping = {"high": "high", "hi": "high", "low": "low", "lo": "low", "seven": "seven", "7": "seven"}
        pick = mapping.get(choice)
        if not pick:
            return await ctx.send("Choose **high** (hi), **low** (lo), or **seven** (7).")
        game = await self._check_bet(ctx, "Hilo", bet)
        if not game:
            return

        d1, d2 = random.randint(1, 6), random.randint(1, 6)
        total = d1 + d2

        if total < 7:
            outcome = "low"
        elif total > 7:
            outcome = "high"
        else:
            outcome = "seven"

        win = pick == outcome
        if win and pick == "seven":
            payout = int(bet * (game["multiplier"] + 2))
        elif win:
            payout = int(bet * game["multiplier"])
        else:
            payout = 0
        net = payout - bet if win else -bet

        await self._apply_result(ctx, "Hilo", bet, win, payout)

        colour = discord.Colour.green() if win else discord.Colour.red()
        e = self._embed(
            "📊 Hi-Lo",
            f"You rolled **{d1}** + **{d2}** = **{total}** ({outcome.title()})\nYou picked **{pick.title()}**.",
            colour,
        )
        if win:
            e.add_field(name="Result", value=f"You won **{humanize_number(payout)}** credits!", inline=False)
        else:
            e.add_field(name="Result", value=f"You lost **{humanize_number(bet)}** credits.", inline=False)
        e.set_footer(text=f"Bet: {humanize_number(bet)} | Net: {'+' if net > 0 else ''}{humanize_number(net)}")
        await ctx.send(embed=e)

    # --- Craps -------------------------------------------------------

    @commands.command()
    @commands.guild_only()
    async def craps(self, ctx, bet: int):
        """Play a simplified craps (pass line bet).

        Come-out roll: 7 pays 7x, 11 wins at normal multiplier, 2/3/12 loses.
        Otherwise a point is set — keep rolling until you hit your point (win) or 7 (lose).

        Example: `[p]craps 200`
        """
        game = await self._check_bet(ctx, "Craps", bet)
        if not game:
            return

        d1, d2 = random.randint(1, 6), random.randint(1, 6)
        total = d1 + d2

        lines = [f"**Come-out roll:** {d1} + {d2} = **{total}**"]

        if total == 7:
            win = True
            payout = bet * 7
            lines.append("🎰 **SEVEN!** You win 7x your bet!")
        elif total == 11:
            win = True
            payout = int(bet * game["multiplier"])
            lines.append("✨ **Eleven!** You win!")
        elif total in (2, 3, 12):
            win = False
            payout = 0
            lines.append("💀 **Craps!** You lose.")
        else:
            point = total
            lines.append(f"📍 **Point is set at {point}.** Rolling...")
            win = None
            for _ in range(20):  # safety limit
                await asyncio.sleep(0.3)
                rd1, rd2 = random.randint(1, 6), random.randint(1, 6)
                rtotal = rd1 + rd2
                lines.append(f"Roll: {rd1} + {rd2} = **{rtotal}**")
                if rtotal == point:
                    win = True
                    payout = int(bet * game["multiplier"])
                    lines.append(f"🎯 **Hit the point!** You win!")
                    break
                elif rtotal == 7:
                    win = False
                    payout = 0
                    lines.append("💀 **Seven out!** You lose.")
                    break
            if win is None:
                win = False
                payout = 0
                lines.append("Took too long — you lose.")

        net = payout - bet if win else -bet
        await self._apply_result(ctx, "Craps", bet, win, payout)

        colour = discord.Colour.green() if win else discord.Colour.red()
        e = self._embed("🎲 Craps", "\n".join(lines), colour)
        e.set_footer(text=f"Bet: {humanize_number(bet)} | Net: {'+' if net > 0 else ''}{humanize_number(net)}")
        await ctx.send(embed=e)

    # --- Blackjack ---------------------------------------------------

    @commands.command(name="blackjack", aliases=["bj", "21"])
    @commands.guild_only()
    async def blackjack(self, ctx, bet: int):
        """Play blackjack against the dealer.

        Hit, stand, or double down. Dealer stands on 17.
        Example: `[p]blackjack 200`
        """
        game = await self._check_bet(ctx, "Blackjack", bet)
        if not game:
            return

        gid = ctx.guild.id
        player_hand = self._draw(gid, 2)
        dealer_hand = self._draw(gid, 2)
        doubled = False

        def make_embed(reveal_dealer=False, result_text=None):
            pv = bj_value(player_hand)
            if reveal_dealer:
                dv = bj_value(dealer_hand)
                dealer_display = hand_str(dealer_hand) + f"  (Value: {dv})"
            else:
                dealer_display = card_str(dealer_hand[0]) + "  🂠"
            player_display = hand_str(player_hand) + f"  (Value: {pv})"

            e = discord.Embed(title="🃏 Blackjack", colour=discord.Colour.gold())
            e.add_field(name="Your Hand", value=player_display, inline=False)
            e.add_field(name="Dealer", value=dealer_display, inline=False)
            if result_text:
                e.add_field(name="Result", value=result_text, inline=False)
            if not reveal_dealer and not result_text:
                e.set_footer(text="Type: hit, stand, or double")
            return e

        # Check natural blackjack
        if bj_value(player_hand) == 21:
            payout = int(bet * 2.5)
            net = payout - bet
            await self._apply_result(ctx, "Blackjack", bet, True, payout)
            e = make_embed(reveal_dealer=True, result_text=f"🎰 **BLACKJACK!** You win **{humanize_number(payout)}**!")
            e.colour = discord.Colour.green()
            e.set_footer(text=f"Bet: {humanize_number(bet)} | Net: +{humanize_number(net)}")
            return await ctx.send(embed=e)

        msg = await ctx.send(embed=make_embed())

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ("hit", "h", "stand", "s", "double", "d")

        while True:
            try:
                resp = await self.bot.wait_for("message", timeout=60.0, check=check)
            except asyncio.TimeoutError:
                await self._apply_result(ctx, "Blackjack", bet, False, 0)
                return await ctx.send(embed=make_embed(reveal_dealer=True, result_text="⏰ Timed out — you lose."))

            action = resp.content.lower()

            if action in ("double", "d"):
                if len(player_hand) != 2:
                    await ctx.send("You can only double down on your first action.", delete_after=5)
                    continue
                if not await bank.can_spend(ctx.author, bet):
                    await ctx.send("You can't afford to double down.", delete_after=5)
                    continue
                doubled = True
                bet *= 2
                player_hand.extend(self._draw(gid, 1))
                # After doubling you get exactly one card then stand
                break
            elif action in ("hit", "h"):
                player_hand.extend(self._draw(gid, 1))
                if bj_value(player_hand) > 21:
                    await self._apply_result(ctx, "Blackjack", bet, False, 0)
                    e = make_embed(reveal_dealer=True, result_text=f"💥 **Bust!** You lost **{humanize_number(bet)}**.")
                    e.colour = discord.Colour.red()
                    e.set_footer(text=f"Bet: {humanize_number(bet)} | Net: -{humanize_number(bet)}")
                    return await ctx.send(embed=e)
                try:
                    await msg.edit(embed=make_embed())
                except discord.HTTPException:
                    msg = await ctx.send(embed=make_embed())
            elif action in ("stand", "s"):
                break

        # Dealer draws
        while bj_value(dealer_hand) < 17:
            dealer_hand.extend(self._draw(gid, 1))

        pv = bj_value(player_hand)
        dv = bj_value(dealer_hand)

        if dv > 21:
            result = "win"
        elif pv > dv:
            result = "win"
        elif pv == dv:
            result = "push"
        else:
            result = "lose"

        if result == "win":
            payout = int(bet * game["multiplier"])
            net = payout - bet
            await self._apply_result(ctx, "Blackjack", bet, True, payout)
            text = f"🎉 You win **{humanize_number(payout)}** credits!"
            colour = discord.Colour.green()
        elif result == "push":
            # Return bet
            await self._apply_result(ctx, "Blackjack", bet, True, bet)
            net = 0
            text = "🤝 **Push!** Bet returned."
            colour = discord.Colour.blue()
        else:
            await self._apply_result(ctx, "Blackjack", bet, False, 0)
            net = -bet
            text = f"💔 Dealer wins. You lost **{humanize_number(bet)}** credits."
            colour = discord.Colour.red()

        e = make_embed(reveal_dealer=True, result_text=text)
        e.colour = colour
        e.set_footer(text=f"Bet: {humanize_number(bet)} | Net: {'+' if net > 0 else ''}{humanize_number(net)}")
        await ctx.send(embed=e)

    # --- War ---------------------------------------------------------

    @commands.command()
    @commands.guild_only()
    async def war(self, ctx, bet: int):
        """Play War — your card vs the dealer's.

        Higher card wins. Tied? Go to war (double or nothing)!
        Example: `[p]war 100`
        """
        game = await self._check_bet(ctx, "War", bet)
        if not game:
            return

        gid = ctx.guild.id
        pc = self._draw(gid, 1)[0]
        dc = self._draw(gid, 1)[0]

        pv = RANK_VALUES_WAR[pc[0]]
        dv = RANK_VALUES_WAR[dc[0]]

        desc = f"Your card: **{card_str(pc)}**\nDealer card: **{card_str(dc)}**"

        if pv > dv:
            win = True
        elif pv < dv:
            win = False
        else:
            # War! Draw again
            pc2 = self._draw(gid, 1)[0]
            dc2 = self._draw(gid, 1)[0]
            pv2 = RANK_VALUES_WAR[pc2[0]]
            dv2 = RANK_VALUES_WAR[dc2[0]]
            desc += f"\n\n⚔️ **WAR!**\nYour card: **{card_str(pc2)}**\nDealer card: **{card_str(dc2)}**"
            win = pv2 >= dv2  # Player wins ties in war round

        payout = int(bet * game["multiplier"]) if win else 0
        net = payout - bet if win else -bet
        await self._apply_result(ctx, "War", bet, win, payout)

        colour = discord.Colour.green() if win else discord.Colour.red()
        e = self._embed("⚔️ War", desc, colour)
        if win:
            e.add_field(name="Result", value=f"You won **{humanize_number(payout)}** credits!", inline=False)
        else:
            e.add_field(name="Result", value=f"You lost **{humanize_number(bet)}** credits.", inline=False)
        e.set_footer(text=f"Bet: {humanize_number(bet)} | Net: {'+' if net > 0 else ''}{humanize_number(net)}")
        await ctx.send(embed=e)

    # --- All-In ------------------------------------------------------

    @commands.command()
    @commands.guild_only()
    async def allin(self, ctx, multiplier: int):
        """Bet your ENTIRE balance for a chance at big winnings.

        The higher the multiplier, the lower your odds (1 in multiplier+1 chance).
        Example: `[p]allin 3`
        """
        if multiplier < 2:
            return await ctx.send("Multiplier must be **2** or higher.")
        game = await self._check_bet(ctx, "Allin", 0)
        if not game:
            return

        bet = await bank.get_balance(ctx.author)
        if bet <= 0:
            return await ctx.send("You're broke!")

        # 1 in (multiplier + 1) chance
        roll = random.randint(0, multiplier)
        win = roll == 0
        payout = bet * multiplier if win else 0
        net = payout - bet if win else -bet

        await self._apply_result(ctx, "Allin", bet, win, payout)

        colour = discord.Colour.green() if win else discord.Colour.red()
        e = self._embed("🎰 All-In", f"Multiplier: **{multiplier}x** (1 in {multiplier + 1} chance)", colour)
        if win:
            e.add_field(name="Result", value=f"🎉 **JACKPOT!** You won **{humanize_number(payout)}** credits!", inline=False)
        else:
            e.add_field(name="Result", value=f"💸 You lost everything (**{humanize_number(bet)}** credits).", inline=False)
        e.set_footer(text=f"Wagered: {humanize_number(bet)}")
        await ctx.send(embed=e)

    # --- Double or Nothing -------------------------------------------

    @commands.command(aliases=["don", "x2"])
    @commands.guild_only()
    async def double(self, ctx, bet: int):
        """Double or nothing — keep doubling until you cash out or bust.

        Each round is a 55/45 coin flip. Type `double` to keep going or `cash` to collect.
        Example: `[p]double 100`
        """
        game = await self._check_bet(ctx, "Double", bet)
        if not game:
            return

        # Withdraw initial bet
        await bank.withdraw_credits(ctx.author, bet)
        current = bet
        rounds = 0

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ("double", "d", "cash", "c")

        while True:
            next_val = current * 2
            e = discord.Embed(title="💰 Double or Nothing", colour=discord.Colour.gold())
            e.add_field(name="Current Pot", value=f"**{humanize_number(current)}** credits", inline=False)
            e.add_field(name="Next Double", value=f"**{humanize_number(next_val)}** credits", inline=False)
            e.set_footer(text=f"Round {rounds + 1} | Type: double or cash")
            await ctx.send(embed=e)

            try:
                resp = await self.bot.wait_for("message", timeout=30.0, check=check)
            except asyncio.TimeoutError:
                # Auto cash out on timeout
                break

            if resp.content.lower() in ("cash", "c"):
                break

            # 55% chance to succeed each round
            if random.random() < 0.55:
                current *= 2
                rounds += 1
            else:
                # Bust!
                async with self.config.member(ctx.author).all() as data:
                    data["losses"] = data.get("losses", 0) + 1
                    data["total_wagered"] = data.get("total_wagered", 0) + bet
                    data.setdefault("cooldowns", {})["Double"] = time.time()

                e = discord.Embed(title="💰 Double or Nothing", colour=discord.Colour.red())
                e.add_field(name="💥 BUST!", value=f"You lost everything after **{rounds + 1}** rounds.", inline=False)
                e.set_footer(text=f"Original bet: {humanize_number(bet)}")
                return await ctx.send(embed=e)

        # Cash out
        try:
            await bank.deposit_credits(ctx.author, current)
        except BalanceTooHigh as exc:
            await bank.set_balance(ctx.author, exc.max_balance)

        net = current - bet
        async with self.config.member(ctx.author).all() as data:
            data["wins"] = data.get("wins", 0) + 1
            data["total_wagered"] = data.get("total_wagered", 0) + bet
            data["total_won"] = data.get("total_won", 0) + current
            data.setdefault("cooldowns", {})["Double"] = time.time()

        e = discord.Embed(title="💰 Double or Nothing", colour=discord.Colour.green())
        e.add_field(name="💵 Cashed Out!", value=f"You collected **{humanize_number(current)}** after **{rounds}** doubles!", inline=False)
        e.set_footer(text=f"Original bet: {humanize_number(bet)} | Profit: +{humanize_number(net)}")
        await ctx.send(embed=e)

    # ==================================================================
    #  USER COMMANDS (casino group)
    # ==================================================================

    @commands.group()
    @commands.guild_only()
    async def casino(self, ctx):
        """Casino information and settings."""
        pass

    @casino.command(name="info")
    async def casino_info(self, ctx):
        """Show casino games and their settings."""
        casino_name = await self.config.guild(ctx.guild).casino_name()
        games = await self.config.guild(ctx.guild).games()
        currency = await bank.get_currency_name(ctx.guild)

        e = discord.Embed(title=f"🎰 {casino_name}", colour=discord.Colour.gold())
        for name, g in sorted(games.items()):
            status = "✅ Open" if g["open"] else "❌ Closed"
            info = (
                f"Bet: {humanize_number(g['min'])}–{humanize_number(g['max'])} {currency}\n"
                f"Multiplier: {g['multiplier']}x | Cooldown: {g['cooldown']}s\n"
                f"Status: {status}"
            )
            if name == "Allin":
                info = f"Bet: Entire balance\nMultiplier: Variable | Cooldown: {g['cooldown']}s\nStatus: {status}"
            e.add_field(name=name, value=info, inline=True)
        e.set_footer(text=f"Casino v{__version__} | Use [p]help <game> for details")
        await ctx.send(embed=e)

    @casino.command(name="stats")
    async def casino_stats(self, ctx, user: Optional[discord.Member] = None):
        """Show your (or another user's) casino stats."""
        user = user or ctx.author
        data = await self.config.member(user).all()
        wins = data.get("wins", 0)
        losses = data.get("losses", 0)
        total_games = wins + losses
        win_rate = f"{(wins / total_games * 100):.1f}%" if total_games > 0 else "N/A"

        e = discord.Embed(title=f"📈 Stats for {user.display_name}", colour=discord.Colour.blue())
        e.add_field(name="Wins", value=humanize_number(wins), inline=True)
        e.add_field(name="Losses", value=humanize_number(losses), inline=True)
        e.add_field(name="Win Rate", value=win_rate, inline=True)
        e.add_field(name="Total Wagered", value=humanize_number(data.get("total_wagered", 0)), inline=True)
        e.add_field(name="Total Won", value=humanize_number(data.get("total_won", 0)), inline=True)
        net = data.get("total_won", 0) - data.get("total_wagered", 0)
        e.add_field(name="Net Profit", value=f"{'+' if net >= 0 else ''}{humanize_number(net)}", inline=True)
        await ctx.send(embed=e)

    @casino.command(name="version")
    async def casino_version(self, ctx):
        """Show the casino cog version."""
        await ctx.send(f"Casino v{__version__} by {__author__}")

    # ==================================================================
    #  ADMIN COMMANDS (casinoset group)
    # ==================================================================

    @commands.group()
    @commands.guild_only()
    @commands.admin_or_permissions(administrator=True)
    async def casinoset(self, ctx):
        """Configure casino settings."""
        pass

    @casinoset.command(name="name")
    async def set_name(self, ctx, *, name: str):
        """Set the casino name (max 30 chars)."""
        if len(name) > 30:
            return await ctx.send("Name must be 30 characters or fewer.")
        await self.config.guild(ctx.guild).casino_name.set(name)
        await ctx.send(f"Casino name set to **{name}**.")

    @casinoset.command(name="min")
    async def set_min(self, ctx, game: str, minimum: int):
        """Set the minimum bet for a game.

        Example: `[p]casinoset min blackjack 100`
        """
        game_title = game.title()
        async with self.config.guild(ctx.guild).games() as games:
            if game_title not in games:
                return await ctx.send(f"Game not found. Available: {', '.join(games.keys())}")
            games[game_title]["min"] = minimum
        await ctx.send(f"Minimum bet for **{game_title}** set to **{humanize_number(minimum)}**.")

    @casinoset.command(name="max")
    async def set_max(self, ctx, game: str, maximum: int):
        """Set the maximum bet for a game.

        Example: `[p]casinoset max blackjack 50000`
        """
        game_title = game.title()
        async with self.config.guild(ctx.guild).games() as games:
            if game_title not in games:
                return await ctx.send(f"Game not found. Available: {', '.join(games.keys())}")
            games[game_title]["max"] = maximum
        await ctx.send(f"Maximum bet for **{game_title}** set to **{humanize_number(maximum)}**.")

    @casinoset.command(name="multiplier")
    async def set_multiplier(self, ctx, game: str, multiplier: float):
        """Set the payout multiplier for a game.

        Example: `[p]casinoset multiplier coin 2.0`
        """
        if multiplier < 1.0:
            return await ctx.send("Multiplier must be at least 1.0.")
        game_title = game.title()
        async with self.config.guild(ctx.guild).games() as games:
            if game_title not in games:
                return await ctx.send(f"Game not found. Available: {', '.join(games.keys())}")
            games[game_title]["multiplier"] = multiplier
        await ctx.send(f"Multiplier for **{game_title}** set to **{multiplier}x**.")

    @casinoset.command(name="cooldown")
    async def set_cooldown(self, ctx, game: str, seconds: int):
        """Set the cooldown (in seconds) for a game.

        Example: `[p]casinoset cooldown blackjack 10`
        """
        if seconds < 0:
            return await ctx.send("Cooldown must be 0 or more.")
        game_title = game.title()
        async with self.config.guild(ctx.guild).games() as games:
            if game_title not in games:
                return await ctx.send(f"Game not found. Available: {', '.join(games.keys())}")
            games[game_title]["cooldown"] = seconds
        await ctx.send(f"Cooldown for **{game_title}** set to **{seconds}s**.")

    @casinoset.command(name="toggle")
    async def set_toggle(self, ctx, game: str):
        """Open or close a game.

        Example: `[p]casinoset toggle blackjack`
        """
        game_title = game.title()
        async with self.config.guild(ctx.guild).games() as games:
            if game_title not in games:
                return await ctx.send(f"Game not found. Available: {', '.join(games.keys())}")
            games[game_title]["open"] = not games[game_title]["open"]
            status = "opened" if games[game_title]["open"] else "closed"
        await ctx.send(f"**{game_title}** has been **{status}**.")

    @casinoset.command(name="payoutlimit")
    async def set_payout_limit(self, ctx, amount: int):
        """Set a maximum payout limit (0 to disable)."""
        await self.config.guild(ctx.guild).payout_limit.set(amount)
        if amount > 0:
            await self.config.guild(ctx.guild).payout_limit_on.set(True)
            await ctx.send(f"Payout limit set to **{humanize_number(amount)}**.")
        else:
            await self.config.guild(ctx.guild).payout_limit_on.set(False)
            await ctx.send("Payout limit disabled.")

    @casinoset.command(name="resetuser")
    async def reset_user(self, ctx, user: discord.Member):
        """Reset a user's casino stats and cooldowns."""
        await self.config.member(user).clear()
        await ctx.send(f"Casino data for **{user.display_name}** has been reset.")

    @casinoset.command(name="reset")
    async def reset_casino(self, ctx):
        """Reset all casino settings to defaults (keeps user data)."""
        await self.config.guild(ctx.guild).casino_name.set("Casino")
        await self.config.guild(ctx.guild).games.set(DEFAULT_GAMES)
        await self.config.guild(ctx.guild).payout_limit.set(0)
        await self.config.guild(ctx.guild).payout_limit_on.set(False)
        await ctx.send("Casino settings reset to defaults. User data preserved.")

    @casinoset.command(name="wipe")
    @commands.is_owner()
    async def wipe_casino(self, ctx):
        """⚠️ Wipe ALL casino data for this server (settings + user data)."""
        await ctx.send("⚠️ This will delete **all** casino data for this server. Type `yes` to confirm.")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            resp = await self.bot.wait_for("message", timeout=15.0, check=check)
        except asyncio.TimeoutError:
            return await ctx.send("Cancelled.")

        if resp.content.lower() != "yes":
            return await ctx.send("Cancelled.")

        await self.config.guild(ctx.guild).clear()
        await self.config.clear_all_members(ctx.guild)
        await ctx.send("All casino data for this server has been wiped.")

    # ------------------------------------------------------------------
    # Data deletion support
    # ------------------------------------------------------------------

    async def red_delete_data_for_user(
        self, *, requester: Literal["discord_deleted_user", "owner", "user", "user_strict"], user_id: int
    ):
        all_members = await self.config.all_members()
        for guild_id in all_members:
            await self.config.member_from_ids(guild_id, user_id).clear()
