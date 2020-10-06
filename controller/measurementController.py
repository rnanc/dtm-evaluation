from flask import Blueprint, render_template, url_for

measurement_blueprint = Blueprint('measurement', __name__, template_folder='templates', static_folder='static')

@measurement_blueprint.route('/medicao')
def detailsPage():
  return render_template('measurement.html')