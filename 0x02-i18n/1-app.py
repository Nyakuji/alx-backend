#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template
from flask_babel import Babel, gettext as _

# Initialize the Flask application
app = Flask(__name__)


class Config(object):
    """Config app class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Apply the configuration to the Flask app
app.config.from_object(Config)

# Instantiate Babel and store it in a module-level variable
babel = Babel(app)


@app.route('/')
def index() -> str:
    """Returns a rendered template"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
