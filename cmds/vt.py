import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Vt(Cog_Extension):
    @commands.command()
    async def test(self, ctx):
        await ctx.send('屌你老母')


def setup(bot):
    bot.add_cog(Vt(bot))
