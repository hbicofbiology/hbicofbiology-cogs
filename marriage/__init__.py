from .marriage import Marriage

async def setup(bot):
    await bot.add_cog(Marriage(bot))