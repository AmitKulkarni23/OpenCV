# Python file which recognizes the number of fingers pointed out in a hand
# CREDITS -> https://www.youtube.com/watch?v=v-XcmsYlzjA


# Import Statements

import cv2
import numpy as np


rect_x = 100
rect_y = 100
rect_x2 = 300
rect_y2 = 300

# We will draw a blue rectangle on the frame at the above mentioned points
rect_color = (255, 0, 0)


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
    # Now we will extract the region of interest from the input frame
    global rect_x, rect_y, rect_color, rect_width, rect_height

    roi = input_frame[rect_x:rect_x2, rect_y:rect_y2]

    # Draw the rectangle on teh input frame
    cv2.rectangle(input_frame, (rect_x, rect_y), (rect_x2, rect_y2), rect_color, 0)

    # Now convert the region of interest( which falls in teh blue rectangle, where
    # the user places his hand into HSV colorspace)
    # Why HSV - HSV works best for skin detection

    input_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # Define the range of the skin
    # Reference link - https://tinyurl.com/y7gp8scb

    # Use cv2.inRange to perform actual color detection
    # Note: These values need to be changed, if the skin detection is not propers
    lower_bound_skin = np.array([0,20,70], dtype=np.uint8)
    upper_bound_skin = np.array([20,255,255], dtype=np.uint8)

    # Use inRange to extract skin color

    skin_mask = cv2.inRange(input_hsv, lower_bound_skin, upper_bound_skin)
