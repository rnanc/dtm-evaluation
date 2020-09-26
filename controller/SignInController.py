from flask import Blueprint, render_template, url_for, request,current_app, redirect, make_response
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, set_access_cookies, jwt_optional

from model.User import User
from config.serializer import UserSchema

home_blueprint = Blueprint('home', __name__, template_folder='templates', static_folder="static")

@home_blueprint.route('/')
@jwt_optional
def home():
  return render_template("signIn.html")

@home_blueprint.route('/signUp', methods=['GET','POST'])
def signUp():
  if request.method == 'POST':
    us = UserSchema()
    user_info = request.form.to_dict()
    user = us.load(user_info)
    user.gen_hash()
    current_app.db.session.add(user)
    current_app.db.session.commit()
  return "cadastrou"

@home_blueprint.route('/login', methods=["POST"])
def login_user():
    user = request.form.to_dict()
    print(user)
    user_query = User.query.filter_by(email=user["email"]).first()
    if user_query != None:
      user_query.verify_password(user['password'])
    if user_query != None:
        access_token = create_access_token(identity=user_query.id)
        refresh_token = create_refresh_token(identity=user_query.id)
        response = make_response(redirect(url_for('patients.patientsPage')))
        response.set_cookie('access_token_cookie', access_token)
        response.set_cookie('username', user_query.name)
        response.set_cookie('user_id', str(user_query.id))
        print (access_token)
        return response
    return redirect(url_for("home.home"))

