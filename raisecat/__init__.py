from .raisecat import RaiseCat


async def setup(bot):
    await bot.add_cog(RaiseCat(bot))
