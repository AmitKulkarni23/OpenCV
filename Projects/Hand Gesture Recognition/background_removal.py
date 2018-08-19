# Python file used to create the BackgroundRemover class
# Idea: There are chances of false positives because the background might
# match with the user's skin

# Therefore before binarization, remove the bacground from the frame
# Step 1) Save a frame(converted to grayscale) and save it as a reference for
# background removal
# ( When the application starts, the first frame is saved as reference.)
# Step 2:  For each new frame we iterate over each pixel of the frame and compare
# it to teh refernce frame

# Step 3) If bg is the refernce frame and nput is teh current frame
# if bg[x, y] - offset <=  input[x, y] <= b[x, y] + offset
# then input[x, y] is classified as background and set to 0.
# Every other pixel in teh frame will be the foreground


import cv2
import numpy as np

class BackgroundRemover:
    """
    Class to remove the background from the current frame
    """

    def __init__(self):
        """
        The constructor
        """
        self.calibrated = False
        self.background = None

    def calibrate(self, input):
        """
        Function that converts the given image to grayscale
        """
        # Get the grayscale image
        self.background = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)

        # Change the flag
        self.calibrated = True

    def get_foreground(self, input_img):
        """
        Function that creates a forground mask and returns the forground image
        """
        foreground_mask = self.get_foreground_mask(input_img)

        if len(foreground_mask.shape) == 3:
            final_foreground = cv2.bitwise_and(foreground_mask, input_img)
        else:
            final_foreground = cv2.bitwise_and(foreground_mask, input_img[:, :, :2])

        return final_foreground


    def get_foreground_mask(self, input_img):
        """
        Function that calculate sthe foreground mask
        """
        w, h, channels = input_img.shape
        # print("SHAPE = ", input.shape)
        fg_mask = np.zeros((w, h, channels), np.uint8)
        if not self.calibrated:
            return fg_mask

        # The calibration is done
        # We have to remove the background i.e compare all pixels
        # in this frame and compare them with the pixels in the
        # reference frame

        fg_mask = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)

        self.remove_background(fg_mask, self.background)

        return fg_mask


    def remove_background(self, input_img, back):
        """
        method that does the pixel by pixel comparison
        """
        # Get the input image's shape first
        rows, cols = input_img.shape

        threshold_offset = 10

        for i in range(rows):
            for j in range(cols):
                frame_pixel = input_img[i][j]
                bg_pixel = back[i][j]

                # Comparison
                if frame_pixel >= bg_pixel - threshold_offset and frame_pixel <= bg_pixel + threshold_offset:
                    # Classify it as background
                    input_img[i][j]= 0
                else:
                    # This is foreground
                    input_img[i][j]= 255


        print("Removing background done")
