from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
    
@bot.command()
async def やぁ(ctx):
    await ctx.send('よぉ')     

    
 @bot.command()
async def やぁ(ctx):
    await ctx.send('よぉ')      

    
@bot.command()
async def 死ね(ctx):
    await ctx.send('は？')


@bot.command()
async def ねこ(ctx):
    await ctx.send('にゃーん')


@bot.command(name="やぁ")
async def hello(ctx):
    await ctx.send(f"よぉ、{ctx.message.author.name}！")


@bot.command(name="pornhub")
async def hello(ctx):
    await ctx.send(f"{ctx.message.author.name}https://jp.pornhub.com/")


@bot.command(name="youtube")
async def hello(ctx):
    await ctx.send(f"{ctx.message.author.name}https://www.youtube.com/?gl=JP")
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
bot.run(token)
