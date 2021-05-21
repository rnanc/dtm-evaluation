from flask import current_app, request, Blueprint
from flask_socketio import emit
#from dtm.extensions.middleware import socketio
from dtm.extensions.database import Patient


def open_measurement(input):
  input = input.split(",")[1]
  current_app.cam_dtm.enqueue_input(input)
  current_app.cam_dtm.open = current_app.cam_dtm.get_distance()
  img = current_app.cam_dtm.get_frame()
  emit('result_open', {'measurement': current_app.cam_dtm.open, 'img': img})


def shut_measurement(input):
  input = input.split(",")[1]
  id_patient = request.cookies.get("patient_id")
  initial_distance = Patient.query.get(id_patient).initial_distance_cm
  current_app.cam_dtm.enqueue_input(input)
  current_app.cam_dtm.shut = current_app.cam_dtm.get_distance()
  final_distance = round(
    (float(initial_distance) * float(current_app.cam_dtm.shut)) / float(current_app.cam_dtm.open), 2)
  img = current_app.cam_dtm.get_frame()
  emit('result_shut', {'measurement': current_app.cam_dtm.shut, 'result': final_distance, 'img': img})




