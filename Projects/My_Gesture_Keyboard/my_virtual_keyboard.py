# Credits -> https://evilporthacker.blogspot.com/2017/10/gesture-driven-virtual-keyboard-using.html

# We are going to design a keyboard which has 26 letters of the alphabet
# and has a space bar

# For each on the virtual keyboard we need 4 things
# - key label - the text displayed on the key
# - top left co-ordinate of the key
# - bottom right co-ordinate of the key
# - center co-ordinate of the key

# Import Statements
import cv2
import numpy as np
import pyautogui as pgui
import pickle

# Read the thresholded image from the .pickle file
pickle_file_name = "hsv_paper.pickle"

with open(pickle_file_name, "rb") as fd:
    t = pickle.load(fd)

# Create a video capture object
video_cap = cv2.VideoCapture(0)

# Get the lower and upper bounds
hsv_lower = np.array([t[0], t[1], t[2]])
hsv_upper = np.array([t[3], t[4], t[5]])

# We need to get the height and width of the ideo frame captured by the camera
video_frame_width = video_cap.get(cv2.CAP_PROP_FRAME_WIDTH)
video_frame_height = video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# Row 1 - 10 keys
# Row 2 - 9 keys
# Row 3 - 7 keys
# Space Bar - equivalent to 5 keys

max_keys_in_row = 10
key_width = video_frame_width // max_keys_in_row


# Now every key is a square( therefore, key_width = key_height)

def get_key_info():
    """
    Function that helps in desigining the keyboard
    Returns the following
    1) Key label
    2) Top left corner coordinate
    3) Bottom right corner coordinate
    4) Center coordinate
    """

    row1_key_width = 10 * key_width # 10 keys in row1
    row2_key_width = 9 * key_width # 9 keys in row2
    row3_key_width = 7 * key_width
    row4_key_width = 5 * key_width

    row_keys = []

    # So the key "q" will be placed at 0, y1
    # where y1 = (video_frame_height - key_width * 4) // 2
    # Why? - Because we need equal margins on both sides( top and bottom)
    # Why * 4 ? - Becuase we have 4 rows

    x1, y1 = 0, (video_frame_height - key_width * 4) // 2
    # Since these are square keys just add keywidth to find the bottom right
    # co-ordinate
    x2, y2 = x1 + key_width, y1 + key_width

    c1, c2 = x1, y1
    count = 0

    keys = "qwertyuiop"
    for i in range(len(keys)):
        row_keys.append([keys[count], (x1, y1), (x2, y2), (int((x2+x1)/2) - 5, int((y2+y1)/2) + 10)])
        # Increment only the x cordinates
        x1 += key_width
        x2 += key_width
        count += 1

    # Copy back the values to x1 and y1
    x1, y1 = c1, c2

    # Second row - has 9 keys
    # To have equal spacing on both the left and right co-ordinates
    # first key in row 2 should be placed a little to teh right of the first
    # key in row1. Similarly the last key should be placed a little to the left of
    # last key in row1
    x1 = (row1_key_width - row2_key_width) // 2
    y1 = y1 + key_width
    x2, y2 = x1 + key_width, y1 + key_width

    c1, c2 = x1, y1

    keys = "asdfghjkl"
    count = 0
    for i in range(len(keys)):
        row_keys.append([keys[count], (x1, y1), (x2, y2), (int((x2+x1)/2) - 5, int((y2+y1)/2) + 10)])
        # Increment only the x cordinates
        x1 += key_width
        x2 += key_width
        count += 1

    # Copy back the values
    x1, y1 = c1, c2

    # Third row
    x1 = (row2_key_width - row3_key_width) // 2
    y1 = y1 + key_width
    x2, y2 = x1 + key_width, y1 + key_width

    c1, c2 = x1, y1

    keys = "zxcvbnm"
    count = 0
    for i in range(len(keys)):
        row_keys.append([keys[count], (x1, y1), (x2, y2), (int((x2+x1)/2) - 5, int((y2+y1)/2) + 10)])
        # Increment only the x cordinates
        x1 += key_width
        x2 += key_width
        count += 1

    # Copy back the values
    x1, y1 = c1, c2

    # For the space bar
    x1 = (row3_key_width - row4_key_width) // 2
    y1 = y1 + key_width
    x2, y2 = x1 + 5 * key_width, y1 + key_width

    c1, c2 = x1, y1

    keys = " "
    count = 0
    for i in range(len(keys)):
        row_keys.append([keys[count], (x1, y1), (x2, y2), (int((x2+x1)/2) - 5, int((y2+y1)/2) + 10)])
        # Increment only the x cordinates
        x1 += key_width
        x2 += key_width
        count += 1


    return row_keys


def perform_key_press():
    """
    Function that sumates a key press
    """
