#!/usr/bin/python3
"""Start a flak web app
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)
app.strict_slashes = False


@app.route('/')
def hello():
    """route to root
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """route to hbnb
    """
    return "HBNB"


@app.route('/c/<input>')
def c_is_fun(input):
    """route to c/
    """
    return f"C {escape(input.replace('_', ' '))}"


@app.route('/python/<text>')
def python_is_cool(text='is_cool'):
    """route to python/
    """
    return f"Python {escape(text.replace('_', ' '))}"


@app.route('/python/')
def python_default():
    """route to hbnb
    """
    return "Python is cool"


@app.route('/number/<int:n>')
def number(n):
    """route to number
    """
    return f"{escape(n)} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

