from flask import Blueprint
import random
import os

views = Blueprint("auth", __name__)

@views.route("/running")
def home():
    return "<h1>404!~</h1>"

    