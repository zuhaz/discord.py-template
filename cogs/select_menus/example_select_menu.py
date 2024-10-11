import discord
from discord.ui import Select, View
from utils.logger import get_logger

logger = get_logger(__name__)

class ExampleSelectMenu(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Option 1", description="This is the first option", value="1"),
            discord.SelectOption(label="Option 2", description="This is the second option", value="2"),
            discord.SelectOption(label="Option 3", description="This is the third option", value="3"),
        ]
        super().__init__(
            placeholder="Choose an option",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        selected_value = self.values[0]
        logger.info(f"User {interaction.user} selected option: {selected_value}")
        await interaction.response.send_message(f"You selected option {selected_value}!", ephemeral=True)

# IMPORTANT: This function is required to register the select menu with the bot.
# It does the following:
# 1. Uses the bot's select_menu_handler to register the select menu.
# 2. Associates the "example_menu" identifier with the ExampleSelectMenu class.
# 3. This allows the bot to create and use this select menu when needed.
# 4. The bot will call this function when loading this module.
async def setup(bot):
    bot.select_menu_handler.register_select_menu("example_menu", ExampleSelectMenu)