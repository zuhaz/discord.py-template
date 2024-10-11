"""
Base modal class for the Discord bot.

This module provides a base class for creating modals with common functionality.

Classes:
    BaseModal: A base class for creating modals.
"""

import discord
from discord.ui import Modal
from utils.logger import get_logger

logger = get_logger(__name__)

class BaseModal(Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_submit(self, interaction: discord.Interaction):
        """
        Called when the modal is submitted. Override this method in subclasses.
        """
        pass

    async def on_error(self, interaction: discord.Interaction, error: Exception):
        """
        Called when an error occurs during modal handling.
        """
        logger.error(f"Error in modal {self.__class__.__name__}: {str(error)}")
        await interaction.response.send_message("An error occurred while processing your input.", ephemeral=True)