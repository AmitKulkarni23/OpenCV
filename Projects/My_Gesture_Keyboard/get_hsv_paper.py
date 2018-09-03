# Python file which sets up a trackbar for the user to determine the HSV
# colors of the paper being held up in front of the camera
# Finally, a .pickle file is generated
# What is pickle in Python? - Object hierarchy is converted into byte stream


# import statements
import argparse
import pickle
from operator import xor
import cv2

# Parse the arguments first
def parse_arguments():
    """
    Function to parse the arguments that the user enters on the command line
    """

    # Create an object of the type Argument Parser
    ap = argparse.ArgumentParser()

    # Note: store_true and store_false -> Special cases of store_const
    # either store True or False
    ap.add_argument("-f", "--filter", required=True, help="Range filter(BGR or HSV)")
    ap.add_argument("-i", "--image", required=False, help="Path to image file")
    ap.add_argument("-w", "--webcam", required=False, help="Use webcam", action="store_true")
    ap.add_argument("-p", "--preview", required=False,
    help="Show image preview after applying mask",
    action="store_true")

    # vars -> Converts object into a dictionary
    args = vars(ap.parse_args())

    # If either the image has not been supplied or the webcam is not provided as
    # an option print out an error message

    if not xor(bool(args['image']), bool(args['webcam'])):
        ap.error("Please specify 1 image source")

    if not args["filter"].upper() in ["RGB", "HSV"]:
        ap.error("Please specify either 'rgb' or 'hsv' color filter")


    return args

def setup_trackbars(range_filter):
    """
    Function to setup trackbars on the user screen
    @range_filter: either RGB or HSV
    """
    # Create a new cv2 window
    cv2.namedWindow("trackbars")

    for i in ["MIN", "MAX"]:
        if i == "MIN":
            v = 0
        else:
            v = 255


        for j in range_filter:
            cv2.createTrackbar("%s_%s" %(j, i), "Range Filter Trackbars", v, 255, callback_func)


def callback_func():
    """
    A dummy call back function for the onChange event
    """
    pass


def get_trackbar_values(range_filter):
    """
    Function to get the trackbar values set by the user
    @range_filter : The range filter passed in the user as command line
    argument( either HSV or RGB)
    """

    track_values = []

    for i in ["MIN", "MAX"]:
        for j in range_filter:
            # getTrackbarPos - (trackbarname, windowname)
            v = cv2.getTrackbarPos("%s_%s" %(j, i), "Range Filter Trackbars")
            track_values.append(v)

    return track_values
