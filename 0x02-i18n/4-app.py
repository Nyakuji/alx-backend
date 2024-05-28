#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template, request
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

babel = Babel(app)


def get_locale() -> str:
    """Get locale from request"""
    # Check if 'locale' parameter is provided in the URL and if it's a
    # supported locale
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # If not, fall back to the default behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Returns a rendered template"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
