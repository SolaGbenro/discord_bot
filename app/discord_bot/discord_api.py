from dotenv import load_dotenv
import discord
import os
# using the app/chatgpt_ai/__init__.py file allows us to extract custom response function from openai.py
from app.chatgpt_ai.openai import chatgpt_response

# load env variables
load_dotenv()
# discord env
discord_token = os.getenv('DISCORD_TOKEN')


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Successfully logged in as: {self.user}")

    async def on_message(self, message):
        print(f"{message.content}")

        if message.author == self.user:
            return

        command, user_message = '', ''
        initializing_command_list = ["/ai", "/bot", "/gpt"]
        for initializing_command in initializing_command_list:
            if message.content.startswith(initializing_command):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(initializing_command, '').strip()

        if command in initializing_command_list:
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(f"Answer: {bot_response}")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
