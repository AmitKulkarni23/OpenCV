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

    lines = cv2.HoughLines(edges, 2, np.pi / 180, 300, 0, 0)

    if lines is not None:
        lines = lines[0]

        lines = sorted(lines, key=lambda line:line[0])

        # The x-axis and y-axis position
        x_axis_pos = 0
        y_axis_pos = 0

        for rho, theta in lines:
            a = np.cos(theta)
            b = np.sin(theta)

            x0 = a * rho
            y0 = b * rho

            x1 = int(x0 + 1000 * -b)
            y1 = int(x0 + 1000 * a)
            x2 = int(x0 - 1000 * -b)
            y2 = int(x0 - 1000 * a)

            if b > 0.5:
                # Check the psoition of the line
                if rho - x_axis_pos > 10:
                    x_axis_pos = rho
                    # Draw a line along the edge
                    cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            else:
                if rho - y_axis_pos > 10:
                    y_axis_pos = rho
                    cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)


    # Display the result
    cv2.imshow("Sudoku Solver", frame)
    return_val, frame = video_capture.read()
    key = cv2.waitKey(1)
    if key == 27:
        # User has pressed ESC
        break

# Release the video capture object
video_capture.release()
# Destroy all open windows
cv2.destroyAllWindows()
