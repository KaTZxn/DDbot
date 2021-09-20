import discord
from discord.ext import commands, tasks
import os


bot = commands.Bot(command_prefix="-")


@bot.event
async def on_ready():
    print("---Bot is online now.---")
    game = discord.Game('湊あくあ')
    await bot.change_presence(status=discord.Status.online, activity=game)


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'loaded {extension} done.')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'unloaded {extension} done.')


@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'reloaded {extension} done.')


for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename[:-3]}")

access_token = os.environ["DISCORD_BOT_TOKEN"]
if __name__ == "__main__":
    bot.run('access_token')
