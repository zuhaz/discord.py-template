from typing import Callable
from discord.ext import commands
from functools import wraps

def command_args(*args_config, permissions=None, cooldown=None):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(self, ctx, *args):
            parsed_args = []
            for i, (arg_name, arg_type, arg_default) in enumerate(args_config):
                if i < len(args):
                    try:
                        parsed_args.append(arg_type(args[i]))
                    except ValueError:
                        await ctx.send(f"Invalid type for argument '{arg_name}'. Expected {arg_type.__name__}.")
                        return
                else:
                    parsed_args.append(arg_default)
            return await func(self, ctx, *parsed_args)
        wrapper.__command_args__ = args_config
        
        if permissions:
            wrapper = commands.has_permissions(**permissions)(wrapper)
        if cooldown:
            wrapper = commands.cooldown(*cooldown)(wrapper)
        
        return wrapper
    return decorator

def slash_command_args(*args_config):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(self, interaction, **kwargs):
            parsed_args = {}
            for arg_name, arg_type, _ in args_config:
                if arg_name in kwargs:
                    parsed_args[arg_name] = kwargs[arg_name]
            return await func(self, interaction, **parsed_args)
        wrapper.__slash_command_args__ = args_config
        
        return wrapper
    return decorator