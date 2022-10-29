import discord
from discord.ext import commands
import os
import random

bot = commands.Bot(intents=discord.Intents.default(), command_prefix='.')


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
async def on_menber_join(member):
    print(f'{member} join!')
    channel = bot.get_channel()


@bot.event
async def on_menber_remove(member):
    print(f'{member} leave!')
bot.run(os.getenv('TOKEN'))


# https://www.youtube.com/watch?v=rFJoLrVlEHY&list=PLSCgthA1Anif1w6mKM3O6xlBGGypXtrtN&index=5&ab_channel=Proladon
