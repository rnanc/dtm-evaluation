from flask_marshmallow import Marshmallow
from dtm.extensions.database import Users
from dtm.extensions.database import Patient
from dtm.extensions.database import Exam

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

def init_app(app):
  ma.init_app(app)
