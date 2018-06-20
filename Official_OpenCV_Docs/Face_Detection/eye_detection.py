# Python file to detect eyes in a face using Harr Classifier


##############

import cv2
import numpy as np

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

#  The path of teh xml file containing pre-trained data for Haar classifier
path = "haarcascade_eye.xml"

# Teh cascade classifier object
eye_cascade_object = cv2.CascadeClassifier(path)

while True:

    # Read the frame
    ret, frame = cap.read()

    # Now we will perform Haar Eye classification here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eyes = eye_cascade_object.detectMultiScale(gray, scaleFactor=1.02, minNeighbors=20, minSize=(10, 10))

    # Now draw teh eyes
    for (x, y, w, h) in eyes:
        # Draw using circle
        xc = (x + x + w) / 2
        yc = (y + y + h) / 2
        radius = w / 2
        cv2.circle(frame, center=(int(xc), int(yc)), radius=int(radius), color=(0, 0, 255), thickness=2)

        cv2.imshow("Eyes", frame)

    # print("Number of eyes = ", len(eyes))

    # Display teh fame
    cv2.imshow("Video Frame", frame)

    # Break out of while loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# REalease teh videocapyure object
cap.release()

# Destroy all open windows
cv2.destroyAllWindows()
