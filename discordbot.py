from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
    
@bot.command()
async def やぁ(ctx):
    await ctx.send('よぉ')     
    
bot.run(token)
