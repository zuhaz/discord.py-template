"""
Event handler for the Discord bot.

This module is responsible for loading and managing event cogs.
It provides functionality to dynamically load event modules from the cogs/events directory.

Classes:
    EventHandler: Handles the loading and management of event cogs.
"""

import os
import traceback
from utils.logger import get_logger

logger = get_logger(__name__)

class EventHandler:
    def __init__(self, bot):
        self.bot = bot

    async def load_events(self, directory='./cogs/events'):
        """
        Loads all event cogs from the specified directory.

        This method is called during the bot's setup phase.
        """
        for filename in os.listdir(directory):
            if filename.endswith('.py') and not filename.startswith('__'):
                try:
                    await self.bot.load_extension(f'cogs.events.{filename[:-3]}')
                    logger.info(f'Loaded event module: {filename[:-3]}')
                except Exception as e:
                    logger.error(f'Failed to load event module {filename[:-3]}')
                    logger.error(traceback.format_exc())