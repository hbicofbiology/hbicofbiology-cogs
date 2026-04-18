from .tarot import Tarot

async def setup(bot):
    await bot.add_cog(Tarot(bot))

