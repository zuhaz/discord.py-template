import discord
from discord.ext import commands
from utils.command_utils import command_args

class ExampleCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @command_args(
        ("name", str, None),
        ("age", int, 0),
        ("is_member", bool, False),
        permissions={"send_messages": True},
        cooldown=(1, 5, commands.BucketType.user)
    )
    async def example(self, ctx, name: str, age: int, is_member: bool):
        """
        An example command with multiple arguments, permissions, and cooldown.

        Parameters:
        - name (str): The name of the user (required)
        - age (int): The age of the user (optional, default: 0)
        - is_member (bool): Whether the user is a member (optional, default: False)

        Usage:
            !example <name> [age] [is_member]
        """
        response = f"Hello, {name}! "
        if age > 0:
            response += f"You are {age} years old. "
        response += f"Member status: {is_member}"
        await ctx.send(response)

# IMPORTANT: This function is required to add the cog to the bot.
# It does the following:
# 1. Creates an instance of the ExampleCommands cog.
# 2. Adds the cog to the bot using bot.add_cog().
# 3. This makes all the prefix commands in this cog available to the bot.
# 4. The bot will call this function when loading the cog.
async def setup(bot):
    await bot.add_cog(ExampleCommands(bot))
