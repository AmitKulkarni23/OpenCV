# Python file which recognizes the number of fingers pointed out in a hand
# CREDITS -> https://www.youtube.com/watch?v=v-XcmsYlzjA


# Import Statements

import cv2
import numpy as np
import math

rect_x = 100
rect_y = 100
rect_x2 = 300
rect_y2 = 300

# We will draw a blue rectangle on the frame at the above mentioned points
rect_color = (255, 0, 0)

# The region of interest( The blue box where the user places the hand)
roi = None

# The video frame
frame = None

# The skin mask that will be created
skin_mask = None

def main_method():
    """
    Method to start capturing frames from the web cam
    """
    global frame

    # Create a Video Capture Object
    video_cap_obj = cv2.VideoCapture(0)

    # Start reading frames until user presses "ESC" on the keyboard
    while True:
        ret_val, frame = video_cap_obj.read()

        # Flip the array returned
        frame = cv2.flip(frame, 1)

        get_skin_mask(frame)

        key = cv2.waitKey(1)

        if key == 27:
            # The user has pressed ESC
            # Break out of the while loop
            break
    # Release the camera
    video_cap_obj.release()

    # Close all open windows
    cv2.destroyAllWindows()



def get_skin_mask(input_frame):
    """
    Function that calculates ROI and displays teh count of the fingers
    @param input_frame: The input frame from the webcam
    """
    # Now we will extract the region of interest from the input frame
    global rect_x, rect_y, rect_color, rect_width, rect_height, roi, skin_mask

    roi = input_frame[rect_x:rect_x2, rect_y:rect_y2]

    # Draw the rectangle on teh input frame
    cv2.rectangle(input_frame, (rect_x, rect_y), (rect_x2, rect_y2), rect_color, 0)

    # Now convert the region of interest( which falls in teh blue rectangle, where
    # the user places his hand into HSV colorspace)
    # Why HSV - HSV works best for skin detection

    input_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # Define the range of the skin
    # Reference link - https://tinyurl.com/y7gp8scb

    # Use cv2.inRange to perform actual color detection
    # Note: These values need to be changed, if the skin detection is not propers
    lower_bound_skin = np.array([0,20,70], dtype=np.uint8)
    upper_bound_skin = np.array([20,255,255], dtype=np.uint8)

    # Use inRange to extract skin color
    # Anything that will be isnide the lowe_bound - upper_bound will be considered as 1
    # Anything that falls outside this range will be considered as 0
    skin_mask = cv2.inRange(input_hsv, lower_bound_skin, upper_bound_skin)

    # As of now, skin color ( hand ) is in white, the rest of background is black

    remove_noise()

def remove_noise():
    """
    Function which takes in the skin_mask and removes teh noise present in the
    image and finds the contours in the image
    """

    global skin_mask
    kernel = np.ones((3,3),np.uint8)

    # Dilation - is a maximization operation
    # Dilation - increases the bright areas in the image
    # Dilation - makes the object in white bigger
    skin_mask = cv2.dilate(skin_mask,kernel,iterations=4)


    # Gaussian Blur - used to smoothen an image
    # Kernel Size -> ( 5 * 5)
    # sigmaX = 100 , std deviation in X direction
    skin_mask = cv2.GaussianBlur(skin_mask,(5,5),100)

    find_contours_in_skin_mask()

def find_contours_in_skin_mask():
    """
    Helper function which finds the contours present in the skin mask
    """
    global skin_mask

    # Contours -> Curver joining all continuous points having the same color or intensity
    # cv2.RETR_TREE -> Create full family hierarchy list
    # cv2.CHAIN_APPROX_SIMPLE -> removes all redundant
    # points of same intensity and hence reduces memory
    _,contours,hierarchy= cv2.findContours(skin_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # Ok, our hand's contour has the maximum area
    # So we need to work on this contour
    # We will extract this contour from a list of contours

    hand_contour = max(contours, key = lambda x: cv2.contourArea(x))

    # Approximate this hand_contour to further reduce noise
    # epislon - max distance of contour from approximated contour
    epsilon = 0.0005*cv2.arcLength(hand_contour,True)

    approx= cv2.approxPolyDP(hand_contour,epsilon,True)

    create_convex_hull(hand_contour, approx)


def create_convex_hull(hand_contour, approx):
    """
    Function that creates a convex hull around the hand countour
    """

    global roi, skin_mask, frame

    hull = cv2.convexHull(hand_contour)

    # Get the area of the hull
    area_hull = cv2.contourArea(hull)

    # Get the area of the hand
    area_hand = cv2.contourArea(hand_contour)

    # Percentage of area that is not covered by hand in the convex hull
    # This will eventually lead us to defects
    area_ratio = ((area_hull-area_hand)/area_hand)*100


    # Reference -> https://tinyurl.com/y7xr8hoo
    # find the defects in convex hull with respect to hand
    hull = cv2.convexHull(approx, returnPoints=False)

    # Defects are regions that are not covered by hand in the convex hull
    defects = cv2.convexityDefects(approx, hull)

    # If you open your palm, the angle between all the fingers in < 90
    # We need to elimnate defects which have angles greater >= 90

    number_of_defects = 0

    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(approx[s][0])
        end = tuple(approx[e][0])
        far = tuple(approx[f][0])
        pt= (100,180)

        # Find the lenght of all sides of teh triangle
        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)

        # perimeter of teh triangle
        s = (a+b+c)/2

        # The area of the triangle
        ar = math.sqrt(s*(s-a)*(s-b)*(s-c))

        # distance between point and convex hull
        min_dist = (2*ar)/a

        # apply cosine rule here
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57

        # We are only going to consider angles less than 90 degrees
        if angle <= 90 and min_dist > 30:
            number_of_defects += 1

            # Draw a red-circle on this indicating the defect
            cv2.circle(roi, far, 3, [0,0,255], -1)


        # Draw lines around the hand
        cv2.line(roi,start, end, [0,255,0], 2)

    # Number of fingers has to be incremented
    # number of fingers = number of defects + 1
    fingers = number_of_defects + 1

    if fingers == 1:
        if area_hand < 2000:
            # means there is no hand placed in the blue box
            # display a message
            display_message("Place hand in the blue box")

        else:
            if area_ratio < 12:
                # 0 fingers held up
                display_message("0")
            else:
                display_message("1")

    elif fingers == 2:
        display_message("2")

    elif fingers == 3:
        display_message("3")

    elif fingers == 4:
        display_message("4")

    elif fingers == 5:
        display_message("5")
    else:
        display_message("reposition")

    cv2.imshow("Binary Mask Hand", skin_mask)
    cv2.imshow("Output Frame", frame)

def display_message(message):
    """
    Helper function that displays the number of fingers pointed out on the frame
    """

    # refer to teh global frame
    global frame
    font = cv2.FONT_HERSHEY_PLAIN
    org = (0, 50)
    color = (0, 255, 0)
    thickness = 3
    font_scale = 2
    line_type = cv2.LINE_AA

    cv2.putText(frame,message,org, font, font_scale, color, thickness, line_type)


if __name__ == "__main__":
    main_method()
