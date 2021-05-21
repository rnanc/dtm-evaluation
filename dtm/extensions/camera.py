import threading
import binascii
from time import sleep
from dtm.utils.conversion import base64_to_pil_image, pil_image_to_base64
import cv2
import dlib
import numpy as np
import math
from imutils import face_utils
from PIL import Image


class CameraDTM(object):
  def __init__(self):
    self.to_process = []
    self.to_output_distance = []
    self.to_output_img = []
    self.measurement = 0
    self.open = 0
    self.shut = 0
    self.final = 0
    self.width = 639
    self.sp = "dtm/static/files/shape_predictor_68_face_landmarks.dat"
    self.predictor = dlib.shape_predictor(self.sp)
    self.detector = dlib.get_frontal_face_detector()
    thread = threading.Thread(target=self.keep_processing, args=())
    thread.daemon = True
    thread.start()

  def facial_landmarks(self, image, shape, colors=None, alpha=0.75):
    overlay = image.copy()
    jaw9 = 0
    nose34 = 0
    font = cv2.FONT_HERSHEY_COMPLEX
    for (name, (i, j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():
      if name == "nose":
        nose34 = shape[i:j][3]

      if name == "jaw":
        jaw9 = shape[i:j][8]
    distance = math.sqrt((nose34[0] - jaw9[0]) ** 2 + (nose34[1] - jaw9[1]) ** 2)
    cv2.putText(overlay, "Distance {0}".format(distance), (230, 50), font, 0.5, (0, 255, 0))

    cv2.line(overlay, (nose34[0], nose34[1]),
             (jaw9[0], jaw9[1]),
             (0, 255, 0))
    return overlay, distance

  def lines_mark(self, image, alpha=0.75):
    overlay = image.copy()
    output = image.copy()
    cv2.line(overlay, (0, 180), (self.width, 180), (255, 127, 0), 1)
    cv2.ellipse(overlay, (300, 140), (100, 200), 0, 0, 180, 255, 2)
    cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
    return output

  def process_one(self):
    if not self.to_process:
      return
    input_str = self.to_process.pop(0)
    input_img = base64_to_pil_image(input_str)
    image = np.array(input_img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rects = []
    while len(rects) == 0:
      rects = self.detector(gray, 0)
    for (i, rect) in enumerate(rects):
      shape = self.predictor(gray, rect)
      shape = face_utils.shape_to_np(shape)
      output = self.lines_mark(image)
      output, distance = self.facial_landmarks(output, shape)
      distance = round(distance, 2)
      # self.measurement = round(distance, 2)
      output_img = Image.fromarray(output)
      output_str = pil_image_to_base64(output_img)
      output_str = binascii.a2b_base64(output_str)
      output_str = b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + output_str + b'\r\n'
      self.to_output_distance.append(distance)
      self.to_output_img.append(str(output_str))

  def keep_processing(self):
    while True:
      self.process_one()
      sleep(0.01)

  def enqueue_input(self, input):
    self.to_process.append(input)

  def get_distance(self):
    while not self.to_output_distance:
      sleep(0.05)
    return self.to_output_distance.pop(0)

  def get_frame(self):
    while not self.to_output_img:
      sleep(0.05)
    return self.to_output_img.pop(0)


def init_app(app):
  app.cam_dtm = CameraDTM()
