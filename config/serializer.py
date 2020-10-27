from flask_marshmallow import Marshmallow
from model.Model import Users

from model.Model import Patient

from model.Model import Exam

ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class UserSchema(ma.ModelSchema):
    class Meta:
        model = Users

class PatientSchema(ma.ModelSchema):
    class Meta:
        model = Patient

class ExamSchema(ma.ModelSchema):
    class Meta:
        model = Exam
