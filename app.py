from flask import Flask, render_template, request, redirect, url_for
#from flask_sqlalchemy import SQLAlchemy

from details import details as details_blueprint
from patients import patients as patients_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/DTM'
#db = SQLAlchemy(app)

app.register_blueprint(details_blueprint)
app.register_blueprint(patients_blueprint)

if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)