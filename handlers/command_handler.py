"""
Command handler for the Discord bot.

This module is responsible for loading and managing command cogs.
It provides functionality to dynamically load command modules from the cogs directory.

Classes:
    CommandHandler: Handles the loading and management of command cogs.
"""

import os
import inspect
import traceback
from discord.ext import commands
from utils.logger import get_logger
from utils.extension_utils import safe_load_extension

logger = get_logger(__name__)

class CommandHandler:
    def __init__(self, bot):
        self.bot = bot
        self.bot.event(self.on_command_error) 

    async def load_commands(self, directory='./cogs/commands'):
        """
        Loads all command cogs from the specified directory.

        This method is called during the bot's setup phase.

        Args:
            directory (str): The directory to load cogs from. Defaults to './cogs/commands'.
        """
        for root, _, files in os.walk(directory):
            for filename in files:
                if filename.endswith('.py') and not filename.startswith('__'):
                    try:
                        cog_path = os.path.join(root, filename)
                        module_path = os.path.relpath(cog_path, './').replace('/', '.').replace('\\', '.')[:-3]
                        if await safe_load_extension(self.bot, module_path):
                            logger.info(f'Loaded command module: {module_path}')
                            self._process_commands(module_path)
                        else:
                            logger.info(f'Command module already loaded: {module_path}')
                    except Exception as e:
                        logger.error(f'Failed to load command module {filename[:-3]}')
                        logger.error(str(e))

    def _process_commands(self, module_path):
        module = __import__(module_path, fromlist=[''])
        for name, obj in inspect.getmembers(module):
            if isinstance(obj, commands.Command):
                self._add_command_help(obj)

    def _add_command_help(self, command):
        if hasattr(command.callback, '__command_args__'):
            args_info = command.callback.__command_args__
            param_desc = "\n".join([f"{name}: {arg_type.__name__}" for name, arg_type, _ in args_info])
            usage = " ".join([f"<{name}>" if default is None else f"[{name}]" for name, _, default in args_info])
            command.help = f"Parameters:\n{param_desc}\n\nUsage: {self.bot.command_prefix}{command.name} {usage}"

    async def on_command_error(self, ctx, error):
        await self.handle_command_error(ctx, error)

    async def handle_command_error(self, ctx, error):
        """
        Handles command errors and provides detailed feedback to the user.
        
        Args:
            ctx (commands.Context): The context of the command invocation.
            error (commands.CommandError): The error that occurred.
        """
        try:
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send(f"Error: Missing required argument: `{error.param.name}`\n"
                               f"Please check the command usage with `{ctx.prefix}help {ctx.command.name}`")
            elif isinstance(error, commands.BadArgument):
                await ctx.send(f"Error: Invalid argument type for `{error.param.name}`\n"
                               f"Please check the command usage with `{ctx.prefix}help {ctx.command.name}`")
            elif isinstance(error, commands.CommandInvokeError):
                original = error.original
                if isinstance(original, ValueError):
                    await ctx.send(f"Error: Invalid value provided. {str(original)}\n"
                                   f"Please check the command usage with `{ctx.prefix}help {ctx.command.name}`")
                elif isinstance(original, TypeError):
                    await ctx.send(f"Error: Incorrect argument type. {str(original)}\n"
                                   f"Please check the command usage with `{ctx.prefix}help {ctx.command.name}`")
                else:
                    await ctx.send(f"An unexpected error occurred: {str(original)}\n"
                                   "Please try again or contact the bot administrator.")
                    logger.error(f"Unexpected error in command {ctx.command.name}: {traceback.format_exc()}")
            elif isinstance(error, commands.CommandNotFound):
                await ctx.send(f"Error: Command not found. Use `{ctx.prefix}help` to see available commands.")
            elif isinstance(error, commands.MissingPermissions):
                await ctx.send(f"Error: You don't have the required permissions to use this command.")
            elif isinstance(error, commands.BotMissingPermissions):
                await ctx.send(f"Error: The bot doesn't have the required permissions to execute this command.")
            elif isinstance(error, commands.CommandOnCooldown):
                await ctx.send(f"Error: This command is on cooldown. Please try again in {error.retry_after:.2f} seconds.")
            else:
                await ctx.send(f"An unexpected error occurred. Please try again or contact the bot administrator.")
                logger.error(f"Unhandled error in command {ctx.command.name}: {traceback.format_exc()}")
        except Exception as e:
            logger.error(f"Error in error handler: {traceback.format_exc()}")
            await ctx.send("An error occurred while processing your command. Please try again later.")

    async def setup(self):
        pass  