from flask import Blueprint, render_template, url_for
import json

patients_blueprint = Blueprint('patients', __name__, template_folder='templates', static_folder='static')

with open('data.json', 'r') as f:
  file = f.read()

data = json.loads(file)

@patients_blueprint.route('/patients')
def patientsPage():
  return render_template('list.html', data=data)
