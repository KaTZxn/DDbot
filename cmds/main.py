import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random


class Main(Cog_Extension):

    @commands.command()
    async def 躝(self, ctx):
        await ctx.send('躝啦屌你老母')

    @commands.command()
    async def hi(self, ctx):
        await ctx.send('屌你老母')

    @commands.command()
    async def car(self, ctx, msg):
        link = ("https://nhentai.net/g/" + str(msg))
        await ctx.send(link)

    @commands.command()
    async def randomcar(self, ctx):
        num = random.randint(1, 370000)
        link = ("https://nhentai.net/g/" + str(num))
        await ctx.send(link)

    @commands.command()
    async def 屌(self, ctx, msg):
        if '@' in msg:
            await ctx.send(msg+'屌你')
        else:
            await ctx.send('你想屌邊個啊屌你')

    @commands.command()
    async def Aguis(self, ctx):
        await ctx.send('最愛芝娃娃')


def setup(bot):
    bot.add_cog(Main(bot))
