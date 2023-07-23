#!/usr/bin/python3
"""Start a flak web app
"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models import State


app = Flask(__name__)
app.strict_slashes = False


@app.teardown_appcontext
def session_close(close):
    storage.close()


@app.route('/hbnb')
def state():
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    places = storage.all('Place').values()
    return render_template('100-hbnb.html', data=[states, amenities, places])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
