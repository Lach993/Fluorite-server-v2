import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    
    @commands.is_owner()
    @commands.command(name="shutdown", aliases=["stop", "exit"])
    async def shutdown(self, ctx):
        """shutdown bot"""
        await ctx.send("shutting down")
        await self.bot.close()
    
    @commands.is_owner()
    @commands.command(name="remove", aliases=["delete"])
    async def remove(self, ctx):
        """remove player from database"""
        pass

    @commands.is_owner()
    @commands.command(name="remove_dead", aliases=["remove_dead_players"])
    async def remove_dead(self, ctx):
        """remove dead players from database"""
        pass

    @commands.is_owner()
    @commands.command(name="refactor", aliases=["refactor_database"])
    async def refactor(self, ctx):
        """refactor database"""
        pass


