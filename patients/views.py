from flask import render_template
import json
from . import patients

with open('data.json', 'r') as f:
    file = f.read()

data = json.loads(file)

@patients.route('/')
def patientsPage():
    return render_template('list.html', data=data)