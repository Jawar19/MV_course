import os
import glob
import cv2 as cv
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def loadImages(path):
    ext = ['png', 'jpg', 'jpeg']  # image format extensions
    files = []  # empty array for file paths to images
    [files.extend(glob.glob(path + '/*.' + e)) for e in ext]
    img = [cv.imread(file) for file in files]
    return img


def babyFood(path):
    path = os.path.normpath(os.path.join(path, './babyfood/'))
    imgBaby = loadImages(path)
    if imgBaby is None:
        print("Could not read the image from", './babyfood/')
        return
    cv.imshow("Babyfood", imgBaby[2])
    cv.waitKey(100)
    #
    hsv_img = cv.cvtColor(imgBaby[2], cv.COLOR_BGR2HSV)
    #cv.imshow("Babytest", hsv_img)

    lo_red = np.array([150., 75., 100.], dtype="uint8")
    hi_red = np.array([179., 255., 255.], dtype="uint8")
    mask = cv.inRange(hsv_img, lo_red, hi_red)
    lo_red = np.array([0., 150., 100.], dtype="uint8")
    hi_red = np.array([10., 255., 255.], dtype="uint8")
    mask = mask + cv.inRange(hsv_img, lo_red, hi_red)
    element = np.ones((5, 5), np.uint8)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, element)
    cv.imshow("mask", mask)

    cv.waitKey(0)
    cv.destroyAllWindows()


def rgb3dPlot(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    r, g, b = cv.split(img)
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1, projection="3d")
    pxColor = img.reshape((np.shape(img)[0] * np.shape(img)[1], 3))
    norm = colors.Normalize(vmin=-1., vmax=1.)
    norm.autoscale(pxColor)
    pxColor = norm(pxColor).tolist()

    axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pxColor, marker=".")
    axis.set_xlabel("Red")
    axis.set_ylabel("green")
    axis.set_zlabel("Blue")
    plt.show()


def hsv3dplot(inImg):
    hsvImg = inImg
    h, s, v = cv.split(hsvImg)
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1, projection="3d")
    pxColor = hsvImg.reshape((np.shape(hsvImg)[0] * np.shape(hsvImg)[1], 3))
    norm = colors.Normalize(vmin=-1., vmax=1.)
    norm.autoscale(pxColor)
    pxColor = norm(pxColor).tolist()

    axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pxColor, marker=".")
    axis.set_xlabel("Hue")
    axis.set_ylabel("Saturation")
    axis.set_zlabel("Value")
    plt.show()