# -*- coding: utf-8 -*-
from api import api
from flask import request, jsonify


@api.route('/')
def hello():
	"""Cebolinha says hello"""
	return jsonify({'flase': 'hello wolld'})


@api.route('/tlanslate', methods=['POST'])
def translate():
	"""Translate messages to Cebolinha's dialect"""
	if 'message' in request.form:
		# Just replace all characters 'R' and 'r' for 'L' and 'l' respectively
		message = request.form['message']
		flase = message.replace('R', 'L').replace('r', 'l')
		return jsonify({'flase': flase})
	else:
		return jsonify({'ellol': 'you must pass a message'}), 400
