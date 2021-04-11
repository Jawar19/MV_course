import sys
import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
font = cv.FONT_HERSHEY_SIMPLEX

from resources.homeBrew import *

print("Hello World!")
print("I am openCV", cv.__version__)

fileDir = os.path.dirname(os.path.realpath('__file__'))
relPath = "./img/"
path = os.path.normpath(os.path.join(fileDir, relPath))

print("\n__--I am located at: ", fileDir, "--__")

## opgave 1

# TODO: indlæs billede fra mappen "img/BabyFood/" og vis dette i et "named window"
#   HINT: imread() og imshow()


cv.waitKey(0)

# TODO: segmenter billedet fra "img/BabyFood" så kun de røde skeer vises.
#   HINT: brug forloop og if-statements


cv.waitKey(0)

## Opgave 3

# I opgave 3 skal i ved hjælp af HAAR-Cascades finde ansigtet på et billede og markere dette.
#   Det kan bla. gøres med rectangle eller circle.

# load af haar-like features
cascPath = cv.data.haarcascades

facePath = cascPath + "haarcascade_frontalface_default.xml"
faceCasc = cv.CascadeClassifier(facePath)

# TODO: indlæs selv "eye" og "smile" haar-cascades



# TODO: indlæs billedet "face.jpg" fra mappen "/img/" i farve



# TODO: opret en kopi af det indlæste billede og konverter dette til gråtoner
#   HINT: cv.CVTCOLOR og flaget cv.COLOR_BGR2GRAY


faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30,30),
    flags=cv.CASCADE_SCALE_IMAGE
)

for (x, y, w, h) in faces:
    # TODO: make "Region of interest" af det originale og gråtone billedet, som kan bruges til at finde
    #   smil og øjne.
    roiColor = color[y:y+h, x:x+w]
    roiGray

    # TODO: tegn en figur som markerer ansigtet, f.eks. rectangle.
    cv.rectangle(frame,
                 """position af øverste venstre hjørne""",
                 """position af nederste højre hjørne""",
                 (255, 0, 0),   #farven i BGR værdier
                 3)             #tykkelse på outline

# # face detection using haar like features
# cascPath = "venv/Lib/site-packages/cv2/data/"
# cascPath = cv.data.haarcascades
# facePath = cascPath + "haarcascade_frontalface_default.xml"
# eyePath = cascPath + "haarcascade_eye.xml"
# smilePath = cascPath + "haarcascade_smile.xml"
#
# faceCascade = cv.CascadeClassifier(facePath)
# eyeCascade = cv.CascadeClassifier(eyePath)
# smileCascade = cv.CascadeClassifier(smilePath)
#
# # Load the image
# frame = cv.imread(path + "\\face.jpg", cv.IMREAD_COLOR)
# cv.imshow("frame", frame)
# gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
# cv.waitKey(1000)
# cv.imshow("frame", gray)
#
# faces = faceCascade.detectMultiScale(
#     gray,
#     scaleFactor=1.1,
#     minNeighbors=5,
#     minSize=(30,30),
#     flags=cv.CASCADE_SCALE_IMAGE
# )
#
# for (x, y, w, h) in faces:
#     roi_gray = gray[y:y+h, x:x+w]
#     roi_color = frame[y:y+h, x:x+w]
#     smile = smileCascade.detectMultiScale(roi_gray,
#                                           scaleFactor=1.25,
#                                           minNeighbors=35,
#                                           minSize=(25, 25),
#                                           flags=cv.CASCADE_SCALE_IMAGE)
#     eyes = eyeCascade.detectMultiScale(roi_gray, scaleFactor=1.1,
#                                        minNeighbors=5,
#                                        minSize=(10, 10),
#                                        flags=cv.CASCADE_SCALE_IMAGE)
#     if len(smile) == 0 and len(eyes) == 0:
#         continue
#     else:
#         cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
#         for (sx, sy, sw, sh) in smile:
#             cv.rectangle(roi_color, (sx,sy), (sx+sw,sy+sh), (0, 255, 0), 2)
#             cv.putText(frame, 'Smile', (x+sx, y+sy), 1, 1, (0, 255, 0), 1)
#
#         for (ex, ey, ew, eh) in eyes:
#             cv.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0, 0, 255), 2)
#             cv.putText(frame, 'Eye', (x+ex, y+ey), 1, 1, (0, 0, 255), 1)
#
# cv.imshow("frame", frame)
# cv.waitKey(0)
# cv.destroyAllWindows()
#
#
# # opening the webcam in window
# cv.namedWindow("Video", cv.WINDOW_AUTOSIZE)
# cap = cv.VideoCapture(0,  cv.CAP_DSHOW)
# cap.set(3, 1920)
# cap.set(4, 1080)
# cap.set(cv.CAP_PROP_FPS, 30)
#
# while True:
#     ret, frame = cap.read()
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     faces = faceCascade.detectMultiScale(
#         gray,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(30, 30),
#         flags=cv.CASCADE_SCALE_IMAGE
#     )
#     for (x, y, w, h) in faces:
#         if w > 100:
#             cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
#     if ret:
#         cv.imshow("Video", frame)
#     else:
#         print("BARK! ")
#     if cv.waitKey(25) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv.destroyAllWindows()