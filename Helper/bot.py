import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='^')

@bot.event
async def on_ready():
    print(">> Bot is Online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(730351075021815909)
    await channel.send(f'{member} 加入伺服器! 歡迎~')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(730351112145600572)
    await channel.send(f'{member} 離開伺服器......qwq')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')


bot.run('NzMwMzE5MjMyMDA4NTg1MzM4.XwWQWA.RaVgAZ2i9WumqtUcUyZ-XC66bwI')