import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='e!', intents = intents)

@bot.event
async def on_ready():
    print(">>bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(993519419747737673)
    await channel.send(f'{member} 歡迎加入')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(993519419747737673)
    await channel.send(f'{member} 離開了我們')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

bot.run("MTAwMDIzMzE0NTY3NDc2MDMzMw.GbGE80.gWUdvfCDDXOZXeB7cwCwDPtYY83K0zfxuE3dQc")