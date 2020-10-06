from flask import Blueprint, render_template, url_for

exam_blueprint = Blueprint('exam', __name__, template_folder='templates', static_folder='static')

@exam_blueprint.route('/measurement')
def detailsPage():
  return render_template('measurement.html')