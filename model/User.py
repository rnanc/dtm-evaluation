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
