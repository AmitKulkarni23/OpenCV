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
key_width = int(video_frame_width / max_keys_in_row)

cv2.namedWindow("My Virtual Keyboard", cv2.WINDOW_FREERATIO)
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

    x1, y1 = 0, int((video_frame_height - key_width * 4) / 2)
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
    x1 = int((row1_key_width - row2_key_width) / 2)
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
    x1 = int((row2_key_width - row3_key_width) / 2)
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
    x1 = int((row3_key_width - row4_key_width) / 2) + x1
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


def perform_key_press(image, center, row_key_points):
    """
    Function that simulates a key press
    image : the image object
    center : the position of click
    row_keys
    """
    # If the position of click is (x, y)
    # then teh key pressed will be (x1<=x<=x2, y1<=y<=y2)

    for item in row_key_points:
        top_left = list(np.int0(np.array(center)) >= np.array(item[1]))
        bottom_right = list(np.int0(np.array(center)) <= np.array(item[2]))

        if top_left == [1, 1] and bottom_right == [1, 1]:
            # We have identified the key to press
            print("Performing key press", item[0])
            pgui.press(item[0])
            # Indicate that the key is pressed with a blue mark on the key
            cv2.fillConvexPoly(image, np.array([np.array(item[1]), np.array([item[1][0], item[2][1]]), np.array(item[2]), np.array([item[2][0], item[1][1]])]), (255, 0, 0))

    return image

def main_func():
    """
    Function that performs the following
    - Recognizes the yellow paper
    - Gets the corner co-ordinates of every key by calling get_keys()
    - Detects the center position of the yellow paper
    - If the click gesture is valied calls the perform_key_press() function
    """

    # get the keys first
    row_key_points = get_key_info()
    new_area = 0
    old_area = 0

    c, c2 = 0, 0

    is_key_pressed = False

    while True:
        # Start reading teh frames from teh webacme
        frame = video_cap.read()[1]

        frame = cv2.flip(frame, 1)

        # Convert the given image to HSV format
        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Apply the mask
        mask = cv2.inRange(frame_hsv, hsv_lower, hsv_upper)

        # Smoothen the image
        # Apply median blur -> runs through each element of the image
        # and replaces teh pixel with the median of the neighbouring
        # pixels

        blur = cv2.medianBlur(src=mask, ksize=15)

        # Now apply Guassian filter
        blur = cv2.GaussianBlur(blur, (5, 5), 0)


        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

        # What are contours? - Contours can be explained simply as a curve
        # joining all the continuous points (along the boundary), having same color or intensity
        # 1st parameter - source image
        # 2nd paramter - retrieval mode
        # 3rd paramtere - Approximation method
        # ( CHAIN_APPROX_NONE -> all the boundary points are stored)
        contours = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[1]


        if len(contours) > 0:
            # get the contour with the maximum area
            countour_max_area = max(contours, key=cv2.contourArea)

            if cv2.contourArea(countour_max_area) > 350:
                # cv2.minAreaRect -> returns the minimum-area bounding rectangle
                # it returns a box2d structure - ( center (x,y), (width, height), angle of rotation )
                rect = cv2.minAreaRect(countour_max_area)

                center = rect[0]

                # But to draw this recatngle, we need 4 corners of the rectangle
                # Therefore we use the API - cv2.boxPoints()
                box = cv2.boxPoints(rect)

                box = np.int0(box)

                # Draw a a green dot / circle on the center of teh yellow paper
                cv2.circle(frame, tuple(np.int0(center)), 2, (0, 255, 0), 2)
                # Draw a red rectangle / bounding box around the yellow paper
                cv2.drawContours(frame,[box],0,(0,0,255),2)

                # For every 3rd iteration we calculate the difference of area
                # What is area? - the area of the contour
                # What contour -> The max contour in the yellow paper

                new_area = cv2.contourArea(countour_max_area)
                new_center = np.int0(center)

                # Area caclulation
                if c == 0:
                    old_area = new_area
                c += 1
                diff_area = 0

                if c > 3:
                    # After every 3rd iteration teh differenc in area is calculated
                    diff_area = new_area - old_area
                    c = 0

                # Center Calculation
                if c2 == 0:
                    old_center = new_center

                c2 += 1
                diff_center = np.array([0, 0])

                if c2 > 5:
                    # After every 5 iterations we calculate teh new center
                    diff_center = new_center - old_center
                    c2 = 0


                center_thresh = 10
                area_thresh = 200

                if abs(diff_center[0]) < center_thresh or abs(diff_center[1]) < center_thresh:
                    if diff_area > area_thresh and is_key_pressed == False:
                        # Everything is in proper state
                        # The yellow paper is newar the webcam is not moving too
                        # fast or too slow. IT IS A CLICK gesture
                        frame = perform_key_press(frame, new_center, row_key_points)
                        is_key_pressed = False
                    elif diff_area < -(area_thresh) and is_key_pressed == True:
                        # The user has moved away from the screen after the key press has occurred
                        is_key_pressed = False
            else:
                is_key_pressed = False
        else:
            is_key_pressed = False

        # Dipslay the keyboard no matter what
        for key in row_key_points:
            cv2.putText(frame, key[0], key[3], cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0))
            cv2.rectangle(frame, key[1], key[2], (0, 255, 0), thickness = 2)

        cv2.imshow("My Virtual Keyboard", frame)

        if cv2.waitKey(1) == ord('q'):
            # Break out of while loop if the user presses q
            break

    # Relase all resources
    video_cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main_func()
