def is_extension_loaded(bot, extension_name):
    return extension_name in bot.extensions

async def safe_load_extension(bot, extension_name):
    if not is_extension_loaded(bot, extension_name):
        await bot.load_extension(extension_name)
        return True
    return False