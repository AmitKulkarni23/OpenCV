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
    cv2.namedWindow("Range Filter Trackbars", 0)

    for i in ["MIN", "MAX"]:
        if i == "MIN":
            v = 0
        else:
            v = 255


        for j in range_filter:
            cv2.createTrackbar("%s_%s" %(j, i), "Range Filter Trackbars", v, 255, callback_func)


def callback_func(dummy_val):
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

def main_func():
    # First accept the user arguments

    args = parse_arguments()
    print(args)

    # Get the range filter from the dictionary
    # Range filter can be either "RGB" or "HSV"
    range_filter = args["filter"].upper()

    # If an image is passed in as argument
    if args["image"]:
        # Read teh image as-is
        frame = cv2.imread(args["image"])

        if range_filter == "RGB":
            # Create a copy, no need to convert the image
            frame_to_thresh = frame.copy()
        else:
            # Need to convert it to HSV
            frame_to_thresh = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    else:
        # We need to capture the image from teh webcam
        # Create a video capture object
        video_cap = cv2.VideoCapture(0)


    # Setup trackbars
    # Call a helper function
    setup_trackbars(range_filter)

    while True:
        if args["webcam"]:
            # Start reading from the web camera
            ret, frame = video_cap.read()

            # if the camera failed to read the image
            # break out of teh while loop

            if not ret:
                print("Camera initialization failed")
                break

            if range_filter == "RGB":
                frame_to_thresh = frame.copy()
            else:
                # HSV color space
                frame_to_thresh = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


        min_1, min_2, min_3, max_1, max_2, max_3 = get_trackbar_values(range_filter)

        # cv2.InRange(image, lower_threshold, upper_thresold)
        # Note -> The cv2.inRange  function expects three arguments:
        # the first is the image  were we are going to perform color detection,
        # the second is the lower  limit of the color you want to detect,
        # and the third argument is the upper  limit of the color you want to detect.

        # After calling cv2.inRange, a binary mask is returned,
        # where white pixels (255) represent pixels that fall into
        # the upper and lower limit range and black pixels (0) do not.
        thresh = cv2.inRange(frame_to_thresh, (min_1, min_2, min_3), (max_1, max_2, max_3))


        # If the user wants a preview of teh thresolded image
        if args["preview"]:
            preview_img = cv2.bitwise_and(frame, frame, mask=thresh)
            # Display this image
            cv2.imshow("Previow image", preview_img)
        else:
            cv2.imshow("Original Image", frame)
            cv2.imshow("Thresholded Image", thresh)

        # We will do a pickle dump of the trackbar values
        # iff presses q
        if cv2.waitKey(1) & 0xFF is ord('q'):
            t_vals = (min_1, min_2, min_3, max_1, max_2, max_3)

            with open("hsv_paper.pickle", "wb") as fd:
                pickle.dump(t_vals, fd)
            fd.close()

            break

if __name__ == "__main__":
    main_func()
