from flask import Blueprint

details = Blueprint("details", __name__, static_folder='../static', template_folder='../template')

from . import views
