import discord
from discord.ext import commands
from utils import time_to_seconds
import asyncio

class Timed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_update = 0
        self.update_interval = time_to_seconds(days=1)
        self.update_task = self.bot.loop.create_task(self.update())

    async def update(self):
        while True:
            await self.bot.wait_until_ready()
            if self.last_update + self.update_interval < time_to_seconds():
                self.last_update = time_to_seconds()
                await self.bot.update()
            await asyncio.sleep(time_to_seconds(minutes=30))
