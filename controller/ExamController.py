from flask import Blueprint, render_template, url_for
from flask_jwt_extended import jwt_required

exam_blueprint = Blueprint('exam', __name__, template_folder='templates', static_folder='static')

@exam_blueprint.route('/measurement')
@jwt_required
def detailsPage():
  return render_template('measurement.html')

@exam_blueprint.route('/exam_data')
@jwt_required
def examData():
  return render_template('exam_data.html')
