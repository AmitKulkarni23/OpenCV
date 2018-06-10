# Python file which captures video from teh camera and displays only the red color
# Everything else is blacked out

# OpenCV has >150 color spaces
# But 2 of teh important ones are BGR -> HSV and BGR -> Gray
# Changing Colorspaces - used API cv2.cvtColor

# Why HSV for color detection?
# Will help in pinpointing a more specific color


# What is HSV -> Hue, Saturation and Value
# Hue - color
# Stauration - Strenght of color
# Value - for light

# Credits: https://pythonprogramming.net/color-filter-python-opencv-tutorial/


###################################


import cv2
import numpy as np

# Creat a VideoCapture object
cap = cv2.VideoCapture(0)

while 1:
    # Read frame-by-frame from teh camera
    _, frame = cap.read()

    # Change to hsv colorspace
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Specify red ranges
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])

    # So we will be seeing anything in the ranges of 30-255, 150-255 and 50-180
    # Mask that is created using inRange is eitehr true or false
    # i.e black or white( See the mask image for more clarity)
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # This is our result
    # we show color where there is the frame AND the mask.
    # The white part of the mask will be red range, that was converted to pure white, while everything else became black.
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('Original Video',frame)
    cv2.imshow('Mask using inRange',mask)
    cv2.imshow('Resultant Video',res)

    k = cv2.waitKey(5) & 0xFF
    # Break out of while loop on press of 'ESC'
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
