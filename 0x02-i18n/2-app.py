#!/usr/bin/env python3
"""This script conatain a flask application"""
from flask import Flask, render_template
from flask_babel import Babel
import requests

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configure the flask application"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('1-app.Config')


def get_locale():
    """Determine the best match with our supported languages"""
    return requests.accept_language.best_match(app.Config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """Return index.html page"""

    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True)
