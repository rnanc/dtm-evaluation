from flask import Blueprint, render_template, url_for, make_response, redirect, request, redirect, flash
from flask_jwt_extended import jwt_required
from dtm.extensions.serializer import PatientSchema
from dtm.extensions.database import Patient
from dtm.extensions.database import Exam

from flask import current_app

bp = Blueprint('patients', __name__, template_folder='templates', static_folder='static')


@bp.route('/dashboard')
@jwt_required
def dashboard():
  patients = Patient.query.all()
  print(request.cookies.get("access_token_cookie"))
  return render_template('dashboard.html', patients=patients)


@bp.route('/register_patient', methods=['GET', 'POST'])
@jwt_required
def register_patient():
  if request.method == "GET":
    return render_template('register_patient.html')
  else:
    patients = Patient.query.all()
    patient = PatientSchema()
    patients_info = request.form.to_dict()
    for p in patients:
      if p.doc_number == patients_info['doc_number']:
        flash("Documento já cadastrado! Tente novamente.", "danger")
        return redirect(url_for("patients.register_patient"))
      if p.email == patients_info['email']:
        flash("Email já cadastrado! Tente novamente.", "danger")
        return redirect(url_for("patients.register_patient"))
      if p.phone == patients_info['phone']:
        flash("Numero já cadastrado! Tente novamente.", "danger")
        return redirect(url_for("patients.register_patient"))
    patients_load = patient.load(patients_info)
    current_app.db.session.add(patients_load)
    current_app.db.session.commit()
    return redirect(url_for('patients.dashboard'))


@bp.route('/edit_patient', methods=["GET", "POST"])
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


@bp.route('/delete_patient', methods=["POST"])
@jwt_required
def delete_patient():
  id = request.cookies.get("patient_id")
  exams = Patient.query.get(id).exams
  for e in exams:
    Exam.query.filter(Exam.id == e.id).delete()
  Patient.query.filter(Patient.id == id).delete()
  current_app.db.session.commit()
  return redirect(url_for('patients.dashboard'))

def init_app(app):
  app.register_blueprint(bp)
