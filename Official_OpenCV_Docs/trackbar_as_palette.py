# Here we will create a simple application which shows the color you specify.
#  You have a window which shows the color and three trackbars to specify each of B,G,R colors.
# You slide the trackbar and correspondingly window color changes. By default,
# initial color will be set to Black.

# cv2.createTrackbar()
# 1st arg -trackbar name
# 2nd arg - window to which teh trackbar is attached to
# 3rd - default value
# 4th arg - max value
# 5th arg - callback function which is executed everytime the trackbar changes

# Tutorial Credits -> https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_trackbar/py_trackbar.html

##############################3
import numpy as np
import cv2

def do_nothing(x):
    # The call back function
    # Do nothing here
    pass

# Create a black image
img = np.zeros((300, 512, 3), np.uint8)

# Create a window
cv2.namedWindow("trackbar_window")

# create trackbars for color change
cv2.createTrackbar('R','trackbar_window',0,255,do_nothing)
cv2.createTrackbar('G','trackbar_window',0,255,do_nothing)
cv2.createTrackbar('B','trackbar_window',0,255,do_nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,do_nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','trackbar_window')
    g = cv2.getTrackbarPos('G','trackbar_window')
    b = cv2.getTrackbarPos('B','trackbar_window')
    s = cv2.getTrackbarPos(switch,'trackbar_window')

    # If switch is OFF, don't do anything
    if s == 0:
        img[:] = 0
    else:
        # else change the image
        img[:] = [b,g,r]

cv2.destroyAllWindows()
