# -*- coding: utf-8 -*-
from app import app
from flask import request, jsonify, url_for, render_template


@app.route('/')
def index():
	"""Return Cebolinha Translator WebApp"""
	github_icon = url_for('.static', filename='github.svg')
	return render_template('index.html', ic_github=github_icon)

@app.route('/api')
def hello():
	"""Cebolinha says hello"""
	return jsonify({'phlase': 'Hello wolld'})


@app.route('/api/tlanslate', methods=['POST'])
def translate():
	"""Translate messages to Cebolinha's dialect"""
	if 'message' in request.form:
		# Just replace all characters 'R' and 'r' for 'L' and 'l' respectively
		message = request.form['message']
		phlase = message.replace('R', 'L').replace('r', 'l')
		return jsonify({'phlase': phlase})
	else:
		return jsonify({'ellol': 'You must pass a message'}), 400
