from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """route to root"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """route to /hbnb"""
    return "HBNB"


@app.route('/c/<input>')
def c_is_fun(input):
    """route to c/"""
    return f"C {escape(input.replace('_', ' '))}"


@app.errorhandler(404)
def not_found(error=None):
    """404 error handler"""
    return render_template("error.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
