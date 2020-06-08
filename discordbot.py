from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='！')
token = os.environ['DISCORD_BOT_TOKEN']



@bot.command()
async def ping(ctx):
    await ctx.send('pong')

    
@bot.command()
async def 井伊野ミコ(ctx):
    await ctx.send('あ、イイっすねー')

    
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

    
@bot.command(name="ざこぼしyoutube")
async def hello(ctx):
    await ctx.send(f"{ctx.message.author.name}https://www.youtube.com/channel/UCOi-pKaujqZtSU8oAnRUV_Q")

    
@bot.command(name="ざこぼしtwitter")
async def hello(ctx):
    await ctx.send(f"{ctx.message.author.name}https://twitter.com/zakoboshi")

    
@bot.command(name="おつにだ")
async def goodbye(ctx):
    await ctx.send(f"乙、＠{ctx.message.author.name}")

    
@bot.command(name="しりとり")
async def goodbye(ctx):
    await ctx.send(f"り、り、リンカーン！")

    
@bot.command(name="おすすめオナネタ")
async def goodbye(ctx):
    await ctx.send(f"{ctx.message.author.name}https://jp.pornhub.com/video/search?search=%E6%97%A5%E6%9C%AC%E4%BA%BA%E3%81%8A%E3%81%99%E3%81%99%E3%82%81")

    
@bot.command(name="二次エロ")
async def goodbye(ctx):
    await ctx.send(f"{ctx.message.author.name}http://buhidoh.net/archives")

    
@bot.command(name="手マン")
async def goodbye(ctx):
    await ctx.send(f"{ctx.message.author.name}https://jp.pornhub.com/video/search?search=%E6%89%8B%E3%83%9E%E3%83%B3")

    
@bot.command(name="ゆゆうた")
async def goodbye(ctx):
    await ctx.send(f"{ctx.message.author.name}https://www.youtube.com/channel/UCNMG8dXjgqxS94dHljP9duQ")

    
@bot.command(name="二次ロリ")
async def goodbye(ctx):
    await ctx.send(f"{ctx.message.author.name}http://moeimg.net/tag/%E3%83%AD%E3%83%AA")

bot.run(token)
