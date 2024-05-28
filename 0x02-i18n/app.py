#!/usr/bin/env python3
"""Basic Babel setup"""
import pytz
from datetime import datetime
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _, format_datetime
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
    # Locale from URL parameters
    locale: Optional[str] = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # Locale from user settings
    user = getattr(g, 'user', None)
    if user and user.get('locale') in app.config['LANGUAGES']:
        return user.get('locale')

    # Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone() -> str:
    """Determine the best match for supported time zones."""
    # Timezone from URL parameters
    timezone: Optional[str] = request.args.get('timezone')
    if timezone and timezone in pytz.all_timezones:
        return timezone

    # Timezone from user settings
    user = getattr(g, 'user', None)
    if user and user.get('timezone') in pytz.all_timezones:
        return user.get('timezone')

    # Default to UTC
    return 'UTC'


@app.before_request
def before_request() -> None:
    """Set the user and timezone in the global context if logged in."""
    g.user = get_user()
    g.timezone = get_timezone()


@app.route('/')
def index() -> str:
    """Returns a rendered template"""
    current_time = datetime.now(pytz.timezone(g.timezone))
    formatted_time = format_datetime(current_time)
    return render_template('index.html', current_time=formatted_time)


if __name__ == "__main__":
    app.run()
