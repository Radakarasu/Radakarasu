from discord.ext import commands
import os
import traceback
from discord.ext import tasks
from datetime import datetime 

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
    
@bot.command()
async def やぁ(ctx):
    await ctx.send('よぉ')     
    
    
@bot.command()
async def 死ね(ctx):
    await ctx.send('は？')     
    
    
@bot.command()
async def pornhub(ctx):
    await ctx.send('https://jp.pornhub.com/')  
    
    
@bot.command()
async def ロリ(ctx):
    await ctx.send('http://moeimg.net/tag/%E3%83%AD%E3%83%AA')     
    
    
@bot.command()
async def 手マン(ctx):
    await ctx.send('https://jp.pornhub.com/video/search?search=%E6%89%8B%E3%83%9E%E3%83%B3')  
    
    
@bot.command()
async def 同人(ctx):
    await ctx.send('http://buhidoh.net/archives')  
       
        
@bot.command()
async def おすすめ(ctx):
    await ctx.send('https://jp.pornhub.com/video/search?search=%E6%97%A5%E6%9C%AC%E4%BA%BA%E3%81%8A%E3%81%99%E3%81%99%E3%82%81')   
 
bot.run(token)
