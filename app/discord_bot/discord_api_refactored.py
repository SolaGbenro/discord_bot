
import os
import discord
import logging
import re
from typing import Tuple
import openai
from dotenv import load_dotenv
from app.chatgpt_ai.openai_refactored import chatgpt_response

# Set up logging
logging.basicConfig(level=os.getenv('LOGGING_LEVEL', 'INFO'))


class MyClient(discord.Client):
    async def on_ready(self) -> None:
        """
        Event handler for when the bot has connected to the server and is ready.
        """
        logging.info(f"Successfully logged in as: {self.user}")

    async def on_message(self, message: discord.Message) -> None:
        """
        Event handler for new messages from users.

        Parameters:
        message (discord.Message): The message that was sent.
        """
        logging.info(f"Received message: {message.content}")

        # Ignore messages from the bot itself
        if message.author == self.user:
            return

        command, user_message = self.parse_message(message.content)

        if command:
            try:
                bot_response = chatgpt_response(prompt=user_message)
                await message.channel.send(f"Answer: {bot_response}")
            except openai.api.OpenAIAPIError as e:
                logging.error(f"Error from OpenAI API: {e}")
            except Exception as e:
                logging.error(f"Unexpected error occurred: {e}")

    @staticmethod
    def parse_message(message_content: str) -> Tuple[str, str]:
        """
        Parses a message content to extract command and user's message.

        Parameters:
        message_content (str): The content of the message.

        Returns:
        Tuple[str, str]: A tuple containing the command and the user's message.
        """
        match = re.match(r'^(\/ai|\/bot|\/gpt)(.*)$', message_content)
        if match:
            return match.group(1), match.group(2).strip()
        return '', ''


def main() -> None:
    """
    Main function that starts the Discord bot.
    """
    # Load environment variables
    load_dotenv()

    # Fetch the Discord token from environment variables
    discord_token = os.getenv('DISCORD_TOKEN')
    if not discord_token:
        raise ValueError("DISCORD_TOKEN not found in environment variables. Please set it.")

    # Set the OpenAI API key
    openai.api_key = os.getenv('OPENAI_API_KEY')
    if not openai.api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables. Please set it.")

    intents = discord.Intents.default()
    intents.message_content = True

    # Instantiate the client and start the bot
    client = MyClient(intents=intents)
    client.run(discord_token)


if __name__ == "__main__":
    main()
