# -*- coding: utf-8 -*-
from app import app
from flask import url_for, render_template


@app.route('/')
def index():
	"""Return Cebolinha Translator WebApp"""
	github_icon = url_for('.static', filename='github.svg')
	return render_template('index.html', ic_github=github_icon)
