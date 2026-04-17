from .chainreaction import ChainReaction

__red_end_user_data_statement__ = (
    "This cog stores user IDs for active games and per-user stats (wins, games played, eliminations)."
)

async def setup(bot):
    await bot.add_cog(ChainReaction(bot))