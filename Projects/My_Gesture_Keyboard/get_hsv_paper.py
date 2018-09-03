# Python file which sets up a trackbar for the user to determine the HSV
# colors of the paper being held up in front of the camera
# Finally, a .pickle file is generated
# What is pickle in Python? - Object hierarchy is converted into byte stream


# import statements
import argparse
import pickle
from operator import xor


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
