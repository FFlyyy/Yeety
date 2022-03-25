from datetime import datetime, timezone
from datetime import timedelta
from time import time as _time
from discord.ext import commands
import json
import discord
import os

intents = discord.Intents().all()
bot = commands.Bot(
    command_prefix='-',
    case_insensitive=True,
    owner_id=942917416768376942,
    activity=discord.Activity(
        type=discord.ActivityType.playing,
        name="Yeeting stuff",
    ),
    status=discord.Status.online,
    intents=intents,
)
global startTime
startTime = _time()
bot.remove_command('help')

    
bot.colors = {
    "WHITE": 0xFFFFFF,
    "AQUA": 0x1ABC9C,
    "GREEN": 0x2ECC71,
    "BLUE": 0x3498DB,
    "GOLD": 0xF1C40F,
    "ORANGE": 0xE67E22,
    "RED": 0xE74C3C,
    "DODGERBLUE": 0x1e90ff
}

bot.color_list = [c for c in bot.colors.values()]
    
    
@bot.command()
async def create_role(ctx, name, hex_str):
    color = int(hex_str, 16)
    await ctx.guild.create_role(name=name, color=discord.Colour(color), mentionable=False)
    await ctx.send(f"The role has been created")
    
    
@bot.command()
async def botinvite(ctx):
    invite = "https://discord.com/api/oauth2/authorize?client_id=954115452991315999&permissions=8&scope=bot"
    await ctx.send(f"Here's your invite: {invite}")

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

    
@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

    
@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        
@bot.command()
async def botservers(ctx):
    await ctx.send(f"I'm in {len(bot.guilds)} servers!")
            
  
bot.run("OTU0MTE1NDUyOTkxMzE1OTk5.YjObQg.XEAw-gj8W6ezyTyUtQ981XQJzDI")