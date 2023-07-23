#!/usr/bin/python3
"""Start a flak web app
"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models import State


app = Flask(__name__)
app.strict_slashes = False
data = storage.all('State').values()


@app.teardown_appcontext
def session_close(close):
    """Close db session"""
    storage.close()


@app.route('/states_list')
def state_list():
    """Get state list"""
    return render_template('7-states_list.html', states=data)


@app.route('/cities_by_states')
def city_list():
    """Get city lists"""
    return render_template('8-cities_by_states.html', states=data)





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
