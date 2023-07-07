from dotenv import load_dotenv
import openai
import os

# load env variables
load_dotenv()
# load openai key
openai.api_key = os.getenv('OPENAI_API_KEY')


def chatgpt_response(prompt, model="gpt-3.5-turbo-0613"):
    sys_prompt = """You're a sarcastic and unhelpful Discord bot with plenty of personality! Express it in your 
    responses but keep them humours and short."""
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']

