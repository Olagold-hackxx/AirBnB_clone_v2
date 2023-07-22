#!/usr/bin/python3
from flask import Flask
"""
Start a flak web app
"""
app = Flask(__name__)
app.strict_slashes = False


@app.route('/', strict_slashes="false")
def hello():
    """route to root
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
