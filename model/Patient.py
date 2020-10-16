from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db 

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    birth_date = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    pain_choice = db.Column(db.Boolean)
    def __init__(self, name, email, phone, birth_date, gender, pain_choice):
        self.name = name
        self.email = email
        self.phone = phone
        self.birth_date = birth_date
        self.gender = gender 
        self.pain_choice = pain_choice