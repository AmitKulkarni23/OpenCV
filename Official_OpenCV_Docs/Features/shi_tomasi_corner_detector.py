# Python file to demonstrate the working of Shi Tomasi corner detctor

# API Used -> cv2.goodFeaturesToTrack()
#
# 1st argument - grayscale image
# 2nd argument - number of corners that you want to find
# 3rd argument - quality level ( 0 - 1)
#                the minimum quality of teh corner below which everyone is rejected
# 4th argument - Euclidean distance between corners

# Credits -> https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_shi_tomasi/py_shi_tomasi.html


######################################

import numpy as np
import cv2
from matplotlib import pyplot as plt

filename = "chessboard.jpg"

img = cv2.imread(filename)

# Convert to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Call teh Shi Tomais API
corners = cv2.goodFeaturesToTrack(gray,25,0.01,20)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

plt.imshow(img),plt.show()
