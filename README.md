<h1 align="center">discord.py-template</h1>

<p align="center">
  A comprehensive and modular template for building Discord bots with discord.py
</p>

<p align="center">
  <a href="https://discord.gg/7mhdvfgybX">
    <img src="https://img.shields.io/discord/1220631055845822485?color=7289DA&logo=discord&logoColor=white" alt="Discord Server"/>
  </a>
  <a href="https://github.com/zuhaz/discord.py-template/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/zuhaz/discord.py-template?style=flat-square" alt="License"/>
  </a>
  <a href="https://github.com/zuhaz/discord.py-template/stargazers">
    <img src="https://img.shields.io/github/stars/zuhaz/discord.py-template?style=flat-square" alt="Stars"/>
  </a>
  <img src="https://img.shields.io/badge/python-3.11.5-blue.svg?style=flat-square" alt="Python 3.11.5"/>
  <img src="https://img.shields.io/badge/discord.py-2.3.2-blue.svg?style=flat-square" alt="discord.py 2.3.2"/>
  <img src="https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square" alt="Code style: black"/>
  <img src="https://img.shields.io/badge/Maintained-yes-green.svg?style=flat-square" alt="Maintained Yes"/>
  <img src="https://img.shields.io/github/issues/zuhaz/discord.py-template?style=flat-square" alt="GitHub issues"/>
  <img src="https://img.shields.io/github/forks/zuhaz/discord.py-template?style=flat-square" alt="GitHub forks"/>
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome"/>
  <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=flat-square" alt="Made with Python"/>
  <img src="https://img.shields.io/github/contributors/zuhaz/discord.py-template?style=flat-square" alt="GitHub contributors"/>
  <img src="https://img.shields.io/github/last-commit/zuhaz/discord.py-template?style=flat-square" alt="GitHub last commit"/>
</p>

## Overview

This project is a versatile and extensible wrapper for discord.py, designed to simplify bot development. It provides a modular architecture with support for:

- Traditional commands
- Slash commands
- Select menus
- Modals
- Event handling

This handler serves as a template and toolkit to streamline the process of creating Discord bots using discord.py.

## Purpose

The discord.py library, while powerful, can be challenging for newcomers due to its extensive documentation and flexibility. This handler aims to:

1. Simplify the bot creation process
2. Provide a structured template for organizing bot components
3. Offer pre-built handlers for common Discord interactions
4. Demonstrate best practices in discord.py bot development

## Table of Contents

1. [Features](#features)
2. [Getting Started](#getting-started)
3. [Setup and Configuration](#setup-and-configuration)
4. [Creating Bot Components](#creating-bot-components)
   - [Commands](#commands)
   - [Slash Commands](#slash-commands)
   - [Modals](#modals)
   - [Select Menus](#select-menus)
   - [Event Listeners](#event-listeners)
5. [Logging](#logging)
6. [Troubleshooting](#troubleshooting)
7. [Contributing](#contributing)
8. [Support](#support)
9. [License](#license)
10. [References](#references)

## Features

- 🧩 Modular cog-based architecture
- 🔧 Support for traditional prefix commands
- 🔪 Slash command integration
- 📋 Select menu functionality
- 🖼️ Modal support for complex user interactions
- 🎭 Comprehensive event handling
- 📝 Logging system for debugging and monitoring
- ⚙️ Configuration management

## Getting Started

To use this handler for your Discord bot:

1. Clone this repository
2. Follow the setup instructions in the [Setup and Configuration](#setup-and-configuration) section
3. Start building your bot by adding your own commands, slash commands, modals, and event listeners in the respective directories
4. Customize the bot's functionality to suit your needs

For detailed instructions on creating each component type, refer to the relevant sections below.

## Project Structure

```
discord.py-template/
├── main.py
├── config.py
├── bot.py
├── .env (secured)
├── requirements.txt
├── cogs/
│   ├── commands/
│   ├── events/
│   ├── modals/
│   ├── select_menus/
│   └── slash_commands/ 
├── handlers/
│   ├── command_handler.py
│   ├── event_handler.py
│   ├── modal_handler.py
│   ├── select_menu_handler.py
│   └── slash_command_handler.py
├── utils/
│   ├── base_modal.py
│   ├── command_utils.py
│   ├── extension_utils.py
│   ├── helpers.py
│   ├── logger.py
│   └── logging_config.py
└── logs/
│   └── bot.log
└── data/
│   └── bot_data.json
```

## Setup and Configuration

1. Clone the repository:
   ```
   git clone https://github.com/zuhaz/discord.py-template.git
   ```
   Change the directory to the cloned repository:
   ```
   cd discord.py-template
   ```
2. Set up a virtual environment (optional but recommended):
   - On Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
   If you encounter any issues, try updating pip first:
   ```
   python -m pip install --upgrade pip
   ```

4. Set up your configuration:
   - Create a `.env` file in the project root directory.
   - Add the following essential configurations:

     ```
     DISCORD_BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN_HERE
     COMMAND_PREFIX=YOUR_PREFIX_HERE
     ```

   - Optional configuration:

     ```
     DEBUG=False
     BOT_STATUS=online
     BOT_ACTIVITY=Listening to !help
     ```
     - Replace `YOUR_DISCORD_BOT_TOKEN_HERE` with your actual Discord bot token.
     - Adjust the `COMMAND_PREFIX` as desired (default is `!`).
     - Set `DEBUG` to `True` for verbose logging (default is `False`).
     - Customize `BOT_STATUS` and `BOT_ACTIVITY` if desired.

5. Run the bot:

   There are several ways to run the bot, depending on your system and preferences:

   a. Using Python directly (works on Windows, macOS, Linux):
      ```
      python main.py
      ```
      or
      ```
      python3 main.py
      ```

   b. Using the Python module syntax (works on Windows, macOS, Linux):
      ```
      python -m main
      ```
      or
      ```
      python3 -m main
      ```

   c. On Windows, you can use the `py` launcher:
      ```
      py main.py
      ```

   d. On Linux or macOS, if you've made the script executable:
      ```
      chmod +x main.py
      ./main.py
      ```

   e. Using a virtual environment (recommended for all systems):
      - On Windows:
        ```
        venv\Scripts\activate
        python main.py
        ```
      - On macOS and Linux:
        ```
        source venv/bin/activate
        python main.py
        ```

   f. Using specific Python versions on Linux (if multiple versions are installed):
      ```
      python3.8 main.py
      python3.9 main.py
      python3.10 main.py
      ```

   g. Using `nohup` on Linux to run the bot in the background:
      ```
      nohup python3 main.py &
      ```

   h. Using `screen` on Linux to run the bot in a detachable session:
      ```
      screen -S discord_bot
      python3 main.py
      ```
      (Press Ctrl+A, then D to detach. Use `screen -r discord_bot` to reattach)

Choose the method that best suits your environment and setup. For production use on Linux servers, methods g or h are often preferred as they allow the bot to run continuously, even after closing the terminal session.

Note: Ensure you've invited the bot to your server with the necessary permissions, including the `applications.commands` scope for slash commands.
## Creating Bot Components

### Commands

Commands are created using the `commands.Cog` class and our custom `command_args` decorator. Here's an example of how to create a command cog with arguments, permissions, and cooldowns:

```python
import discord
from discord.ext import commands
from utils.command_utils import command_args

class ExampleCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @command_args(
        ("name", str, None),
        ("age", int, 0),
        ("is_member", bool, False),
        permissions={"send_messages": True},
        cooldown=(1, 5, commands.BucketType.user)
    )
    async def example(self, ctx, name: str, age: int, is_member: bool):
        """
        An example command with multiple arguments, permissions, and cooldown.

        Parameters:
        - name (str): The name of the user (required)
        - age (int): The age of the user (optional, default: 0)
        - is_member (bool): Whether the user is a member (optional, default: False)

        Usage:
            !example <name> [age] [is_member]
        """
        response = f"Hello, {name}! "
        if age > 0:
            response += f"You are {age} years old. "
        response += f"Member status: {is_member}"
        await ctx.send(response)

async def setup(bot):
    await bot.add_cog(ExampleCommands(bot))
```

#### Key Components:
- Use the `@commands.command()` decorator to define commands.
- Use the `@command_args()` decorator to specify argument types, default values, permissions, and cooldowns.
- The `ctx` parameter is a `commands.Context` object, providing context about the command invocation.

#### Defining Arguments:
The `@command_args()` decorator takes tuples for each argument, in the format:
```python
(argument_name, argument_type, default_value)
```
- `argument_name`: The name of the argument (string)
- `argument_type`: The expected type of the argument (e.g., str, int, bool)
- `default_value`: The default value if the argument is not provided (use None for required arguments)

#### Permissions:
Use the `permissions` parameter in the `@command_args()` decorator to specify required permissions. You can pass a dictionary of permission flags. For example:

```python
permissions={"manage_messages": True, "kick_members": True}
```

#### Cooldowns:
Use the `cooldown` parameter in the `@command_args()` decorator to specify cooldown rates. The parameter takes a tuple of three values:

```python
cooldown=(rate, per, type)
```

- `rate`: Number of uses allowed (int)
- `per`: Time period in seconds (float)
- `type`: The bucket type for the cooldown (commands.BucketType)

Bucket types include:
- `commands.BucketType.default`: Global cooldown
- `commands.BucketType.user`: Per-user cooldown
- `commands.BucketType.guild`: Per-guild cooldown
- `commands.BucketType.channel`: Per-channel cooldown
- `commands.BucketType.member`: Per-member cooldown (combination of user and guild)
- `commands.BucketType.category`: Per-category cooldown
- `commands.BucketType.role`: Per-role cooldown

#### Usage:
1. Place your command cogs in the `cogs/commands/` directory.
2. The bot will automatically load them on startup using the `CommandHandler`.

To use a command in Discord, type the command prefix followed by the command name and arguments:
```
!example Zuhaz 18 true
```

#### Expected Command Errors:

- Missing Required Argument: If a required argument is not provided, the bot will inform the user which argument is missing and show the correct usage.
- Invalid Argument Type: If an argument of the wrong type is provided, the bot will notify the user and show the correct usage.
- Missing Permissions: If a user doesn't have the required permissions, they will be notified.
- Cooldown: If a user tries to use a command too frequently, they will be informed of the remaining cooldown time.
- Other Errors: For any other errors, a generic error message will be displayed.

Example error messages:
```
Error: Missing required argument: name
Usage: !example <name> [age] [is_member]

Error: Invalid argument type. Please check the command usage.
Usage: !example <name> [age] [is_member]

Error: You don't have permission to use this command.

Error: This command is on cooldown. Please try again in 4.5 seconds.
```

### Slash Commands

Slash commands are created using the `discord.app_commands` module and our custom `slash_command_args` decorator. Here's an example of how to create a slash command cog with arguments, permissions, and cooldowns:

```python
import discord
from discord import app_commands
from discord.ext import commands
from utils.command_utils import slash_command_args

class ExampleSlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="example_slash", description="An example slash command with arguments")
    @app_commands.checks.cooldown(1, 5)  # 1 use per 5 seconds
    @app_commands.checks.has_permissions(send_messages=True)
    @slash_command_args(
        ("name", str, None),
        ("age", int, 0),
        ("is_member", bool, False)
    )
    async def example_slash_command(self, interaction: discord.Interaction, name: str, age: int, is_member: bool):
        """
        An example slash command that uses arguments.

        Parameters:
        - name (str): The name of the user (required)
        - age (int): The age of the user (optional, default: 0)
        - is_member (bool): Whether the user is a member (optional, default: False)

        Usage:
            /example_slash <name> [age] [is_member]
        """
        response = f"Hello, {name}! "
        if age > 0:
            response += f"You are {age} years old. "
        response += f"Member status: {is_member}"
        await interaction.response.send_message(response)

async def setup(bot):
    await bot.add_cog(ExampleSlashCommands(bot))
```

#### Key Components:
- Use the `@app_commands.command()` decorator to define slash commands.
- Use `@app_commands.checks.cooldown()` for cooldowns.
- Use `@app_commands.checks.has_permissions()` for permissions.
- Use the `@slash_command_args()` decorator to specify argument types and default values.
- The `interaction` parameter is a `discord.Interaction` object, representing the command invocation.

#### Defining Arguments:
The `@slash_command_args()` decorator takes tuples for each argument, in the format:
```python
(argument_name, argument_type, default_value)
```
- `argument_name`: The name of the argument (string)
- `argument_type`: The expected type of the argument (e.g., str, int, bool)
- `default_value`: The default value if the argument is not provided (use None for required arguments)

#### Permissions:
Use the `@app_commands.checks.has_permissions()` decorator to specify required permissions. You can pass one or more permission flags as keyword arguments. For example:

```python
@app_commands.checks.has_permissions(administrator=True) 
@app_commands.checks.has_permissions(manage_messages=True, kick_members=True)
```

Common permission flags includes (For both the `commands` and the `app_commands`):

- `administrator`
- `manage_guild`
- `manage_roles`
- `manage_channels`
- `kick_members`
- `ban_members`
- `manage_messages`
- `mention_everyone`
- `mute_members`
- `deafen_members`
- `move_members`
- `manage_nicknames`
- `manage_webhooks`
- `send_messages`
- `manage_emojis`

For a full list of permissions, refer to the [Discord API documentation](https://discordpy.readthedocs.io/en/latest/api.html#permissions).

#### Cooldowns:
Use the `@command.checks.cooldown()` decorator to specify cooldown rates. The decorator takes three arguments:

```python
@app_commands.checks.cooldown(rate, per)
```

- `rate`: Number of uses allowed (int)
- `per`: Time period in seconds (float)

#### Usage:
1. Place your slash command cogs in the `cogs/slash_commands/` directory.
2. The bot will automatically load and sync them on startup using the `SlashCommandHandler`.

To use a slash command in Discord, type `/` followed by the command name, and Discord will prompt you for the arguments:
```
/example_slash
```

#### Note on Slash Command Arguments:
Discord.py handles type conversion and validation for slash command arguments automatically. The `@slash_command_args()` decorator is primarily used for consistency with regular commands and to generate help text. Discord's UI will present appropriate input methods for different argument types (e.g., a dropdown for boolean values).

#### Expected Slash Command Errors:

- Missing Required Argument: If a required argument is not provided, the bot will inform the user which argument is missing and show the correct usage.
- Invalid Argument Type: If an argument of the wrong type is provided, the bot will notify the user and show the correct usage.
- Missing Permissions: If a user doesn't have the required permissions, they will be notified.
- Cooldown: If a user tries to use a command too frequently, they will be informed of the remaining cooldown time.
- Other Errors: For any other errors, a generic error message will be displayed.

Example error messages:
```
Error: You don't have permission to use this command.

Error: This command is on cooldown. Please try again in 4.5 seconds.
```

### Select Menus

Select menus are created using the `discord.ui.Select` class and our custom select menu handler. Here's a comprehensive guide to implementing select menus in your Discord bot:

```python
import discord
from discord.ui import Select, View
from utils.logger import get_logger

logger = get_logger(__name__)

class ExampleSelectMenu(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Option 1", description="This is the first option", value="1"),
            discord.SelectOption(label="Option 2", description="This is the second option", value="2"),
            discord.SelectOption(label="Option 3", description="This is the third option", value="3"),
        ]
        super().__init__(
            placeholder="Choose an option",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        selected_value = self.values[0]
        logger.info(f"User {interaction.user} selected option: {selected_value}")
        await interaction.response.send_message(f"You selected option {selected_value}!", ephemeral=True)

async def setup(bot):
    """Register the select menu with the bot's select menu handler."""
    bot.select_menu_handler.register_select_menu("example_menu", ExampleSelectMenu)
```

#### Key Components:
- Inherit from `discord.ui.Select` to create a custom select menu.
- Define options using `discord.SelectOption`.
- Implement the `callback` method to handle user selections.
- Use the `setup` function to register the select menu with the bot's handler.

#### Select Menu Configuration Parameters:

1. Select:
   - `custom_id` (str): Unique identifier for the select menu.
   - `placeholder` (str): Text displayed when no option is selected.
   - `min_values` (int): Minimum number of options that must be chosen.
   - `max_values` (int): Maximum number of options that can be chosen.

2. SelectOption:
   - `label` (str): The text displayed on the option. [Max: 100 characters]
   - `value` (str): The value associated with the option. [Max: 100 characters]
   - `description` (str, optional): Additional text shown for the option. [Max: 100 characters]
   - `emoji` (str or Emoji, optional): An emoji to display with the option.
   - `default` (bool, optional): Whether this option is selected by default.

#### Usage:
1. Place your select menu cogs in the `cogs/select_menus/` directory.
2. The bot will automatically load and register them on startup using the `SelectMenuHandler`.

To use a select menu in your bot:

For slash commands:
```python
@discord.slash_command()
async def example_select(self, interaction: discord.Interaction):
    view = discord.ui.View()
    view.add_item(self.bot.select_menu_handler.get_select_menu("example_menu"))
    await interaction.response.send_message("Choose an option:", view=view)
```

For prefix commands:
```python
@commands.command()
async def example_select(self, ctx):
    view = discord.ui.View()
    view.add_item(self.bot.select_menu_handler.get_select_menu("example_menu"))
    await ctx.send("Choose an option:", view=view)
```

#### Important Notes:
- Ensure that your callback method has the correct signature: `async def callback(self, interaction: discord.Interaction)`
- Remember to import necessary modules (discord) in your command files.

For further information and advanced usage, consult the [discord.py documentation on select menus](https://discordpy.readthedocs.io/en/stable/interactions/api.html#select-menus).

### Modals

Modals are created using the `discord.ui.Modal` class and our custom modal handler. Here's a comprehensive guide to implementing modals in your Discord bot:

```python
import discord
from utils.base_modal import BaseModal
from utils.logger import get_logger

logger = get_logger(__name__)

class ExampleModal(BaseModal):
    def __init__(self, *args, **kwargs):
        super().__init__(title="Example Modal", *args, **kwargs)
        self.add_item(discord.ui.TextInput(
            label="Sample Input",
            placeholder="Enter some text",
            style=discord.TextStyle.short,
            min_length=1,
            max_length=50,
            required=True
        ))

async def example_submit_handler(modal: ExampleModal, interaction: discord.Interaction):
    """Process the submitted modal data."""
    sample_input = modal.children[0].value
    
    logger.info(f"Modal submitted by {interaction.user}. Input: {sample_input}")
    
    await interaction.response.send_message(
        f"Thank you for your input: {sample_input}",
        ephemeral=True
    )

async def example_error_handler(modal: ExampleModal, interaction: discord.Interaction, error: Exception):
    """Handle any errors that occur during modal submission."""
    error_id = logger.error(f"Error in modal submission: {str(error)}", exc_info=True)
    
    await interaction.response.send_message(
        f"An error occurred (ID: {error_id}). Please try again later.",
        ephemeral=True
    )

async def setup(bot):
    """Register the modal with the bot's modal handler."""
    bot.modal_handler.register_modal(
        "example_modal",
        ExampleModal,
        submit_handler=example_submit_handler,
        error_handler=example_error_handler
    )
```

#### Key Components:
- Inherit from `BaseModal` (which extends `discord.ui.Modal`) to create a custom modal.
- Use `TextInput` to add input fields to your modal.
- Implement submit and error handler functions.
- Use the `setup` function to register the modal with the bot's handler.

#### Modal Configuration Parameters:

1. Modal:
   - `title` (str): Modal title. [Max: 45 characters]

2. TextInput:
   - `label` (str): Input field label. [Max: 45 characters]
   - `style` (TextStyle): Input style (short or paragraph).
   - `placeholder` (str, optional): Placeholder text. [Max: 100 characters]
   - `default` (str, optional): Default input value.
   - `required` (bool, optional): Input requirement flag. [Default: True]
   - `min_length` (int, optional): Minimum input length. [Range: 0-4000]
   - `max_length` (int, optional): Maximum input length. [Range: 1-4000]

3. ModalHandler.register_modal:
   - `name` (str): Unique identifier for the modal.
   - `modal_class` (type): The modal class to register.
   - `submit_handler` (callable): Function to process submissions.
   - `error_handler` (callable): Function to handle errors.

#### Usage:
1. Place your modal cogs in the `cogs/modals/` directory.
2. The bot will automatically load and register them on startup using the `ModalHandler`.

To use a modal in your bot:

For slash commands or other interaction-based commands:
```python
@discord.slash_command()
async def example_slash(self, interaction: discord.Interaction):
    modal = self.bot.modal_handler.get_modal("example_modal")
    await interaction.response.send_modal(modal)
```

For prefix commands (using a button to open the modal):
```python
@commands.command()
async def example_command(self, ctx):
    modal = self.bot.modal_handler.get_modal("example_modal")
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Open Modal", custom_id="open_modal"))
    await ctx.send("Click the button to open the modal:", view=view)

    def check(interaction):
        return interaction.data["custom_id"] == "open_modal" and interaction.user.id == ctx.author.id

    try:
        interaction = await self.bot.wait_for("interaction", check=check, timeout=60.0)
        await interaction.response.send_modal(modal)
    except asyncio.TimeoutError:
        await ctx.send("You didn't click the button in time.")
```

#### Important Notes:
- Ensure that your submit_handler and error_handler functions have the correct signatures:
  ```python
  async def submit_handler(modal: ExampleModal, interaction: discord.Interaction)
  async def error_handler(modal: ExampleModal, interaction: discord.Interaction, error: Exception)
  ```
- Remember to import necessary modules (discord, asyncio) in your command files.
- Modals are limited to 5 input fields. Plan your data collection accordingly.

For further information and advanced usage, consult the [discord.py documentation on modals](https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.Modal).

### Event Listeners

Event listeners are created using the `commands.Cog.listener()` decorator. Here's an example of how to create an event listener cog:

```python
import discord
from discord.ext import commands

class ExampleEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        An example event listener that responds to specific messages.
        """
        if message.author.bot:
            return

        if "hello" in message.content.lower():
            await message.channel.send("Hello there!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """
        An example event listener that welcomes new members.
        """
        welcome_channel = member.guild.system_channel
        if welcome_channel:
            await welcome_channel.send(f"Welcome to the server, {member.mention}!")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """
        An example event listener that handles command errors.
        """
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command not found. Use !help to see available commands.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing required argument: {error.param.name}")
        else:
            await ctx.send(f"An error occurred: {str(error)}")

async def setup(bot):
    await bot.add_cog(ExampleEvents(bot))
```

#### Key Components:
- Use the `@commands.Cog.listener()` decorator to define event listeners.
- The method name should match the event name (e.g., `on_message`, `on_member_join`, `on_command_error`).
- Each event provides specific parameters that you can use in your listener function.

#### Common Events:
- `on_message`: Triggered when a message is sent in a channel the bot can see.
- `on_member_join`: Triggered when a new member joins a server.
- `on_member_remove`: Triggered when a member leaves a server.
- `on_guild_join`: Triggered when the bot joins a new server.
- `on_reaction_add`: Triggered when a reaction is added to a message.
- `on_command_error`: Triggered when an error occurs during command execution.

#### Usage:
1. Place your event listener cogs in the `cogs/events/` directory.
2. The bot will automatically load them on startup using the `EventHandler`.

#### Important Notes:
- Be cautious with the `on_message` event, as it triggers for every message. Avoid heavy processing in this event to prevent performance issues.
- Use the `on_command_error` event to handle command-specific errors and provide user-friendly error messages.
- Remember to check if the message author is a bot in the `on_message` event to avoid potential loops.

For a complete list of events and their parameters, refer to the [discord.py API documentation](https://discordpy.readthedocs.io/en/stable/api.html#event-reference).

## Logging

Logs are stored in the `logs/` directory. The logging system is configured in `utils/logger.py`.

## Troubleshooting

- **Bot doesn't respond to commands:**
  - Ensure your bot token is correct in `config.py`.
  - Check if the bot has the necessary permissions in your Discord server.

- **Slash commands don't appear:**
  - It may take up to an hour for slash commands to propagate. Be patient!
  - Ensure you've invited the bot with the `applications.commands` scope.

- **Logs show connection errors:**
  - Check your internet connection.
  - Ensure Discord's API is not experiencing outages.

## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Write your code and tests.
4. Ensure all tests pass and your code adheres to PEP 8 style guidelines.
5. Submit a pull request with a clear description of your changes.

## Support

For support, please join the [Discord Server](https://discord.gg/7mhdvfgybX).


## Acknowledgements

This project wouldn't be possible without the amazing work of the discord.py developers and the broader Discord bot community. Special thanks to:

- [Rapptz](https://github.com/Rapptz) for creating and maintaining discord.py
- Contributors (me)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## References

- [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)
- [Discord Developer Portal](https://discord.com/developers/docs)
- [Discord.py Commands Framework](https://discordpy.readthedocs.io/en/stable/ext/commands/index.html)
- [Discord.py Application Commands](https://discordpy.readthedocs.io/en/stable/interactions/application_commands.html)
- [Discord.py UI Elements](https://discordpy.readthedocs.io/en/stable/interactions/ui_components.html)
---