from flask import Blueprint, render_template, url_for, make_response, redirect
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, set_access_cookies, jwt_optional

patients_blueprint = Blueprint('patients', __name__, template_folder='templates', static_folder='static')

@patients_blueprint.route('/dashboard')
@jwt_required
def dashboard():
  return render_template('dashboard.html')

@patients_blueprint.route('/register_patient')
@jwt_required
def register_patient():
  return render_template('register_patient.html')


