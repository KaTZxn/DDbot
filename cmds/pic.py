import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
from bs4 import BeautifulSoup
import requests


class Pic(Cog_Extension):
    @commands.command()
    async def s(self, ctx, msg,*,num=1):
        response = requests.get(f'https://yande.re/post?tags={msg}')
        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.find_all('a', {'class': 'directlink largeimg'})
        image_links = [result.get("href") for result in results]
        for i in range(num):
            num = random.randint(1, len(image_links))
            await ctx.send(image_links[num])


def setup(bot):
    bot.add_cog(Pic(bot))
