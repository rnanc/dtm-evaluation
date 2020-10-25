from flask import Blueprint, render_template, url_for, make_response, redirect, request, redirect
from flask_jwt_extended import jwt_required
from config.serializer import PatientSchema

from model.Model import Patient
from model.Model import Users

from flask import current_app

patients_blueprint = Blueprint('patients', __name__, template_folder='templates', static_folder='static')

@patients_blueprint.route('/dashboard')
@jwt_required
def dashboard():
  patients = Patient.query.all()
  return render_template('dashboard.html', patients=patients)

@patients_blueprint.route('/register_patient', methods=['GET', 'POST'])
@jwt_required
def register():
  if request.method == "POST":
    patient = PatientSchema()
    patients_info = request.form.to_dict()
    user_query = Users.query.filter(Users.id==int(request.cookies.get("user_id"))).first()
    patients_load = patient.load(patients_info)
    current_app.db.session.add(patients_load)
    user_query.patients.append(patients_load)
    current_app.db.session.commit()
    return redirect(url_for('patients.dashboard'))

@patients_blueprint.route('/show_register', methods=['GET'])
@jwt_required
def show_register():
  if request.method == "GET":
    return render_template('register_patient.html')

@patients_blueprint.route('/edit/<int:id>', methods=['GET', 'POST'])
@jwt_required
def edit(id):
  patient = Patient.query.get(id)
  if request.method == 'POST':
    patient.name = request.form['name']
    patient.email = request.form['email']
    patient.phone = request.form['phone']
    patient.age = request.form['age']
    current_app.db.session.commit()
    return redirect(url_for('index'))
  return render_template('edit.html', patient = patient)

@patients_blueprint.route('/edit_patient')
@jwt_required
def edit_patient():
  return render_template('edit_patient.html')
