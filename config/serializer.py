from flask_marshmallow import Marshmallow
from model.User import User
ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
