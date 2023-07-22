#!/usr/bin/python3
"""
Start a flak web app
"""
from flask import Flask
app = Flask(__name__)
app.strict_slashes = False


@app.route('/', strict_slashes="false")
def hello():
    """route to root
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
