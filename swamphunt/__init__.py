from .swamphunt import SwampHunt


async def setup(bot):
    await bot.add_cog(SwampHunt(bot))