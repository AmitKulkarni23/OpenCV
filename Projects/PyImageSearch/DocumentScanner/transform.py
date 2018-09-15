# Python file which does a 4 point perspective transformation
# Inspired by -> https://tinyurl.com/ydbnn8tx


# This is related to obtaining a "TOP-DOWN" view or a "bird's eye view of an image"

# Import statements
import numpy as np
import cv2

def order_points(pts):
    """
    Function that properly orders points of a rectangle
    in an anitclockwise direction, starting from top-left
    i.e top_left-> top_right->bottom-right->bottom-left

    pts -> list of four points specifying the (x, y) coordinates of the rectangle
    """

    # Initialize a list of coordinates that will be ordered
    rect = np.zeros((4, 2), dtype = "float32")

    # top_left -> smallest (x + y) sum
    # bottom_right -> largest(x+y) sum
    s = pts.sum(axis = 1)

    rect[0] = pts[argmin(s)]
    rect[2] = pts[argmax(s)]

    # bottom_left -> largest difference(x - y) points
    # top_right -> largest difference (x - y)
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[2] = pts[np.argmax(diff)]

    # Finally return this ordered ordered points
    return rect
