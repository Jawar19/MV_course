import sys

from resources.homeBrew import *

print("Hello World!")
print("I am openCV", cv.__version__)

fileDir = os.path.dirname(os.path.realpath('__file__'))
relPath = "./img/"
path = os.path.normpath(os.path.join(fileDir, relPath))

print("\n__--I am located at: ", fileDir, "--__")

# import all images from img folder.
img = loadImages(path)  # loading all images from ./img/ folder (.jpg, .jpeg, .png)
# if no image is found, error massage and termination
if img is None:
    sys.exit("Could not read the image.")

#color3dPlot(img[0])

cv.imshow("Display window", img[0])
k = cv.waitKey(0)

babyFood(path)


