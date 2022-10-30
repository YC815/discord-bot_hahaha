import discord
from discord.ext import commands
import random
from discord.ext import commands
import json
from core.classes import Cog_Extension

with open('./setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Main(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("%s %d%s" % ("pong! ", int(self.bot.latency*1000), "(ms)"))

def setup(bot):
    bot.add_cog(Main(Main(bot)))