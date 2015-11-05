# -*- coding: utf-8 -*-
from flask import Blueprint

# Initializes the blueprint
api = Blueprint('api', __name__)

# Import application's views (a.k.a. routes)
from api import views
