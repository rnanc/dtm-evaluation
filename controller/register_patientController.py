from flask import Blueprint, render_template, url_for

register_blueprint = Blueprint('register', __name__, template_folder='templates', static_folder='static')

@register_blueprint.route('/register')
def detailsPage():
  return render_template('register_patient.html')
