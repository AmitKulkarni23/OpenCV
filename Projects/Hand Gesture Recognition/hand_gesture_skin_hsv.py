# Python file which recognizes the number of fingers pointed out in a hand
# CREDITS -> https://www.youtube.com/watch?v=v-XcmsYlzjA


# Import Statements

import cv2
import numpy as np




def main_method():
    """
    Method to start capturing frames from the web cam
    """
    # Create a Video Capture Object
    video_cap_obj = cv2.VideoCapture(0)

    # Start reading frames until user presses "ESC" on the keyboard
    while True:
        ret_val, frame = video_cap_obj.read()

        # Flip the array returned
        frame = cv2.flip(frame, 1)

        display_count(frame)


        key = cv2.waitKey(1)

        if key == 27:
            # The user has pressed ESC
            # Break out of the while loop

    # Release the camera
    video_cap_obj.release()

    # Close all open windows
    cv2.destroyAllWindows()



def display_count(input_frame):
    """
    Function that calculates ROI and displays teh count of the fingers
    @param input_frame: The input frame from the webcam
    """
    
