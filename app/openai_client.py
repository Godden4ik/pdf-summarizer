import openai
from dotenv import load_dotenv

load_dotenv()

# https://github.com/openai/openai-python/blob/main/examples/demo.py

client = openai.OpenAI()


def summarize_text(text):
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize the text below.\n\n{text}",
                },
            ],
        )
        return chat_completion.choices[0].message.content
    except openai.OpenAIError as e:
        return str(e)
