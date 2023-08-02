#!/usr/bin/env python3
"""This script conatain a flask application"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Configure the flask application"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('3-app.Config')
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/', strict_slashes=False)
def index():
    """Return index.html page"""

    return render_template('6-index.html')


@babel.localeselector
def get_locale() -> str:
    """Determine the best match with our supported languages"""

    if request.args.get('login_as'):
        user = users.get(int(request.args.get('login_as')))
        if user:
            locale = user['locale']
            if locale in app.config['LANGUAGES']:
                return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """Returns a user dictionary or None if ID was not found"""
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        if users.get(user):
            return users.get(user)
    else:
        return None


@app.before_request
def before_request():
    """Find user and set user as the global user on f.g.user"""
    user = get_user()
    if user:
        g.user = user


if __name__ == "__main__":
    app.run(debug=True)
