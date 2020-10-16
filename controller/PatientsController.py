from flask import Blueprint, render_template, url_for, make_response, redirect, request, redirect

from config.serializer import PatientSchema

from model.Patient import Patient
from sqlalchemy.testing.config import db

patients_blueprint = Blueprint('patients', __name__, template_folder='templates', static_folder='static')

@patients_blueprint.route('/dashboard')
def dashboard():
  # patients = Patient.query.all()
  return render_template('dashboard.html')

@patients_blueprint.route('/register_patient', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    patient = PatientSchema()
    patients_info = request.form.to_dict()
    patients_load = patient.load(patients_info)
    db.session.add(patients_load)
    db.session.commit()
    return redirect(url_for('dashboard'))
  return render_template('register_patient.html')

# @patients_blueprint.route('/delete/<int:id>')
# def delete(id):
#   paciente = Paciente.query.get(id)
#   db.session.delete(paciente)
#   db.session.commit()
#   return redirect(url_for('dashboard'))

@patients_blueprint.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
  patient = Patient.query.get(id)
  if request.method == 'POST':
    patient.nome = request.form['nome']
    patient.email = request.form['email']
    patient.telefone = request.form['telefone']
    db.session.commit()
    return redirect(url_for('dashboard'))
  return render_template('edit.html', patient = patient)