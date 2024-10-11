"""
Slash command handler for the Discord bot.

This module is responsible for loading and managing slash command cogs.
It provides functionality to dynamically load slash command modules from the cogs/slash_commands directory.

Classes:
    SlashCommandHandler: Handles the loading and management of slash command cogs.
"""

import os
import inspect
import traceback
from discord import app_commands
from utils.logger import get_logger
from utils.extension_utils import safe_load_extension

logger = get_logger(__name__)

class SlashCommandHandler:
    def __init__(self, bot):
        self.bot = bot
        self.synced = False
        self.bot.tree.on_error = self.on_app_command_error

    async def load_slash_commands(self, directory='./cogs/slash_commands'):
        """
        Loads all slash command cogs from the specified directory.

        This method is called during the bot's setup phase.

        Args:
            directory (str): The directory to load slash command cogs from. Defaults to './cogs/slash_commands'.
        """
        for root, _, files in os.walk(directory):
            for filename in files:
                if filename.endswith('.py') and not filename.startswith('__'):
                    try:
                        cog_path = os.path.join(root, filename)
                        module_path = os.path.relpath(cog_path, './').replace('/', '.').replace('\\', '.')[:-3]
                        if await safe_load_extension(self.bot, module_path):
                            logger.info(f'Loaded slash command module: {module_path}')
                            await self._process_slash_commands(module_path)
                        else:
                            logger.info(f'Slash command module already loaded: {module_path}')
                    except Exception as e:
                        logger.error(f'Failed to load slash command module {filename[:-3]}')
                        logger.error(str(e))

    async def _process_slash_commands(self, module_path):
        module = __import__(module_path, fromlist=[''])
        for name, obj in inspect.getmembers(module):
            if isinstance(obj, app_commands.Command):
                self._add_slash_command_help(obj)
                self.bot.tree.add_command(obj)
                logger.info(f"Added slash command: {obj.name}")

    def _add_slash_command_help(self, command):
        if hasattr(command.callback, '__slash_command_args__'):
            args_info = command.callback.__slash_command_args__
            param_desc = "\n".join([f"{name}: {arg_type.__name__}" for name, arg_type, _ in args_info])
            usage = " ".join([f"<{name}>" if default is None else f"[{name}]" for name, _, default in args_info])
            command.description = f"Parameters:\n{param_desc}\n\nUsage: /{command.name} {usage}"

    async def sync_slash_commands(self):
        """
        Syncs all slash commands with Discord.

        This method should be called after all slash commands are loaded.
        """
        logger.info("Syncing slash commands...")
        try:
            synced = await self.bot.tree.sync()
            logger.info(f"Synced {len(synced)} slash command(s)!")
            self.synced = True
        except Exception as e:
            logger.error(f"Failed to sync slash commands: {str(e)}")

    async def on_app_command_error(self, interaction, error):
        """
        Handles errors for application commands (slash commands).
        
        Args:
            interaction (discord.Interaction): The interaction that caused the error.
            error (app_commands.AppCommandError): The error that occurred.
        """
        try:
            if isinstance(error, app_commands.CommandOnCooldown):
                await interaction.response.send_message(f"Error: This command is on cooldown. Please try again in {error.retry_after:.2f} seconds.", ephemeral=True)
            elif isinstance(error, app_commands.MissingPermissions):
                await interaction.response.send_message("Error: You don't have the required permissions to use this command.", ephemeral=True)
            elif isinstance(error, app_commands.BotMissingPermissions):
                await interaction.response.send_message("Error: The bot doesn't have the required permissions to execute this command.", ephemeral=True)
            elif isinstance(error, app_commands.CommandNotFound):
                await interaction.response.send_message("Error: Command not found.", ephemeral=True)
            else:
                await interaction.response.send_message(f"An unexpected error occurred. Please try again or contact the bot administrator.", ephemeral=True)
                logger.error(f"Unhandled error in slash command: {traceback.format_exc()}")
        except Exception as e:
            logger.error(f"Error in slash command error handler: {traceback.format_exc()}")
            await interaction.response.send_message("An error occurred while processing your command. Please try again later.", ephemeral=True)

    async def setup(self):
        await self.sync_slash_commands()
