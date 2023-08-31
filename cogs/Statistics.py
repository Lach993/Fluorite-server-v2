import discord
from discord.ext import commands

class Statistics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="stats", aliases=["statistics", "stat"])
    async def stats(self, ctx):
        """get stats from uuid"""
        pass

    @commands.command(name="uuid", aliases=["uuid_from_username"])
    async def uuid(self, ctx):
        """get uuid from username"""
        pass

    @commands.command(name="cosmetics", aliases=["cosmetic"])
    async def cosmetics(self, ctx):
        """get cosmetics from name"""
        pass

    @commands.command(name="capes", aliases=["cape"])
    async def capes(self, ctx):
        """get capes from name"""
        pass

    @commands.command(name="info", aliases=["information"])
    async def info(self, ctx):
        """get total amount of players stored in database"""
        pass

    @commands.command(name="top", aliases=["top_players"])
    async def top(self, ctx):
        """get top players"""
        pass

    