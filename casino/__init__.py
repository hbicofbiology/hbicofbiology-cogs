from .casino import Casino


async def setup(bot):
    cog = Casino(bot)
    await bot.add_cog(cog)
