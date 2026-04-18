from .race import Race


async def setup(bot):
    cog = Race(bot)
    await bot.add_cog(cog)
