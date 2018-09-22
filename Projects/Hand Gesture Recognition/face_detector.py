# Python file which creates a class called as FaceDetector and removes the face
# from the binary image by drawing a rectangle over the face

import cv2
class FaceDetector:
    """
    Class to detect and remove faces from the input image
    using Haar Cascade
    """
    def __init__(self):
        """
        The constructor.
        Loads the haar cascade xml file
        """
        # Loads in teh xml file and performs initialization
        path = "haarcascade_frontalface_default.xml"
        self.face_cascade = cv2.CascadeClassifier(path)


    def remove_faces(self, input):
        """
        Function to f=draw a black rectangle over the face
        """

        gray = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)

        # Now detect faces
        # scaleFactor -> We only want faces close to the camera. Therefore scale = 1.05
        # minNeighbors -> Minimum number of object detction required before it is considered a face
        # minSize -> Actual face size

        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2, minSize=(120, 120))

        # For each detected face in faces
        # Draw a black recatngle over it

        for (x, y, w, h) in faces:
            cv2.rectangle(input, (x,y), (x+w, y+h), (0, 0, 0), thickness=-1)
