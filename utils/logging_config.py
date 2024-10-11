import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logging(debug_mode=False):
    if not os.path.exists('logs'):
        os.makedirs('logs')

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG if debug_mode else logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if debug_mode else logging.INFO)
    console_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_format)

    file_handler = RotatingFileHandler(
        'logs/bot.log',
        maxBytes=5*1024*1024, 
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_format)

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

def get_logger(name):
    return logging.getLogger(name)