from flask import Blueprint, render_template, url_for, make_response
from flask_jwt_extended import jwt_required
from model.Model import Patient
from model.Model import Users
from datetime import date

Date = date
details_blueprint = Blueprint('details', __name__, template_folder='templates', static_folder='static')


@details_blueprint.route('/details/<id>')
@jwt_required
def detailsPage(id):
  patient = Patient.query.get(id)
  actual_year = Date.today().year
  date = patient.age
  date = date.split("-")
  birth_year = date[0]
  age = int(actual_year) - int(birth_year)
  exams = patient.exams
  for exam in exams:
    doctor = Users.query.get(exam.user_id)
    exam.doctor = doctor.name
  res = make_response(render_template('details.html', patient=patient, age=age, exams=exams))
  res.set_cookie("patient_id", str(id))
  return res
