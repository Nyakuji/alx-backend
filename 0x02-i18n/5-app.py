#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _
from typing import Optional, Dict, Union

# Initialize the Flask application
app = Flask(__name__)

# Define the users table
users: Dict[int, Dict[str, Union[str, None]]] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> Optional[Dict[str, Union[str, None]]]:
    """Retrieve a user dictionary based on the login_as parameter."""
    user_id: Optional[str] = request.args.get('login_as')
    if user_id is None:
        return None
    try:
        user_id = int(user_id)
        return users.get(user_id)
    except (ValueError, KeyError):
        return None


class Config(object):
    """Config app class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Apply the configuration to the Flask app
app.config.from_object(Config)

babel = Babel(app)


def get_locale() -> Optional[str]:
    """Determine the best match for supported languages."""
    user = getattr(g, 'user', None)
    if user and user.get('locale') in app.config['LANGUAGES']:
        return user.get('locale')
    locale: Optional[str] = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.before_request
def before_request() -> None:
    """Set the user in the global context if logged in."""
    g.user = get_user()


@app.route('/')
def index() -> str:
    """Returns a rendered template"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()