import discord
from utils.base_modal import BaseModal
from utils.logger import get_logger

logger = get_logger(__name__)

class ExampleModal(BaseModal):
    def __init__(self, *args, **kwargs):
        super().__init__(title="Example Modal", *args, **kwargs)
        self.add_item(
            discord.ui.TextInput(
                label="Sample Input",
                placeholder="Enter some text",
                style=discord.TextStyle.short,
                min_length=1,
                max_length=50,
                required=True,
            )
        )

async def example_submit_handler(modal: ExampleModal, interaction: discord.Interaction):
    sample_input = modal.children[0].value

    logger.info(f"Modal submitted by {interaction.user}. Input: {sample_input}")

    await interaction.response.send_message(
        f"Thank you for your input: {sample_input}", ephemeral=True
    )

async def example_error_handler(
    modal: ExampleModal, interaction: discord.Interaction, error: Exception
):
    error_id = logger.error(f"Error in modal submission: {str(error)}", exc_info=True)

    await interaction.response.send_message(
        f"An error occurred (ID: {error_id}). Please try again later.", ephemeral=True
    )

# IMPORTANT: This function is required to register the modal with the bot.
# It does the following:
# 1. Defines a setup function that takes the bot as an argument.
# 2. Uses the bot's modal_handler to register the modal.
# 3. Specifies four key components:
#    a. "example_modal": A custom name used to call this modal elsewhere in the code.
#    b. ExampleModal: The class that defines the structure of the modal.
#    c. submit_handler: The function to be called when the modal is submitted successfully.
#    d. error_handler: The function to be called if an error occurs during submission.
# This setup allows the bot to create and manage this modal when needed.
async def setup(bot):
    bot.modal_handler.register_modal(
        "example_modal",
        ExampleModal,
        submit_handler=example_submit_handler,
        error_handler=example_error_handler,
    )
