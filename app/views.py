# -*- coding: utf-8 -*-
from app import app
from flask import request, jsonify, url_for, render_template


@app.route('/')
def index():
    """Return Cebolinha Translator WebApp"""
    logo = url_for('.static', filename='images/logo.svg')
    github_icon = url_for('.static', filename='images/github.svg')
    js = url_for('.static', filename='js/main.js')
    return render_template(
        'index.html',
        ic_github=github_icon,
        ic_logo=logo,
        js_main=js
    )


@app.route('/api')
def hello():
    """Cebolinha says hello"""
    return jsonify({'phlase': 'Hello wolld'})


@app.route('/api/tlanslate', methods=['POST'])
def translate():
    """Translate messages to Cebolinha's dialect"""

    # Message to be translated
    message = None

    # If message was passed as json object
    if request.headers['content-type'].lower().find('application/json') > -1:
        data = request.get_json()
        message = data['message']

    # If message was passed inside a form
    elif 'message' in request.form:
        message = request.form['message']

    if message is not None:
        # Just replace all characters 'R' and 'r' for 'L' and 'l' respectively
        phlase = message.replace('R', 'L').replace('r', 'l')
        return jsonify({'phlase': phlase})
    else:
        return jsonify({'ellol': 'You must pass a message'}), 400
