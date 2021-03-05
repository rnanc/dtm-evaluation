from flask import Blueprint, render_template, url_for, make_response, redirect, request, redirect
from flask_jwt_extended import jwt_required
from config.serializer import PatientSchema
from model.Model import Patient
from model.Model import Exam

from flask import current_app

patients_blueprint = Blueprint('patients', __name__, template_folder='templates', static_folder='static')


@patients_blueprint.route('/dashboard')
@jwt_required
def dashboard():
  patients = Patient.query.all()
  return render_template('dashboard.html', patients=patients)


@patients_blueprint.route('/register_patient', methods=['GET', 'POST'])
@jwt_required
def register_patient():
  if request.method == "GET":
    return render_template('register_patient.html')
  else:
    patient = PatientSchema()
    patients_info = request.form.to_dict()
    patients_load = patient.load(patients_info)
    current_app.db.session.add(patients_load)
    current_app.db.session.commit()
    return redirect(url_for('patients.dashboard'))


@patients_blueprint.route('/edit_patient', methods=["GET", "POST"])
@jwt_required
def edit_patient():
  if request.method == "GET":
    id = request.cookies.get("patient_id")
    patient = Patient.query.get(id)
    return render_template("edit_patient.html", patient=patient)
  else:
    id = request.cookies.get("patient_id")
    patient = Patient.query.filter(Patient.id == id)
    patient.update(request.form.to_dict())
    current_app.db.session.commit()
    return redirect(url_for('patients.dashboard'))


@patients_blueprint.route('/delete_patient', methods=["POST"])
@jwt_required
def delete_patient():
  id = request.cookies.get("patient_id")
  exams = Patient.query.get(id).exams
  for e in exams:
    Exam.query.filter(Exam.id == e.id).delete()
  Patient.query.filter(Patient.id == id).delete()
  current_app.db.session.commit()
  return redirect(url_for('patients.dashboard'))
