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

    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    # bottom_left -> largest difference(x - y) points
    # top_right -> largest difference (x - y)
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    # Finally return this ordered ordered points
    return rect


def get_fourpoint_transform(image, pts):
    """
    Function that returns the top-down view of an image

    pts - list of 4 points that contains the ROI of the image
    """

    rect = order_points(pts)

    # Unpack the four corners of the rectangle
    (tl, tr, br, bl) = rect

    # Compute the width of the image
    # width = max(dist(br, bl), dis(tr, tl))
    width_a = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    width_b = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))

    max_width = max(int(width_a), int(width_b))

    # Compute the height of the image
    # height = max(dist(tr, br), dist(tl, bl))

    height_a = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    height_b = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))

    max_height = max(int(height_a), int(height_b))

    # Construct the bird's eye view of the image
    # in the tl, tr, br and bl order

    dest = np.array([[0, 0], [max_width - 1, 0], [max_width-1, max_height-1], [0, max_height-1]], dtype="float32")

    my_matrix = cv2.getPerspectiveTransform(rect, dest)
    # Apply this perspective transform
    warped = cv2.warpPerspective(image, my_matrix, (max_width, max_height))


    return warped
