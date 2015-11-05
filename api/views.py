# -*- coding: utf-8 -*-
from api import api
from flask import jsonify


@api.route('/')
def hello():
	"""Cebolinha says hello"""
	return jsonify({'flase': 'hello wolld'})
