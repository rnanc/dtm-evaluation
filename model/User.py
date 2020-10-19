from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha512
db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(150))
  email = db.Column(db.String(150))
  registered_number = db.Column(db.String(150))
  password = db.Column(db.String(150))

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
