"""
Select Menu handler for the Discord bot.

This module is responsible for loading, managing, and handling select menu interactions.

Classes:
    SelectMenuHandler: Handles the loading, management, and interaction of select menu cogs.
"""

import os
import traceback
from utils.logger import get_logger
import discord

logger = get_logger(__name__)

class SelectMenuHandler:
    def __init__(self, bot):
        self.bot = bot
        self.select_menus = {}

    async def load_select_menus(self):
        """
        Loads all select menu cogs from the cogs/select_menus directory.
        """
        for filename in os.listdir('./cogs/select_menus'):
            if filename.endswith('.py') and not filename.startswith('__'):
                try:
                    await self.bot.load_extension(f'cogs.select_menus.{filename[:-3]}')
                    logger.info(f'Loaded select menu module: {filename[:-3]}')
                except Exception as e:
                    logger.error(f'Failed to load select menu module {filename[:-3]}')
                    logger.error(traceback.format_exc())

    def register_select_menu(self, name: str, select_menu_class: type):
        """
        Register a select menu class with given name.
        """
        self.select_menus[name] = select_menu_class
        logger.info(f"Registered select menu: {name}")

    def get_select_menu(self, name: str) -> discord.ui.Select:
        """
        Get an instance of a registered select menu by name.
        """
        if name not in self.select_menus:
            raise ValueError(f"Select menu {name} not found")
        return self.select_menus[name]()