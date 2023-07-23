#!/usr/bin/python3
"""Start a flak web app
"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage


app = Flask(__name__)
app.strict_slashes = False
data = storage.all('State').values()


@app.route('/states_list')
def state_list():
    """Get state list"""
    return render_template('7-states_list.html', states=data)


@app.teardown_appcontext
def session_close(close=None):
    """Close db session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
