from flask import Blueprint, request, jsonify
from .openai_client import summarize_text

app = Blueprint('routes', __name__)


@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text', '')
    summary = summarize_text(text)
    return jsonify({'summary': summary})
