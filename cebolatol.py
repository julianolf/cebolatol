# -*- coding: utf-8 -*-
from flask import Flask
from app import app
from api import api

# Create new Flask application
cebolatol = Flask(__name__)

# Register blueprints
cebolatol.register_blueprint(app)
cebolatol.register_blueprint(api, url_prefix='/api')

if __name__ == "__main__":
	# Runs server in debug mode with external visibility
    cebolatol.run(host='0.0.0.0', debug=True)
