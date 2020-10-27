from flask import Blueprint, render_template, url_for
from flask_jwt_extended import jwt_required

details_blueprint = Blueprint('details', __name__, template_folder='templates', static_folder='static')

@details_blueprint.route('/details')
@jwt_required
def detailsPage():
  return render_template('details.html')