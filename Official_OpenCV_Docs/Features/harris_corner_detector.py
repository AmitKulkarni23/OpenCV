# Python file which demonstrates the Harris Corner Detector

# APIS used
# cv2.cornerHarris()
#
# 1st arg -> image -> grayscale and float32
# 2nd arg -> blocksize -> size of neighbourhood considered for corner detection
# 3rd arg -> ksize -> Aperture Parameter used in Sobel derivative
# 4th arg-> Harris Detector Free Parameter in the equation

# Credits-> https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_features_harris/py_features_harris.html

###################################

import cv2

import numpy as np

filename = 'chessboard.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('Harris Corner Image',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
