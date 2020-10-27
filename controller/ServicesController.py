from flask import Blueprint, Response, request, make_response
from services.dtm import dtm_tool

services_blueprint = Blueprint('services', __name__, template_folder='templates', static_url_path="static")


@services_blueprint.route('/dtm')
def dtm():
  return Response(dtm_tool.Run(), mimetype='multipart/x-mixed-replace; boundary=frame')

