import discord
from discord.ext import commands
from core.classes import Cog_Extension

class React(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.bot.user:
            return
        if message.content.startswith('躝'):
            channel = message.channel
            await channel.send('躝啦屌你老母')

def setup(bot):
    bot.add_cog(React(bot))