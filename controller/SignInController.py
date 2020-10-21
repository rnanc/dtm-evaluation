import datetime

from flask import Blueprint, render_template, url_for, request, current_app, redirect, make_response, flash
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, set_access_cookies, jwt_optional

from model.Model import Users
from config.serializer import UserSchema

home_blueprint = Blueprint('home', __name__, template_folder='templates', static_folder="static")


@home_blueprint.route('/')
def home():
  return render_template("signIn.html")


@home_blueprint.route('/signUp', methods=['GET', 'POST'])
def signUp():
  if request.method == 'POST':
    us = UserSchema()
    user_info = request.form.to_dict()
    user = us.load(user_info)
    users = Users.query.all()
    for u in users:
      if u.email == user.email:
        flash("Email já cadastrado ! Tente novamente.", "danger")
        return redirect(url_for("home.home"))
    if "@aluno.cesupa.br" not in user.email and "@prof.cesupa.br" not in user.email:
      flash("Email precisa ser do domínio CESUPA ! Tente novamente cadastrando seu email do CESUPA. ", "danger")
      return render_template("signIn.html"), 400
    user.gen_hash()
    current_app.db.session.add(user)
    current_app.db.session.commit()
    flash("Cadastro realizado com sucesso !", "success")
  return redirect(url_for("home.home"))


@home_blueprint.route('/login', methods=["POST"])
def login_user():
  user = request.form.to_dict()
  print(user)
  user_query = Users.query.filter_by(email=user["email"]).first()
  if user_query != None:
    verify = user_query.verify_password(user['password'])
  if user_query != None and verify:
    access_token = create_access_token(identity=user_query.id, expires_delta=datetime.timedelta(hours=12))
    # refresh_token = create_refresh_token(identity=user_query.id)
    response = make_response(redirect(url_for('patients.dashboard')))
    response.set_cookie('access_token_cookie', access_token)
    response.set_cookie('username', user_query.name)
    response.set_cookie('user_id', str(user_query.id))
    print(access_token)
    return response
  else:
    flash("Senha ou email erradas!", "danger")
  return redirect(url_for("home.home"))
