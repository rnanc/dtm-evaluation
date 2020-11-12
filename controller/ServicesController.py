from flask import Blueprint, Response, request, current_app

services_blueprint = Blueprint('services', __name__, template_folder='templates', static_url_path="static")

@services_blueprint.route('/dtm')
def dtm():
  return Response(current_app.dtm.Run(), mimetype='multipart/x-mixed-replace; boundary=frame')


