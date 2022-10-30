from click import command
import discord
from discord.ext import commands
import random
from discord.ext import commands
import json

class  Cog_Extensio(commands.cog):
    def __init__(self, bot):
        self.bot = bot