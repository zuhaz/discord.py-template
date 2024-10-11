"""
Modal handler for the Discord bot.

This module is responsible for loading, managing, and handling modal interactions.

Classes:
    ModalHandler: Handles the loading, management, and interaction of modal cogs.
"""

import os
import traceback
from utils.logger import get_logger
from utils.base_modal import BaseModal
import discord

logger = get_logger(__name__)

class ModalHandler:
    def __init__(self, bot):
        self.bot = bot
        self.modals = {}
        self.submit_handlers = {}
        self.error_handlers = {}

    async def load_modals(self, directory='./cogs/modals'):
        """
        Loads all modal cogs from the specified directory.
        """
        for filename in os.listdir(directory):
            if filename.endswith('.py') and not filename.startswith('__'):
                try:
                    await self.bot.load_extension(f'cogs.modals.{filename[:-3]}')
                    logger.info(f'Loaded modal module: {filename[:-3]}')
                except Exception as e:
                    logger.error(f'Failed to load modal module {filename[:-3]}')
                    logger.error(traceback.format_exc())

    def register_modal(self, name: str, modal_class: type, submit_handler=None, error_handler=None):
        """
        Register a modal class with given name and handlers.
        """
        if not issubclass(modal_class, BaseModal):
            raise ValueError("Modal class must inherit from BaseModal")
        self.modals[name] = modal_class
        if submit_handler:
            self.submit_handlers[name] = submit_handler
        if error_handler:
            self.error_handlers[name] = error_handler
        logger.info(f"Registered modal: {name}")

    def get_modal(self, name: str, *args, **kwargs) -> BaseModal:
        """
        Get an instance of a registered modal by name.
        """
        if name not in self.modals:
            raise ValueError(f"Modal {name} not found")
        modal = self.modals[name](*args, **kwargs)
        modal.on_submit = lambda interaction: self.handle_submit(modal, interaction)
        modal.on_error = lambda interaction, error: self.handle_error(modal, interaction, error)
        return modal

    async def handle_submit(self, modal: BaseModal, interaction: discord.Interaction):
        """
        Handle modal submission.
        """
        modal_name = next((name for name, cls in self.modals.items() if isinstance(modal, cls)), None)
        if modal_name and modal_name in self.submit_handlers:
            await self.submit_handlers[modal_name](modal, interaction)
        else:
            logger.warning(f"No submit handler found for modal: {modal.__class__.__name__}")
            await interaction.response.send_message("Thank you for your submission.", ephemeral=True)

    async def handle_error(self, modal: BaseModal, interaction: discord.Interaction, error: Exception):
        """
        Handle modal error.
        """
        modal_name = next((name for name, cls in self.modals.items() if isinstance(modal, cls)), None)
        if modal_name and modal_name in self.error_handlers:
            await self.error_handlers[modal_name](modal, interaction, error)
        else:
            logger.error(f"Error in modal {modal.__class__.__name__}: {str(error)}")
            await interaction.response.send_message("An error occurred while processing your input.", ephemeral=True)