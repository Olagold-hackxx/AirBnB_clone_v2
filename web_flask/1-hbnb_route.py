#!/usr/bin/python3
from flask import Flask
"""Start a flak web app"""

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """route to root"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """route to hbnb"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
