import openai
from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

client = OpenAI()


def summarize_text(text):
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"{text}\n\nThe summary of the above text is:",
                },
            ],
        )
        return chat_completion.choices[0].message.content
    except openai.OpenAIError as e:
        return str(e)


@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text', '')
    summary = summarize_text(text)
    return jsonify({'summary': summary})


if __name__ == '__main__':
    app.run(debug=True)
