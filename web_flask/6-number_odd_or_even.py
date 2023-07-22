#!/usr/bin/python3
"""Start a flak web app
"""
from flask import Flask, render_template
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
def c_var(input):
    """route to c/
    """
    return f"C {escape(input.replace('_', ' '))}"


@app.route('/python/<text>')
def python_var(text='is_cool'):
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


@app.route('/number_template/<int:n>')
def number_template(n):
    """render with template
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """render with template
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

