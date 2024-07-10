from flask import Flask
from .openai_client import summarize_text
from .routes import app as routes_blueprint

app = Flask(__name__)
app.register_blueprint(routes_blueprint)
