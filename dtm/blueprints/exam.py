from flask import Blueprint, render_template, url_for, request, current_app, Response, redirect
from flask_jwt_extended import jwt_required
from datetime import date
from dtm.extensions.database import Exam
from dtm.extensions.database import Users
from dtm.extensions.database import Patient
bp = Blueprint('exam', __name__, template_folder='templates', static_folder='static')


@bp.route('/measurement', methods=["GET", "POST"])
@jwt_required
def measurement_open_mouth():
  if request.method == 'GET':
    return render_template('measurement.html')
  else:
    return render_template('measurement.html')

@bp.route("/create_exam", methods=["POST"])
@jwt_required
def create_exam():
  patient = Patient.query.get(int(request.cookies.get("patient_id")))
  user = Users.query.get(int(request.cookies.get("user_id")))
  exam_info = request.form.to_dict()
  report_open = eval(exam_info['report_open'])
  report_shut = eval(exam_info['report_shut'])
  data_atual = date.today()
  data_atual = "{}/{}/{}".format(data_atual.day, data_atual.month, data_atual.year)
  exam_info["date"] = data_atual
  exam = Exam(date=data_atual, open_measurement_px=exam_info['open_measurement_px'],
              shut_measurement_px=exam_info['shut_measurement_px'],
              result_measurement_cm=exam_info['result_measurement_cm'],
              report_open=report_open, report_shut=report_shut)
  current_app.db.session.add(exam)
  patient.exams.append(exam)
  user.exams.append(exam)
  current_app.db.session.commit()
  return redirect(url_for("details.detailsPage", id=request.cookies.get("patient_id")))

@bp.route('/exam_data/<id>')
def examData(id):
  exam = Exam.query.get(id)
  doctor = Users.query.get(exam.user_id)
  patient = Patient.query.get(exam.patient_id)
  return render_template('exam_data.html', exam=exam, doctor=doctor, patient=patient)

@bp.route('/report_open/<id>')
def report_open(id):
  exam = Exam.query.get(id)
  return Response(exam.report_open, mimetype='multipart/x-mixed-replace; boundary=frame')

@bp.route('/report_shut/<id>')
def report_shut(id):
  exam = Exam.query.get(id)
  return Response(exam.report_shut, mimetype='multipart/x-mixed-replace; boundary=frame')

def init_app(app):
  app.register_blueprint(bp)
