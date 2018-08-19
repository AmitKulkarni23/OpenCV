# Python file which creates a class called as SkinDetector
# responsible skin detection of the user

import cv2
import numpy as np

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

        # print("The frame height is ", frame_height)
        # print("the frame width is ", frame_width)

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

    def calibrate(self, input):
        """
        Function to perform calibration
        Calculate the user's skin color through thresholding
        """
        frame_height, frame_width = input.shape[:2]

        # Convert the image to a hsv color space
        hsv_input = cv2.cvtColor(input, cv2.COLOR_BGR2HSV)

        # ASSUMPTION -> We are cropping an image using
        # Cropping hsv_input
        # What are we cropping? What is our region of interest?
        samp1_x = frame_width // 5
        samp1_y = frame_height // 2
        samp1_w = 20
        samp1_h = 20

        samp2_x = frame_width // 5
        samp2_y = frame_height // 3
        samp2_w = 20
        samp2_h = 20

        sample_1 = hsv_input[samp1_y:samp1_y+samp1_h, samp1_x:samp1_x+samp1_w]
        sample_2 = hsv_input[samp2_y:samp2_y+samp2_h, samp2_x:samp2_x+samp2_w]

        # Calculate the thresolds for these images
        self.calculate_thresholds(sample_1, sample_2)

        self.calibrated = True


    def calculate_thresholds(self, sample1, sample2):
        """
        Function to actually cacluate the skin HSV thresholds
        """
        offset_low_thresh = 80
        offset_high_thresh = 30

        # cv2.mean(array) -> Calcuates the mean of array elements
        hsv_mean_sample_1 = cv2.mean(sample1)

        hsv_mean_sample_2 = cv2.mean(sample2)

        # H Value
        self.h_low_thresh = min(hsv_mean_sample_1[0], hsv_mean_sample_2[0]) - offset_low_thresh
        self.h_high_thresh = max(hsv_mean_sample_1[0], hsv_mean_sample_2[0]) + offset_high_thresh

        # S Value
        self.s_low_thresh = min(hsv_mean_sample_1[1], hsv_mean_sample_2[1]) - offset_low_thresh
        self.s_high_thresh = max(hsv_mean_sample_1[1], hsv_mean_sample_2[1]) + offset_high_thresh

        self.v_low_thresh = min(hsv_mean_sample_1[2], hsv_mean_sample_2[2]) - offset_low_thresh
        self.v_high_thresh = max(hsv_mean_sample_1[2], hsv_mean_sample_2[2]) + offset_high_thresh

        # print("Done calculating thresholds")
        # print(self.calibrated)

    def get_skin_mask(self, input):
        """
        Function to get the skin mask
        """
        w, h, channels = input.shape
        skin_mask = np.zeros((w, h, channels), np.uint8)

        if not self.calibrated:
            # The user has performed any calibration
            # Retrun a numpy array of zeroes
            return skin_mask

        hsv_input = cv2.cvtColor(input, cv2.COLOR_BGR2HSV)

        # skin_mask = cv2.inRange(hsv_input,
        #             (self.h_low_thresh, self.s_low_thresh, self.v_low_thresh),
        #             (self.h_high_thresh, self.s_high_thresh, self.v_high_thresh))

        skin_mask = cv2.inRange(hsv_input,
                    np.array([self.h_low_thresh, self.s_low_thresh, self.v_low_thresh]),
                    np.array([self.h_high_thresh, self.s_high_thresh, self.v_high_thresh]))

        structuring_element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
        skin_mask = cv2.morphologyEx(skin_mask, cv2.MORPH_OPEN, structuring_element)

        kernel = np.ones((3,3),np.uint8)
        skin_mask = cv2.dilate(skin_mask, kernel, 3)

        return skin_mask
