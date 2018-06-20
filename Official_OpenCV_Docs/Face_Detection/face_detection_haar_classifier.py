# Python fiel which demonstrates how a Haar classifier works


##################

import cv2
import numpy

img = cv2.imread("faces.jpeg", 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Path for XML file
path = "haarcascade_frontalface_default.xml"

# Create a face cascade object

# Loads in teh xml file and performs initialization
face_cascade = cv2.CascadeClassifier(path)

# Now detect faces
# scaleFactor -> We only want faces close to the camera. Therefore scale = 1.05
# minNeighbors -> Minimum number of object detction required before it is considered a face
# minSize -> Actual face size

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, minSize=(40, 40))
print(len(faces))

# Draw the bounding faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness=3)

# Display teh image
cv2.imshow("All Faces", img)

# Wait for usre input
cv2.waitKey(0)

cv2.destroyAllWindows()
