from flask import Blueprint, render_template, url_for, make_response, redirect, request, redirect, current_app
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
    user = Users.query.filter(Users.id == id)
    us = UserSchema()
    user_form = request.form.to_dict()
    user_sch = us.load(user_form)
    user_sch.gen_hash()
    user_form["password"] = user_sch.password
    user.update(user_form)
    current_app.db.session.commit()
    return redirect(url_for('patients.dashboard'))
