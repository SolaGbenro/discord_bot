
import os
import discord
import logging
from typing import Tuple

import openai
from dotenv import load_dotenv
from app.chatgpt_ai.openai_refactored import chatgpt_response

logging.basicConfig(level=logging.INFO)


class MyClient(discord.Client):
    async def on_ready(self):
        logging.info(f"Successfully logged in as: {self.user}")

    async def on_message(self, message: discord.Message):
        logging.info(f"Received message: {message.content}")

        # Ignore messages from the bot itself
        if message.author == self.user:
            return

        command, user_message = self.parse_message(message.content)

        if command:
            try:
                bot_response = chatgpt_response(prompt=user_message)
                await message.channel.send(f"Answer: {bot_response}")
            except Exception as e:
                logging.error(f"Error generating response: {e}")

    @staticmethod
    def parse_message(message_content: str) -> Tuple[str, str]:
        command, user_message = '', ''
        initializing_command_list = ["/ai", "/bot", "/gpt"]
        for initializing_command in initializing_command_list:
            if message_content.startswith(initializing_command):
                command = message_content.split(' ')[0]
                user_message = message_content.replace(initializing_command, '').strip()
        return command, user_message


def main():
    # Load environment variables
    load_dotenv()

    # Fetch the Discord token from environment variables
    discord_token = os.getenv('DISCORD_TOKEN')
    if not discord_token:
        raise ValueError("DISCORD_TOKEN not found in environment variables")

    # Set the OpenAI API key
    openai.api_key = os.getenv('OPENAI_API_KEY')
    if not openai.api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")

    intents = discord.Intents.default()
    intents.message_content = True

    # Instantiate the client and start the bot
    client = MyClient(intents=intents)
    client.run(discord_token)


if __name__ == "__main__":
    main()
