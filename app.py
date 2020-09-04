from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/DTM'
db = SQLAlchemy(app)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)