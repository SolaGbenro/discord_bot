
import os
import openai
import logging
from dotenv import load_dotenv
from typing import Dict, Optional
import json
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)

# System prompt for the chat model
SYSTEM_PROMPT = """You're a sarcastic but still helpful Discord bot with plenty of personality! Express it in your 
responses while keeping them humorous and short."""


def update_token_usage(response: Dict, filename: str) -> None:
    """
    Update the token usage in a text file. If the text file does not exist, it will be created.
    
    Args:
        response (Dict): The response object from the chat model.
        filename (str): The name of the file where token usage is stored.
    """
    # Get today's date and convert it to string
    today = datetime.today().strftime('%Y-%m-%d')

    # Extract total tokens used from the response
    total_tokens_used = response.get('usage', {}).get('total_tokens', 0)

    # Try to read the existing data from the file
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file does not exist or cannot be read, create a new dictionary
        data = {}

    # Update the token count for today's date or add a new date with the token count
    data[today] = data.get(today, 0) + total_tokens_used

    # Write the updated data back to the file
    with open(filename, 'w') as file:
        json.dump(data, file)


def chatgpt_response(prompt: str, model: str = "gpt-3.5-turbo-0613") -> Optional[str]:
    """
    Generate a response using the GPT-3 model.

    Args:
        prompt (str): The user's input.
        model (str, optional): The model to be used. Defaults to "gpt-3.5-turbo-0613".

    Returns:
        Optional[str]: The generated response, or None if an error occurred.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=400
        )
        # Update the token usage
        update_token_usage(response, "outputs/token_usage.txt")
        return response['choices'][0]['message']['content']
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        return None


def main() -> None:
    """
    Load environment variables and set the OpenAI API key.
    """
    # Load environment variables
    load_dotenv()

    # Set the OpenAI API key
    openai.api_key = os.getenv('OPENAI_API_KEY')
    if not openai.api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")


if __name__ == "__main__":
    main()
    