import discord
from discord.ext import commands
import os
import random
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix='.')

@bot.event
async def on_ready():
    print(">>", bot.user, "is online <<")
    game_type = random.randint(1, 5)
    if game_type == 1:
        game = discord.Game('微積分')
    elif game_type == 2:
        game = discord.Game('Java')
    elif game_type == 3:
        game = discord.Game('C++')
    elif game_type == 4:
        game = discord.Game('量子力學')
    elif game_type == 5:
        game = discord.Game('相對論')
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    channel = bot.get_channel(1035896049958662165)
    await channel.send(str(member) +' 進入了道具庫，歡迎你的加入！')
    
@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')
    channel = bot.get_channel(1035896049958662165)
    await channel.send(str(member) + ' 離開了道具庫，我們有緣再見面QQ')

@bot.command()
async def ping(ctx):
    await ctx.send("%s %d%s" % ("pong! ", int(bot.latency*1000), "(ms)"))

bot.run(os.getenv('TOKEN'))


# https://www.youtube.com/watch?v=rFJoLrVlEHY&list=PLSCgthA1Anif1w6mKM3O6xlBGGypXtrtN&index=5&ab_channel=Proladon
