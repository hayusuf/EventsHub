"""BOB Dylan."""
import pathlib
# import arrow
import flask
from flask import send_from_directory, request, redirect
import eventsAI

@eventsAI.app.route('/', methods=['get'])
def show_index():
    
    context = {}
    return flask.render_template("index.html", **context)
