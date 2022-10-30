from re import L
import discord
from discord.ext import commands
import random
import json
import os

with open('./setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix='.')


@bot.event
async def on_ready():
    print(">>", bot.user, "is online <<")
    game_type = random.randint(1, 5)
    if game_type == 1: game = discord.Game('微積分')
    elif game_type == 2: game = discord.Game('Java')
    elif game_type == 3: game = discord.Game('C++')
    elif game_type == 4: game = discord.Game('量子力學')
    elif game_type == 5: game = discord.Game('相對論')
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    channel = bot.get_channel(int(jdata['door_channel']))
    await channel.send(str(member) +' 進入了道具庫，歡迎你的加入！')
    
@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')
    channel = bot.get_channel(int(jdata['door_channel']))
    await channel.send(str(member) + ' 離開了道具庫，我們有緣再見面QQ')

for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(("cmds.%s" % Filename[-3]))

if __name__ == '__main__':
    bot.run(jdata['TOKEN'])


