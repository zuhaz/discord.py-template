import discord
from discord.ext import commands

class ExampleEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        An example event listener that responds to specific messages.

        This event is triggered every time a message is sent in a channel the bot can see.
        For full details on the message object, see:
        https://discordpy.readthedocs.io/en/stable/api.html#discord.Message

        Parameters:
        - message (discord.Message): The message object containing all information about the sent message
        """
        # Ignore messages from bots to prevent potential loops
        if message.author.bot:
            return

        # Check if the message contains "hello" (case-insensitive)
        if "hello" in message.content.lower():
            await message.channel.send("Hello there!")

# IMPORTANT: This function is required to add the cog to the bot.
# It does the following:
# 1. Creates an instance of the ExampleEvents cog.
# 2. Adds the cog to the bot using bot.add_cog().
# 3. This makes all the event listeners in this cog available to the bot.
# 4. The bot will call this function when loading the cog.
async def setup(bot):
    await bot.add_cog(ExampleEvents(bot))