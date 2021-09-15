import discord
import random
from discord.ext import commands
from core.classes import Cog_Extension


class React(Cog_Extension):

    messageList = [
        '躝啦屌你老母',
        '唔該躝',
        '躝啦'
    ]

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if '躝' in message.content:
            channel = message.channel
            await channel.send(self.messageList[random.randint(0, 2)])

        gayList = [
            '米高',
            '木屌',
            'Ag',
            'Hei'
        ]
        for gay in gayList:
            if gay in message.content:
                channel = message.channel
                await channel.send("He's gay.")


def setup(bot):
    bot.add_cog(React(bot))
