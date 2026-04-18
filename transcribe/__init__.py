from .transcribe import Transcribe


async def setup(bot):
    await bot.add_cog(Transcribe(bot))
