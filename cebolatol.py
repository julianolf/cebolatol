# -*- coding: utf-8 -*-
from app import app, views

if __name__ == "__main__":
	# Runs server in debug mode with external visibility
    app.run(host='0.0.0.0', debug=True)
