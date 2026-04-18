from .moodmusic import MoodMusic

async def setup(bot):
    await bot.add_cog(MoodMusic(bot))
