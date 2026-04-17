from .loveconfessions import LoveConfessions

async def setup(bot):
    await bot.add_cog(LoveConfessions(bot))