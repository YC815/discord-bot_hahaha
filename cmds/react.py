import discord
from discord.ext import commands
import random
from discord.ext import commands
import json
from core.classes import Cog_Extension

with open('./setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def meme(self, ctx):
        r_pic = random.choice(jdata['pic'])
        pic = discord.File(r_pic)
        await ctx.send(file = pic)

def setup(bot):
    bot.add_cog(React(React(bot)))