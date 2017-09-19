import discord
from discord.ext import commands

class Lenny:
    """My custom cog that does stuff!"""

  def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(pass_context=True, name="lenny")
    async def _lenny(self, ctx: commands.Context):

        await self.bot.say("( ͡° ͜ʖ ͡°)")

def setup(bot: commands.bot):
    bot.add_cog(Lenny(bot))