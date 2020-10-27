import cv2

import dlib
import numpy as np

import math

from imutils import face_utils
from collections import OrderedDict

capture = cv2.VideoCapture(0)

facial_feature_coordinates = {}
width = 639
height = 479
sp = "predictors/shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(sp)
detector = dlib.get_frontal_face_detector()


FACIAL_LANDMARKS_IDXS = OrderedDict([
	("mouth", (48, 68)),
	("right_eyebrow", (17, 22)),
	("left_eyebrow", (22, 27)),
	("right_eye", (36, 42)),
	("left_eye", (42, 48)),
	("nose", (27, 35)),
	("jaw", (0, 17))
])

def shape_to_np_array(shape, dtype="int"):
    coordinates = np.zeros((68,2), dtype=dtype)

    for i in range(0, 68):
        coordinates[i] = (shape.part(i))

    return coordinates

def facial_landmarks(image, shape, colors=None, alpha=0.75):
    overlay = image.copy()
    output = image.copy()

    jaw9 = 0
    nose34 = 0

    font = cv2.FONT_HERSHEY_COMPLEX

    for (name, (i,j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():
        if name == "nose":
            nose34 = shape[i:j][3]

        if name == "jaw":
            jaw9 = shape[i:j][8]

    distance = math.sqrt((nose34[0] - jaw9[0]) ** 2 + (nose34[1] - jaw9[1]) ** 2)
    cv2.putText(overlay, "Distance {0}".format(distance), (230,50),font,0.5,(0,255,0))

    cv2.line(overlay, (nose34[0],nose34[1]),
                      (jaw9[0],jaw9[1]),
                      (0,255,0))
    cv2.line(overlay, (0, 180), (width, 180), (255, 127, 0), 1)
    cv2.ellipse(overlay, (300,140), (100,200), 0, 0, 180, 255, 2)
    cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)

    # print(facial_feature_coordinates)
    return output

while True:
    ret, image = capture.read()
    dlib.shape_predictor()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 0)

    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        output = facial_landmarks(image, shape)

        cv2.imshow("Video", output)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break


capture.release()

cv2.destroyAllWindows()
