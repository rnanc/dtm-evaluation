from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha512

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class Users(db.Model):
  __name__ = "users"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(150))
  email = db.Column(db.String(150))
  registered_number = db.Column(db.String(150))
  password = db.Column(db.String(150))
  exams = db.relationship("Exam", backref="users", lazy="select")

  def gen_hash(self):
      self.password = pbkdf2_sha512.hash(self.password)

  def verify_password(self, password):
      return pbkdf2_sha512.verify(password, self.password)

  def __init__(self, name, registered_number, email, password):
    self.name = name
    self.registered_number = registered_number
    self.email = email
    self.password = password

class Patient(db.Model):
  __name__ = "patients"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  email = db.Column(db.String(100))
  phone = db.Column(db.String(100))
  age = db.Column(db.String(100))
  gender = db.Column(db.String(100))
  pain_choice = db.Column(db.String(100))
  initial_distance_cm = db.Column(db.Float, nullable=False)
  exams = db.relationship("Exam", backref="patient", lazy="select")

  def __init__(self, name, email, phone, age, gender, pain_choice, initial_distance_cm):
    self.name = name
    self.email = email
    self.phone = phone
    self.age = age
    self.gender = gender
    self.pain_choice = pain_choice
    self.initial_distance_cm = initial_distance_cm
class Exam(db.Model):
  __name__ = "exams"
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.String(100), nullable=False)
  open_measurement_px = db.Column(db.Float, nullable=False)
  shut_measurement_px = db.Column(db.Float, nullable=False)
  result_measurement_cm = db.Column(db.Float, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))

  def __init__(self, date, open_measurement, shut_measurement, result_measurement):
    self.date = date
    self.open_measurement_px = open_measurement
    self.shut_measurement_px = shut_measurement
    self.result_measurement_cm = result_measurement
