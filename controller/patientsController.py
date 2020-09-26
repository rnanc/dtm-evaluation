from flask import Blueprint, render_template, url_for
from flask_jwt_extended import jwt_required

patients_blueprint = Blueprint('patients', __name__, template_folder='templates', static_folder='static')

@patients_blueprint.route('/patients')
@jwt_required
def patientsPage():
  return render_template('patientList.html')
