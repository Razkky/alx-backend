#!/usr/bin/env python3
"""This script conatain a flask application"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Configure the flask application"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('3-app.Config')


@app.route('/', strict_slashes=False)
def index():
    """Return index.html page"""

    return render_template('3-index.html')


@babel.localeselector
def get_locale() -> str:
    """Determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True)
