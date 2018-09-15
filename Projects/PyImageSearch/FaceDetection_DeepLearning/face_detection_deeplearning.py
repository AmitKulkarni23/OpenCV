# Python file which detects faces in an image or a video using OpenCV's
# built-in deep learning API

# Credits -> https://www.pyimagesearch.com/2018/02/26/face-detection-with-opencv-and-deep-learning/
# import statements
import cv2
from imutils.video import VideoStream
import argparse
import time
import numpy as np
import imutils

# parse the user arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True, help="The prototxt file")
ap.add_argument("-m", "--model", required=True, help="The caffe model file")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
help="The minimum confidence required to filter out weak detections")

# args is a dictionary of all the user arguments
args = vars(ap.parse_args())

# Load the serailized model from the disk
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

video_stream = VideoStream(src=0).start()

# Wait for the video stream to start
time.sleep(2.0)

# Start looping over the video frames
while True:
    frame = video_stream.read()
    # Resize the frame to have a max width of 400 pixels
    frame = imutils.resize(frame, width=400)

    # get the dimesnions of the frame
    (h, w) = frame.shape[:2]

    # Convert it to a blob
    # blob - Binary large object
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

    # Pass the blob through the network and obtain predictions
    net.setInput(blob)

    # Capture the detection
    detections = net.forward()

    # Loop over all the detctions
    for i in range(0, detections.shape[2]):

        # What is teh confidence of the image
        confidence = detections[0, 0, i, 2]

        if confidence < args["confidence"]:
            # This is a weak confidence
            # we do not want to process this
            continue

        # Compute the (x, y) co-ordinates of the bounding box
        box = detections[0,0,i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        # We need to draw the bounding box around the face and also
        # display the confidence
        text = "{:.2f}%".format(confidence * 100)

        if startY - 10 > 10:
            y = startY - 10
        else:
            y = startY + 10

        # Draw a rectangle
        cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

        # Display the confidence as text
        cv2.putText(frame, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255), 1)


    # Display the image
    cv2.imshow("Face Detction Frame", frame)

    key = cv2.waitKey(1)

    if key == 27:
        # If the user presses ESC
        break


# Destroy all windows
cv2.destroyAllWindows()
video_stream.stop()
