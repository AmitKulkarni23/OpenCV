# Python file which uses Hough Line Transform technique to perform grid detection
# on the Sudoku material

# import statements
import cv2
import numpy as np

# Global variables
# Create a named window
cv2.namedWindow("Sudoku Solver")
minVal = 30
ratio = 3

# We will input the Sudoku image to the program with the help of the web camera
# Therefore, create a video capture object

video_capture = cv2.VideoCapture(0)

if video_capture.isOpened():
    return_val, frame = video_capture.read()
else:
    print("The web camera failed to initialize")
    return_val = False

while return_val:
    # Perform pre-processing of the image'
    sudoku_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Blur this image to remove any noise in the image
    # cv2.blur - Averaging
    # Takes the average of all the pixels under the kernel area and replaces the
    # current element by this average
    # The kernel here is a 3 x 3 kernel
    sudoku_img = cv2.blur(sudoku_img, (3, 3))


    # Now apply Canny edge detection
    # Canny Edge Detecion has a total of 5 stages
    # Credits -> https://docs.opencv.org/3.1.0/da/d22/tutorial_py_canny.html
    # 1) Noise Reduction
    # 2) Find intensity gradient of the image
    # 3) Non-Maximum Supression
    # 4) Hysteresis Thresholding

    # cv2.cannyimage, minVal, maxVal)
    edges = cv2.Canny(sudoku_img, minVal, minVal * ratio)

    # Now apply Hough Line transform to these edges
    # Working of Hough Line Transform
    # Credits -> https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html
    # Essentially Hough Line Transform works as a voting system
    # rho = x * costheta + y * sintheta
    # where rho is the perpendicular distance between the origin and the line
    # theta - the angle it forms with the x-axis

    
