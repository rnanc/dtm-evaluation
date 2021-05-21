from flask import Blueprint, render_template, url_for, make_response, redirect, request, redirect, current_app, flash
from flask_jwt_extended import jwt_required
from dtm.extensions.serializer import UserSchema
from dtm.extensions.database import Users

bp = Blueprint('users', __name__, template_folder='templates', static_folder='static')


@bp.route('/profile')
@jwt_required
def profile():
  id = request.cookies.get("user_id")
  user = Users.query.get(id)
  return render_template('profile.html', user=user)


@bp.route('/edit_profile', methods=["GET", "POST"])
@jwt_required
def edit_profile():
  if request.method == "GET":
    id = request.cookies.get("user_id")
    user = Users.query.get(id)
    return render_template('edit_profile.html', user=user)
  else:
    id = request.cookies.get("user_id")
    user = Users.query.get(id)
    user_query = Users.query.filter(Users.id == id)
    us = UserSchema()
    user_form = request.form.to_dict()
    if user_form != None:
      if "@aluno.cesupa.br" in user_form["email"] or "@prof.cesupa.br" in user_form["email"]:
        if user_form["email"] == user_form["email_confirm"] and user_form["password"] == user_form["password_confirm"]:
          del user_form["email_confirm"]
          del user_form["password_confirm"]
          user_sch = us.load(user_form)
          user_sch.gen_hash()
          if user != None:
            verify = user.verify_password(user_form['password'])
          if user != None and verify:
            user_form["password"] = user_sch.password
            user_query.update(user_form)
            current_app.db.session.commit()
            return redirect(url_for('users.profile'))
          else:
            flash("Senha errada!", "danger")
            return redirect(url_for('users.edit_profile'))
        else:
          flash("Campos de confirmação errados!", "danger")
          return redirect(url_for('users.edit_profile'))
      else:
        flash("Email precisa ser do domínio CESUPA! Tente novamente cadastrando seu email do CESUPA. ", "danger")
        return redirect(url_for('users.edit_profile'))


@bp.route('/delete_user', methods=["POST"])
@jwt_required
def delete_user():
  id = request.cookies.get("user_id")
  user = Users.query.get(id)
  user_form = request.form.to_dict()
  if user_form["registered_number"] == user.registered_number:
    Users.query.filter(Users.id == id).delete()
    current_app.db.session.commit()
    return redirect(url_for('home.home'))
  else:
    flash("Campo de confirmação errado!", "danger")
    return redirect(url_for('users.profile'))

def init_app(app):
  app.register_blueprint(bp)
