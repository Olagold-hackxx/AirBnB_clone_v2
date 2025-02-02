#!/usr/bin/python3
"""Start a flak web app
"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage

app = Flask(__name__)
app.strict_slashes = False


@app.teardown_appcontext
def session_close(close):
    storage.close()


@app.route('/states')
def state():
    data = storage.all('State')
    return render_template('9-states.html', states=data)


@app.route('/states/<id>')
def state_id(id):
    data = storage.all('State').values()
    for state in data:
        if state.id == id:
            return render_template("9-states.html", states=state)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
