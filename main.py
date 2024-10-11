"""
Main entry point for the Discord bot.

This script initializes and runs the bot. It's responsible for setting up logging
and handling any top-level exception handling if necessary.

Usage:
    python main.py
"""

import asyncio
from bot import DiscordBot
from utils.logger import setup_logging, get_logger

# Set up logging
setup_logging()

logger = get_logger(__name__)

async def main():
    logger.info("Starting bot...")
    bot = DiscordBot()
    try:
        await bot.start()
    except Exception as e:
        logger.error(f"Error running bot: {str(e)}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user.")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")