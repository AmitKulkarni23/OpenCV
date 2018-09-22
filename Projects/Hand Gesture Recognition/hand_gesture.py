# Python file which recognizes the number of fingers raised on a hand
# using OpenCV


# Steps Involved
# 1) Segmentation -> Extracting objects of interest
# How to segment? - Find the color of the user's skin and use it to binarize
# the image

# 1a) How to find the color of the skin?
# - The user has tp place his hand in a designated rectangle
# - The s key on the keyboard saves the images in the rectangle area
# - The 2 average colors are used as the lower and upper thresholds and are used
#   to find the user's skin



# Credits -> https://tinyurl.com/ycyxuvdk


# Import statements
import cv2
import numpy as np
from skin_detector import SkinDetector
from face_detector import FaceDetector
from background_removal import BackgroundRemover

def main_method():
    """
    This is our main method
    """

    # Create a video capture object
    # Why do we need a video capture object?
    # We are going to be giving the program input frames in real-time

    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        print("Camera is busy. Exiting the program")
        return -1

    # Create all the necessary objects
    skin_det = SkinDetector()
    face_det = FaceDetector()
    back_rem = BackgroundRemover()

    while True:

        # Read the frames from the camera
        return_code, frame = video_capture.read()

        frame_out = frame.copy()

        # Draw the sample rectangles, where teh user has to place his hand
        skin_det.skin_color_sampler(frame_out)

        # Remove the background for better results
        # foreground = back_rem.get_foreground(frame)

        # Face Detector
        face_det.remove_faces(frame)
        #
        hand_mask = skin_det.get_skin_mask(frame);

        cv2.imshow("Frame Out Window", frame_out)
        cv2.imshow("Hand Mask", hand_mask)

        key = cv2.waitKey(1)
        # Break out of teh while loop on pressing 'q'
        if key & 0xFF == ord('q'):
            print("Qutting Now")
            break
        elif key == 98:
            # user has pressed 'b'
            # Remove background
            back_rem.calibrate(frame)
        elif key == 115:
            # The user pressed s
            # Then we need to calibrate
            skin_det.calibrate(frame)



    # Release teh videocapyure object
    video_capture.release()

    # Destroy all open windows
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main_method()
