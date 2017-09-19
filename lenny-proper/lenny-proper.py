import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lenny(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("( ͡° ͜ʖ ͡°)")