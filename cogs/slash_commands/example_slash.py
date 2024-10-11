import discord
from discord import app_commands
from discord.ext import commands
from utils.command_utils import slash_command_args

class ExampleSlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="example_slash", description="An example slash command with arguments")
    @app_commands.checks.cooldown(1, 5) 
    @app_commands.checks.has_permissions(send_messages=True)
    @slash_command_args(
        ("name", str, None),
        ("age", int, 0),
        ("is_member", bool, False)
    )
    async def example_slash_command(self, interaction: discord.Interaction, name: str, age: int, is_member: bool):
        response = f"Hello, {name}! "
        if age > 0:
            response += f"You are {age} years old. "
        response += f"Member status: {is_member}"
        await interaction.response.send_message(response)

# IMPORTANT: This function is required to add the cog to the bot.
# It does the following:
# 1. Creates an instance of the ExampleSlashCommands cog.
# 2. Adds the cog to the bot using bot.add_cog().
# 3. This makes all the slash commands in this cog available to the bot.
# 4. The bot will call this function when loading the cog.
async def setup(bot):
    await bot.add_cog(ExampleSlashCommands(bot))