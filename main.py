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

opg = 1 # vælg opgave nummer her, inden i afvikler koden

if opg == 1:
    ## opgave 1 & 2

    # TODO: indlæs billede fra mappen "img/BabyFood/" og vis dette i et "named window"
    #   HINT: imread() og imshow()
    #   https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html#display-image
    #   https://docs.opencv.org/master/d5/d98/tutorial_mat_operations.html


    cv.waitKey(0)

    # TODO: segmenter billedet fra "img/BabyFood" så kun de røde skeer vises.
    #   HINT: brug forloop og if-statements
    #   https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html


    cv.waitKey(0)

if opg == 3:
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


if opg == 4:
    ## opgave 4

    # TODO: Lav et videocapture objekt med cv.VideoCapture()
    cap =

    while True:
        ret, frame = cap.read()

        # TODO: Implemeter facedetection som ovenfor, og opdater vinduet "Video"
        cv.imshow("video", frame)

        if cv.waitKey(25) & 0xFF == ord('q'): # stop videovisning ved at trykke på "q"
                break

    cap.release() #release videodevice, så systemet kan se den igen


cv.destroyAllWindows() # lukker alle video vinduer.
