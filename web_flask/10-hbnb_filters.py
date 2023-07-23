#!/usr/bin/python3
"""Start a flak web app
"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models import State


app = Flask(__name__)
app.strict_slashes = False
states = storage.all('State').values()
amenities = storage.all('Amenity').values()


@app.teardown_appcontext
def session_close(close):
    storage.close()


@app.route('/hbnb_filters')
def state():
    return render_template('10-hbnb_filters.html', data=[states, amenities])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
