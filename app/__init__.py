# -*- coding: utf-8 -*-
from flask import Blueprint

# Initializes the blueprint
app = Blueprint('app', __name__, template_folder='templates', static_folder='static')

# Import application's views (a.k.a. routes)
from app import views
