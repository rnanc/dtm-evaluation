from flask import Blueprint, render_template, url_for, request, current_app
from flask_jwt_extended import jwt_required

from model.Model import Exam
from config.serializer import ExamSchema

exam_blueprint = Blueprint('exam', __name__, template_folder='templates', static_folder='static')

@exam_blueprint.route('/measurement')
@jwt_required
def detailsPage():
  return render_template('measurement.html')

@exam_blueprint.route("/create_exam", methods=["POST"])
def create_exam():
  exam_sc = ExamSchema()
  exam_info = request.form.to_dict()
  exam_info["date"] = 21102020
  exam = exam_sc.load(exam_info)
  current_app.db.session.add(exam)
  return "Oi"

@exam_blueprint.route('/exam_data')
def examData():
  return render_template('exam_data.html')
