# Python file which demponstrates the working of hough circles

# API used: cv2.HoughCircles()

# 1st arg -> input image -> 8 bit single channel, grayscale image
# 2nd arg -> CV_HOUGH_GRADIESNT
#
# 3rd arg -> dp -> inverse ration of accumulator resolution to the image resolution
# dp = 1, acc res = img res
# dp = 2, acc = 0.5 * width image
#         acc = 0.5 * height of image
#
# 4th arg - minimum distance between centers of detected circles
#
# Optional arguments
# minRadius - min radius of the circle
# maxRadius - max radius of the circle


# Credits -> https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html

###############

import cv2
import numpy as np

img = cv2.imread('opencv-logo.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
