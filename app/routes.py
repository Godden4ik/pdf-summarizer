from PyPDF2 import PdfReader
from flask import Blueprint, request, jsonify
from .openai_client import summarize_text

app = Blueprint('routes', __name__)


@app.route('/summarize', methods=['POST'])
def summarize():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded. Please upload a PDF file'})

    file = request.files['file']

    if file and file.filename.endswith('.pdf'):
        try:
            # https://pypdf2.readthedocs.io/en/3.x/user/extract-text.html
            pdf_reader = PdfReader(file.stream)
            text = pdf_reader.pages[0].extract_text()

            summary = summarize_text(text)
            return jsonify({'summary': summary})

        except Exception as e:
            return jsonify({'error': str(e)})

    else:
        return jsonify({'error': 'Unsupported file format, must be a PDF file'})
