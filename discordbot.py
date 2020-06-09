from discord.ext import commands
import os
import traceback
import queue

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
answer_set = queue.Queue(maxsize=30)
current_ans =''
current_ques = ''

@bot.command(aliases=['q'])
@commands.dm_only() # DM以外でこのコマンドを入力するとエラーを吐く
async def question(ctx,arg):
    global current_ans
    if answer_set.full():
        await ctx.send('キューがいっぱいだにゃ')
    else:
        answer_set.put(arg.replace(' ','_'))
        if current_ans == '':
            current_ans = answer_set.get()
        await ctx.send('問題を受け付けたにゃ')

# エラーの処理
@question.error
async def question_error(ctx,error):
    if isinstance(error, commands.errors.PrivateMessageOnly):
        await ctx.send(f'{ctx.author.mention}`/q`はDM限定だにゃー')


@bot.command(aliases=['a'])
async def answer(ctx,arg):
    global current_ans
    global current_ques
    listed_arg = list(arg)
    if current_ans == '':
        await ctx.send('DMに`/q`で問題を送るにゃ')
    elif arg == current_ans:
        current_ans = ''
        current_ques = ''
        if not answer_set.empty():
            current_ans = answer_set.get()
        await ctx.send(f'{ctx.author.mention} 正解だにゃ')
    elif len(current_ans) != len(listed_arg):
        await ctx.send(f'{ctx.author.mention} ぶっぶー！長さが違うにゃ')
    else:
        cnt = 0
        for i in range(len(current_ans)):
            if current_ans[i] == listed_arg[i]:
                cnt+=1
        await ctx.send(f'{ctx.author.mention} ぶっぶー！ **'+ str(cnt) +'** 文字あってるにゃ')        
        
 # /start または /s と発言したらスタートする処理
@bot.command(aliases=['s'])
async def start(ctx):
    global current_ans
    global current_ques
    if current_ans =='':
        await ctx.send('DMに`/q`で問題を送るにゃ')
    else:
        text = sorted(current_ans)
        if current_ques == '':
            current_ques = ''.join()
        await ctx.send('問題は **'+ current_ques +'** だにゃ')       
        
        
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
