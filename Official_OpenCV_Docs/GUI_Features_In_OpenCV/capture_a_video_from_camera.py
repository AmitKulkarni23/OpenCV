# Python file to capture a video from camera
# API used -> VideoCapture objects APIs
# VideoCapture object takes in teh device index as the argument
# The device index is just a number to specify which camera to use


#########################

# Import the numpy and cv2 modules
import numpy as np
import cv2

# Create a video capture object
cap = cv2.VideoCapture(0)

while(1):
    # Read frame by frame
    ret, frame = cap.read()

    # cvtColor -> Converts an image from one color space to another
    # So we are converting the frame to gray scale here
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Show the frame
    cv2.imshow("Video Frame", img_gray)

    # Press w key to come out of the loop
    if cv2.waitKey(1) & 0XFF == ord('w'):
        # COme out of teh loop
        break

# Release the resources
cap.release()
cv2.destroyAllWindows()
