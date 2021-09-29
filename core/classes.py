import discord
from discord.ext import commands


class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


class Music_Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.is_playing = False

        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        self.FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': 'vn'}

        self.vc = ""
