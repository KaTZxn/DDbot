import discord
from discord.ext import commands
from discord.ext.commands.core import check
from core.classes import Cog_Extension
import random
import json
import math


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
        try:
            json_file = open("./cmds/gayList.json", "r")
            json_obj = json.load(json_file)
            json_file.close()
            if msg in json_obj["gay"]:
                await ctx.send('{name}本身就係死gay佬'.format(name=msg))
                return

            json_obj["gay"].append(msg)

            json_file = open("./cmds/gayList.json", "w", encoding="UTF-8")
            json.dump(json_obj, json_file, ensure_ascii=False)
            json_file.close()
            await ctx.send('{name}而家都係死gay佬'.format(name=msg))
        except Exception as ex:
            print(ex)

    @commands.command()
    async def removeGay(self, ctx, msg):
        json_file = open("./cmds/gayList.json", "r")
        json_obj = json.load(json_file)
        json_file.close()

        for index in range(len(json_obj["gay"])):
            if msg == json_obj["gay"][index]:
                del json_obj["gay"][index]
                json_file = open("./cmds/gayList.json", "w", encoding="UTF-8")
                json.dump(json_obj, json_file, ensure_ascii=False)
                json_file.close()
                await ctx.send('{name}而家唔係死gay佬啦...'.format(name=msg))
                return
        await ctx.send('{name}本來就唔係死gay佬'.format(name=msg))

    @commands.command()
    async def listGay(self, ctx):
        json_file = open("./cmds/gayList.json", "r")
        json_obj = json.load(json_file)
        list = []
        list = json_obj["gay"]
        await ctx.send(list)

    # helper function
    def randomBool(self, prob):
        return True if random.random() < prob else False

    @commands.command()
    async def weeb(self, ctx, *args):
        if len(args) == 0:
            await ctx.send('（黑化勃起')
            return

        with open("./cmds/weeb_msg.json", "r") as file:
            json_obj = json.load(file)

        weeb_text = ''

        for line in args:
            have_www = self.randomBool(0.2)
            # a if condition else b
            www_count = random.randint(2, 7) if have_www else 0
            www_str = 'w' * www_count if www_count else ''

            have_postfix = self.randomBool(0.6)
            postfix_index = random.randint(
                0, (len(json_obj["postfix"]) - 1))
            postfix_str = json_obj["postfix"][postfix_index] if have_postfix else ''

            have_prefix = self.randomBool(0.2)
            prefix_index = random.randint(
                0, (len(json_obj["prefix"]) - 1))
            prefix_str = json_obj["prefix"][prefix_index] if have_prefix else ''

            weeb_text += f'{prefix_str} {line}{www_str}{postfix_str}\n'.lstrip()

        await ctx.message.delete()
        await ctx.send(weeb_text)

    @commands.command()
    async def pien(self, ctx):
        pic = discord.File('./pic/pien.jpg')
        await ctx.send(file=pic)

    @commands.command()
    async def xi(self, ctx):
        pic = discord.File('./pic/xi.jpg')
        await ctx.send(file=pic)

    @commands.command()
    async def 我婆(self, ctx):
        with open('setting.json', 'r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        ranpic = random.choice(jdata['WIFE'])
        pic = discord.File(ranpic)
        await ctx.send(file=pic)


def setup(bot):
    bot.add_cog(Main(bot))
