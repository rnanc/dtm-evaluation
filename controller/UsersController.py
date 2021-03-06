from flask import Blueprint, render_template, url_for, make_response, redirect, request, redirect, current_app, flash
from flask_jwt_extended import jwt_required
from config.serializer import UserSchema
from model.Model import Users

users_blueprint = Blueprint('users', __name__, template_folder='templates', static_folder='static')

@users_blueprint.route('/profile')
@jwt_required
def profile():
  id = request.cookies.get("user_id")
  user = Users.query.get(id)
  return render_template('profile.html', user=user)

@users_blueprint.route('/edit_profile', methods=["GET", "POST"])
@jwt_required
def edit_profile():
  if request.method == "GET":
    return render_template("edit_profile.html")
  else:
    id = request.cookies.get("user_id")
    user = Users.query.get(id)
    user_query = Users.query.filter(Users.id == id)
    us = UserSchema()
    user_form = request.form.to_dict()
    if user_form != None:
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
