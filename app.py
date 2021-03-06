from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model.Model import configure as db_config
from config.serializer import configure as se_config
from config.jwt import configure as jwt_config
from controller.SignInController import home_blueprint
from controller.PatientsController import patients_blueprint
from controller.DetailsController import details_blueprint
from controller.ExamController import exam_blueprint
from controller.ServicesController import services_blueprint
from controller.UsersController import users_blueprint
from services.dtm.dtm_tool import DTM
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/DTM?gssencmode=disable'
app.config['SECRET_KEY'] = 'e7c0596d00d6d1d17e64d6547cd732cf'
app.config['JWT_SECRET_KEY'] = "1cca2a86e499bc8f16a75000cea3fbc5"
app.config['JWT_TOKEN_LOCATION'] = "cookies"
app.config['JWT_COOKIE_CSRF_PROTECT'] = False



db = SQLAlchemy(app)

dtm = DTM()

db_config(app)
se_config(app)

Migrate(app, app.db)
jwt_config(app)
dtm.init_app(app)
app.register_blueprint(home_blueprint)
app.register_blueprint(patients_blueprint)
app.register_blueprint(details_blueprint)
app.register_blueprint(exam_blueprint)
app.register_blueprint(services_blueprint)
app.register_blueprint(users_blueprint)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
