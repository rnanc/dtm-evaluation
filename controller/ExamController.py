from flask import Blueprint, render_template, url_for, request, current_app, make_response, redirect
from flask_jwt_extended import jwt_required
from datetime import date
from model.Model import Exam
from config.serializer import ExamSchema
from config.serializer import UserSchema
from config.serializer import PatientSchema
from model.Model import Users
from model.Model import Patient

exam_blueprint = Blueprint('exam', __name__, template_folder='templates', static_folder='static')


@exam_blueprint.route('/measurement_open_mouth', methods=["GET", "POST"])
@jwt_required
def measurement_open_mouth():
  if request.method == 'GET':
    return render_template('measurement.html', measurement_open_mouth="0", measurement_shut_mouth="0", measurement_result="0", finalizar_open="false", finalizar_shut="false", step="1")
  else:
    return render_template('measurement.html', measurement_open_mouth="0", measurement_shut_mouth="0", measurement_result="0", finalizar_open="true", finalizar_shut="false", measurement="true", step="1")

@exam_blueprint.route('/measurement_mouth_shut', methods=["GET", "POST"])
@jwt_required
def measurement_mouth_shut():
  if request.method == 'GET':
    file = open("services/dtm/output/distance.txt")
    distance = file.read()
    file.close()
    res = make_response(render_template('measurement.html', measurement_open_mouth=distance, measurement_shut_mouth="0",
                                        measurement_result="0", finalizar_shut="false", finalizar_open="false", step="2"))
    res.set_cookie("measurement_open_mouth", distance)
    return res
  else:
    measurement_open_mouth = request.cookies.get("measurement_open_mouth")
    return render_template('measurement.html', measurement_open_mouth=measurement_open_mouth, measurement_shut_mouth="0",
                           measurement_result="0", finalizar_shut="true", finalizar_open="false", measurement="true", step="2")

@exam_blueprint.route('/measurement_result', methods=["GET", "POST"])
@jwt_required
def measurement_result():
  if request.method == 'GET':
    file = open("services/dtm/output/distance.txt")
    distance = file.read()
    file.close()
    measurement_open_mouth = request.cookies.get("measurement_open_mouth")
    result = round(float(measurement_open_mouth) - float(distance), 2)
    return render_template('measurement.html', measurement_open_mouth=measurement_open_mouth, measurement_shut_mouth=distance, measurement_result=result, finalizar_shut="false", finalizar_open="false", step="3")

@exam_blueprint.route("/create_exam", methods=["POST"])
@jwt_required
def create_exam():
  patient = Patient.query.get(int(request.cookies.get("patient_id")))
  user = Users.query.get(int(request.cookies.get("user_id")))
  exam_sc = ExamSchema()
  exam_info = request.form.to_dict()
  data_atual = date.today()
  exam_info["date"] = str(data_atual)
  exam = exam_sc.load(exam_info)
  current_app.db.session.add(exam)
  patient.exams.append(exam)
  user.exams.append(exam)
  current_app.db.session.commit()
  return redirect(url_for("details.detailsPage", id=patient.id))


@exam_blueprint.route('/exam_data/<id>')
def examData(id):
  exam = Exam.query.get(id)
  doctor = Users.query.get(exam.user_id)
  patient = Patient.query.get(exam.patient_id)
  return render_template('exam_data.html', exam=exam, doctor=doctor, patient=patient)
