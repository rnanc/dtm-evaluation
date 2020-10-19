from flask_marshmallow import Marshmallow
from model.Model import User
from model.Patient import Patient

ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

class PatientSchema(ma.ModelSchema):
    class Meta:
        model = Patient
