# -*- coding: utf-8 -*-
from app import app
from flask import render_template


@app.route('/')
def index():
	"""Return Cebolinha Translator WebApp"""
	return render_template('index.html')
