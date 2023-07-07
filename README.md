## Introduction

This is a simple Discord bot that integrates with OpenAI's GPT-3 model. The bot responds to commands prefixed by `/ai`, `/bot`, or `/gpt` and provides sarcastic and humorous responses based on the user's input.

## File Structure

The project is structured into three Python files:

1. `run.py`: The main executable file that runs the bot.
2. `discord_api.py`: Defines the Discord bot class, `MyClient`, that handles Discord events.
3. `openai.py`: A utility file that integrates with OpenAI's GPT-3 API.

## Getting Started

To run this bot, follow the instructions below.

### Prerequisites

1. **Python 3.7+**: The bot is written in Python, so you'll need a Python environment to run it. You can download Python [here](https://www.python.org/downloads/).

2. **Discord Bot Token**: You'll need to create a bot on Discord's developer portal and get a token. You can follow the guide [here](https://discordpy.readthedocs.io/en/stable/discord.html).

3. **OpenAI API Key**: You'll need an API key from OpenAI to use the GPT-3 model. You can follow the guide [here](https://beta.openai.com/docs/developer-quickstart/).

### Installation

1. **Clone the repository**: Clone this repository to your local machine using `git clone`.

2. **Set up a virtual environment**: (Optional) You can set up a virtual environment to keep the dependencies required by this project separate from your other Python projects. Here's how you can do it:

    - Install the virtual environment wrapper: `pip install virtualenv`
    - Navigate to the project directory and create a virtual environment: `virtualenv venv`
    - Activate the virtual environment:
        - On Windows: `.env\Scriptsctivate`
        - On Unix or MacOS: `source venv/bin/activate`

3. **Install the dependencies**: Install the necessary Python packages using pip:

    ```
    pip install discord.py python-dotenv openai
    ```

### Configuration

Create a `.env` file in the root directory of the project. This file should contain the following two lines:

```
DISCORD_TOKEN=<Your Discord Bot Token>
OPENAI_API_KEY=<Your OpenAI API Key>
```

Replace `<Your Discord Bot Token>` and `<Your OpenAI API Key>` with your actual Discord bot token and OpenAI API key, respectively.

### Running the Bot

With the dependencies installed and the `.env` file set up, you're ready to run the bot.

1. Navigate to the project directory in your terminal.
2. Run `python run.py`.

The bot should now be running. Check your Discord server to see if the bot is online.

### Interacting with the Bot

Once the bot is online, it will respond to messages that start with `/ai`, `/bot`, or `/gpt`. For example, if you type `/ai What's the weather today?`, the bot will respond with a sarcastic and humorous message.

## Code Overview

The bot's logic is spread across three Python files: `run.py`, `discord_api.py`, and `openai.py`.

- `run.py` is the entry point of the bot. It imports the `client` object from `discord_api.py` and runs the bot with the token defined in the `.env` file.
- `discord_api.py` defines the `MyClient` class, a subclass of `discord.Client`. The `on_ready` method is called when the bot successfully logs into Discord, and the `on_message` method is called whenever a message is sent in a channel that the bot has access to. If a message starts with `/ai`, `/bot`, or `/gpt`, the bot sends a request to the OpenAI API and responds with the generated message.
- `openai.py` defines the `chatgpt_response` function, which sends a request to the OpenAI API and returns the generated response.

## Disclaimer

This bot is designed to provide sarcastic and humorous responses, and it's not intended to provide serious or helpful answers. Please use it responsibly.

## License

This project is licensed under the terms of the MIT license.
