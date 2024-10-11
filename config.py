import os
import discord
from dotenv import load_dotenv
from utils.logger import get_logger

load_dotenv()

logger = get_logger(__name__)

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
if not TOKEN:
    raise ValueError("No Discord bot token set. Please set the DISCORD_BOT_TOKEN environment variable in your .env file.")

PREFIX = os.getenv('COMMAND_PREFIX', '!')
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

BOT_STATUS = os.getenv('BOT_STATUS', 'online')
BOT_ACTIVITY = os.getenv('BOT_ACTIVITY', f'Prefix: {PREFIX} | Type {PREFIX}help')

STATUS = getattr(discord.Status, BOT_STATUS.lower(), discord.Status.online)
ACTIVITY = discord.Game(name=BOT_ACTIVITY)

INTENTS = discord.Intents(
    guilds=True,
    members=True,
    moderation=True,
    bans=True,
    emojis=True,
    emojis_and_stickers=True,
    integrations=True,
    presences=True,
    messages=True,
    guild_messages=True,
    dm_messages=True,
    reactions=True,
    guild_reactions=True,
    typing=False,
    message_content=True,
)

logger.info(f"Bot configuration loaded. Prefix: {PREFIX}, Debug mode: {DEBUG}")
logger.info(f"Bot status: {STATUS}, Activity: {ACTIVITY}")

# Validate token
if not TOKEN:
    logger.error("No Discord bot token found in .env file.")
    raise ValueError("No Discord bot token set. Please set the DISCORD_BOT_TOKEN environment variable in your .env file.")