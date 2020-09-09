from flask import Blueprint

patients = Blueprint('patients', __name__, static_folder='../static', template_folder='../template')

from . import views