# Python file which creates a class called as SkinDetector
# responsible skin detection of the user

import cv2
class SkinDetector:

    def __init__(self):
        """
        The constructor for the SkinDetector class
        """

        # Initialize all instance variables
        # Note: The idea is to capture 2 images of the user's hand
        # and take the average of the colors to form the lower and upper thresholds

        # Note: The image of the hand is converted into the HSV colorspace
        self.h_low_thresh = 0
        self.h_high_thresh = 0

        self.s_low_thresh = 0
        self.s_high_thresh = 0

        self.v_low_thresh = 0
        self.v_high_thresh = 0

        self.calibrated = False

    def skin_color_sampler(self, input):
        """
        Function that draws the rectangle where the user has to place his
        hand on the screen

        @param: input: The input frame capture from the user's camera
        """
        # Get the frame height and frame shape
        frame_height, frame_width = input.shape[:2]

        print("The frame height is ", frame_height)
        print("the frame width is ", frame_width)

        rectangle_size = 20

        # Drawing a recatngle
        # pt1 - Top - left
        # pt2 - Bottom - right
        # cv2.rectangle(img, pt1, pt2, color, thickness)
        rect_color = (255, 0, 255)

        # Draw the 2 sample rectangles on the same input frame
        x1 = frame_width // 5
        y1 = frame_height // 2
        x2 = x1 + rectangle_size
        y2 = y1 + rectangle_size

        # Sample 1
        cv2.rectangle(input, (x1,y1), (x2, y2), rect_color)


        a1 = frame_width // 5
        b1 = frame_height // 3
        a2 = a1 + rectangle_size
        b2 = b1 + rectangle_size

        # Sample Rectangle 2
        cv2.rectangle(input, (a1,b1), (a2, b2), rect_color)
