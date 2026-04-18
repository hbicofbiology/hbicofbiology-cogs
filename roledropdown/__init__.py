from .roledropdown import RoleDropdown


async def setup(bot):
    await bot.add_cog(RoleDropdown(bot))
