import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

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

    @commands.command()
    async def addGay(self, ctx, msg):
        with open('./gayList.json') as f:
            data = json.load(f)
            data["gay"].append(msg)
            json.dump(data, f, indent=4)

        await ctx.send('{name}而家都係死gay佬'.format(name=msg))

    @commands.command()
    async def removeGay(self, ctx, msg):
        with open('./gayList.json') as f:
            data = json.load(f)
            for index in data.gay:
                if msg == data.gay[index]:
                    del data.gay[index];
                    await ctx.send('{name}而家唔係死gay佬啦...'.format(name=msg))
        await ctx.send('{name}本來就唔係死gay佬'.format(name=msg))


def setup(bot):
    bot.add_cog(Main(bot))
