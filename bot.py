"""
Core bot class and initialization.

This module defines the main DiscordBot class, which inherits from commands.Bot.
It handles the initialization of the bot, including loading cogs and setting up handlers.

Classes:
    DiscordBot: The main bot class.
"""

import discord
from discord.ext import commands
from config import TOKEN, PREFIX, INTENTS, DEBUG, STATUS, ACTIVITY
from handlers.command_handler import CommandHandler
from handlers.event_handler import EventHandler
from handlers.slash_command_handler import SlashCommandHandler
from handlers.modal_handler import ModalHandler
from handlers.select_menu_handler import SelectMenuHandler 
from utils.logger import get_logger

logger = get_logger(__name__)

class DiscordBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=PREFIX,
            intents=INTENTS,
            status=STATUS,
            activity=ACTIVITY
        )
        self.command_handler = CommandHandler(self)
        self.event_handler = EventHandler(self)
        self.slash_command_handler = SlashCommandHandler(self)
        self.modal_handler = ModalHandler(self)
        self.select_menu_handler = SelectMenuHandler(self)  

    async def setup_hook(self):
        """A coroutine to be called to setup the bot, by default this is blank."""
        logger.info("Setting up bot...")
        try:
            await self.command_handler.load_commands()
            await self.event_handler.load_events()
            await self.slash_command_handler.load_slash_commands()
            await self.modal_handler.load_modals()
            await self.select_menu_handler.load_select_menus()
            await self.tree.sync() 
            if DEBUG:
                logger.debug("All handlers loaded successfully.")
        except Exception as e:
            logger.error(f"Error during setup: {str(e)}")
            raise

    async def on_ready(self):
        """Called when the bot is done preparing the data received from Discord."""
        logger.info(f'Logged in as {self.user} (ID: {self.user.id})')
        if DEBUG:
            logger.debug(f"Debug mode is ON. Intents: {self.intents}")
            logger.debug(f"Connected to {len(self.guilds)} guilds")
        logger.info('------')

    async def on_error(self, event_method, *args, **kwargs):
        """Handles errors that occur in event listeners."""
        logger.error(f"An error occurred in {event_method}")
        if DEBUG:
            logger.exception("Exception details:")

    async def start(self):
        """Start the bot."""
        logger.info("Starting bot...")
        try:
            if DEBUG:
                logger.debug(f"Attempting to start bot with token: {TOKEN[:5]}...")
            await super().start(TOKEN, reconnect=True)
        except discord.LoginFailure:
            logger.error("Failed to login. Please check your token.")
        except Exception as e:
            logger.error(f"An error occurred while starting the bot: {str(e)}")
            if DEBUG:
                logger.exception("Exception details:")

if __name__ == "__main__":
    bot = DiscordBot()
    try:
        bot.run(TOKEN)
    except KeyboardInterrupt:
        logger.info("Bot stopped by user.")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        if DEBUG:
            logger.exception("Exception details:")