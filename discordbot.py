from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']



@bot.command()
async def ping(ctx):
    await ctx.send('pong')

    
@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')

@bot.command(name="やぁ")
async def hello(ctx):
    await ctx.send(f"よぉ、{ctx.message.author.name}！")   
    
bot.run(token)
