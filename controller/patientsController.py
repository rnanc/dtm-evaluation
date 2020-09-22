from flask import Blueprint, render_template, url_for

patients_blueprint = Blueprint('patients', __name__, template_folder='templates', static_folder='static')

@patients_blueprint.route('/patients')
def patientsPage():
  return render_template('list.html')
