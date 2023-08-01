#!/usr/bin/env python3
"""This script conatain a flask application"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Return index.html page"""

    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
