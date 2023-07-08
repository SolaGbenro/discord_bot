
import os
import openai
import logging
from dotenv import load_dotenv
from typing import Optional

# Set up logging
logging.basicConfig(level=logging.INFO)

# System prompt for the chat model
SYSTEM_PROMPT = """You're a sarcastic but still helpful Discord bot with plenty of personality! Express it in your 
responses but keep them humours and short. """


def chatgpt_response(prompt: str, model: str = "gpt-3.5-turbo-0613") -> Optional[str]:
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        return None


def main():
    # Load environment variables
    load_dotenv()

    # Set the OpenAI API key
    openai.api_key = os.getenv('OPENAI_API_KEY')
    if not openai.api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")


if __name__ == "__main__":
    main()
