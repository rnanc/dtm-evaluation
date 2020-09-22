from flask import Blueprint, render_template, url_for

details_blueprint = Blueprint('details', __name__, template_folder='templates', static_folder='static')

@details_blueprint.route('/details')
def detailsPage():
  return render_template('details.html')
