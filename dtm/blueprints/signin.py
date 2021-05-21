from flask import Blueprint, render_template, url_for, request, current_app, redirect, make_response, flash
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies
from dtm.extensions.database import Users
from dtm.extensions.serializer import UserSchema

bp = Blueprint('home', __name__, template_folder='templates', static_folder="static")


@bp.route('/')
def home():
  return render_template("signIn.html")


@bp.route('/signUp', methods=['GET', 'POST'])
def signUp():
  if request.method == 'POST':
    us = UserSchema()
    user_info = request.form.to_dict()
    user = us.load(user_info)
    users = Users.query.all()
    for u in users:
      if u.email == user.email:
        flash("Email já cadastrado! Tente novamente.", "danger")
        return redirect(url_for("home.home"))
      if u.registered_number == user.registered_number:
        flash("Matricula já cadastrada! Tente novamente.", "danger")
        return redirect(url_for("home.home"))
    if "@aluno.cesupa.br" not in user.email and "@prof.cesupa.br" not in user.email:
      flash("Email precisa ser do domínio CESUPA! Tente novamente cadastrando seu email do CESUPA. ", "danger")
      return render_template("signIn.html"), 400
    user.gen_hash()
    current_app.db.session.add(user)
    current_app.db.session.commit()
    flash("Cadastro realizado com sucesso!", "success")
  return redirect(url_for("home.home"))


@bp.route('/login', methods=["POST"])
def login_user():
  user = request.form.to_dict()
  user_query = Users.query.filter_by(email=user["email"]).first()
  verify = False
  if user_query != None:
    verify = user_query.verify_password(user['password'])
  if user_query != None and verify:
    access_token = create_access_token(identity=user_query.id)
    refresh_token = create_refresh_token(identity=user_query.id)
    response = make_response(redirect(url_for('patients.dashboard')))
    response.set_cookie('refresh_token_cookie', refresh_token)
    response.set_cookie('username', user_query.name)
    response.set_cookie('user_id', str(user_query.id))
    set_access_cookies(response, access_token)
    return response
  else:
    flash("Senha ou email erradas!", "danger")
  return redirect(url_for("home.home"))


@bp.route('/logoff', methods=["POST"])
def logoff_user():
  response = make_response(redirect(url_for('home.home')))
  response.set_cookie('username', '', expires=0)
  response.set_cookie('user_id', '', expires=0)
  response.set_cookie('access_token_cookie', '', expires=0)
  response.set_cookie('refresh_token_cookie', '', expires=0)
  response.set_cookie('patient_id', '', expires=0)
  return response

def init_app(app):
  app.register_blueprint(bp)
