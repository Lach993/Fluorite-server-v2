import discord 

from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord import Intents
from discord import Embed
from discord import Color


import asyncio
import aiohttp
import json
import os


"""SETTINGS"""
class Fluorite_Bot:
    def __init__(self, token, loop):
        self.bot = Bot(command_prefix="f.", intents=Intents.all())
        self.bot.remove_command("help")
        self.bot.loop.create_task(self.update())
        self.bot.run(token)

        

    

    