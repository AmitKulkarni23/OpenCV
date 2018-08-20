# Python file which essentially solves the Where's Waldo puzzle.

# CREDITS -> https://machinelearningmastery.com/using-opencv-python-and-template-matching-to-play-wheres-waldo/

# Note: Waldo is just a visual pattern
# We will us etemplate matching to solve the Where's Waldo puzzle



# We require 2 images
# 1 - puzzle image
# 2 - query image( Waldo's iamge)

# Import Statements
import cv2
import numpy as np
import argparse
# A global dictionary that will hold the path to the
# puzzle image and the query image

args = {}

def parse_arguments():
    """
    Function that utilizes the argparse module and parses the command line
    arguments from the user
    """
    global args

    arg_parser = argparse.ArgumentParser()

    # Accept the path to the puzzle image
    arg_parser.add_argument("-p", "--puzzle_image", required=True, help="Path to puzzle image")

    # Accept the path to teh query image
    arg_parser.add_argument("-q", "--query_image", required=True, help="Path to query image")

    args = vars(arg_parser.parse_args())

def match_template():
    """
    Function that loads the puzzle image and the image and performs template matching
    """
    global args

    # Load the puzzle image
    puzzle_img = cv2.imread(args["puzzle_image"])

    # Load the query image
    query_img = cv2.imread(args["query_image"])

    # Get the shape of the query image
    (q_height, q_width, q_channels) = query_img.shape


    # Find the query image in the puzzle image
    # cv2.matchTemplate API ->
    # parameter 1 -> puzzle image
    # parameter 2 -> query image
    # parameter 3 -> Template matching method
    # How does template matching work?

    # Takes a "sliding window" of our query image and slides it across our
    # puzzle image from left-to-right and top-to-bottom

    # Then for each of the regions, we determine how "good" or "bad" the match is
    # Regions with high coefficient -> match

    result = cv2.matchTemplate(puzzle_img, query_img, cv2.TM_CCOEFF)

    # cv2.minMaxLoc -> gives us where our good matches are
    # cv2.minMax -> finds the global minimum and aximum in an array
    # Returns -> minVal, maxVal, minLoc, maxLoc
    (min_val, max_val, min_loc, max_loc) = cv2.minMaxLoc(result)


    # Now we need to highlight our query image in the puzzle image
    top_left = max_loc

    # Calculate the bottom right co-ordinates
    bottom_right = (top_left[0] + q_width, top_left[1] + q_height)

    # What is out region of interest
    roi = puzzle_img[top_left[1]:bottom_right[1], top_left[0]: bottom_right[0]]


    # Now darken everything in teh puzzle except teh query image( which is our
    # region of interest)
    mask = np.zeros(puzzle_img.shape, dtype="uint8")

    # Now create the transparent effect
    puzzle_img = cv2.addWeighted(puzzle_img, 0.25, mask, 0.75, 0)

    # our puzzle image -> contributes 25% to the transparency
    # the mask -> contributes 75 % to the transparency


    # Highlight the query image region
    # Place roi back into teh image
    puzzle_img[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]] = roi

    # Display the images
    cv2.imshow("Where is Waldo?", puzzle_img)

    cv2.imshow("Waldo image", query_img)

    # Wait for any key press
    cv2.waitKey(0)

    # destroy all open windows
    cv2.destroyAllWindows()


parse_arguments()
match_template()
