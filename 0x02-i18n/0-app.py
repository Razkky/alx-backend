#!/usr/bin/env python3
"""This script conatain a flask application"""
from flask import Flask, render_template


app = Flask(__name__, strict_slashes=False)


@app.route('/')
def index():
    """Return index.html page"""

    return render_template('index.html')


if __name__ == "__main__":
    app.run()
