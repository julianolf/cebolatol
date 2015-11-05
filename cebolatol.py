# -*- coding: utf-8 -*-
from flask import Flask
from api import api

# Create new Flask application
app = Flask(__name__)

# Register blueprints
app.register_blueprint(api, url_prefix='/api')

if __name__ == "__main__":
	# Runs server in debug mode with external visibility
    app.run(host='0.0.0.0', debug=True)
