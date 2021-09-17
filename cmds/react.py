import discord
import random
from discord.ext import commands
from core.classes import Cog_Extension
import json


class React(Cog_Extension):

    messageList = [
        '躝啦屌你老母',
        '唔該躝',
        '躝啦'
    ]
    gayList = []
    with open('./cmds/gayList.json', 'r', encoding='utf8') as f:
        json_data = json.load(f)
        gayList = json_data["gay"]

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        if '躝' in message.content:
            channel = message.channel
            await channel.send(self.messageList[random.randint(0, 2)])
            return

        if message.content.startswith('立屌玩緊'):
            msg = message.content.split(" ", 2)
            if len(msg) == 1:
                await message.channel.send("？")
                return
            else:
                game = discord.Game(msg[1])
                await self.bot.change_presence(activity=game)
                await message.channel.send('立屌而家玩緊'+msg[1])
                return


        if message.content in self.gayList:
            channel = message.channel
            await channel.send("He's gay.")
            return



def setup(bot):
    bot.add_cog(React(bot))
