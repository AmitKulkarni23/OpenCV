# Image Gradients - are nothing but high pass filters
# Can be used to detect edges in images

# OpenCV provides 3 types of HPF
# Sobel, Scharr and Laplacian

###############################

import cv2
import numpy as np

# Create a video capture object
cap = cv2.VideoCapture(0)

while 1:
    # Read fame by frame
    _, frame = cap.read()

    # Laplacian edge detection
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)

    # Sobel x
    sobel_x = cv2.Sobel(frame, cv2.CV_64F, 1, 0, 5)

    # Sobel y
    sobel_y = cv2.Sobel(frame, cv2.CV_64F, 0, 1, 5)

    # Show the image
    cv2.imshow("Original Frame", frame)

    cv2.imshow("Laplacian", laplacian)

    cv2.imshow("Sobel X", sobel_x)

    cv2.imshow("Sobel Y", sobel_y)


    # 0xFF is a hexadecimal constant which is 11111111
    # in binary. By using bitwise AND (&) with this constant,
    # it leaves only the last 8 bits of the original (in this case, whatever cv2.waitKey(0) is)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        # Exit out of teh while loop
        break

# Destroy all windows and release teh video capture resource
cv2.destroyAllWindows()

cap.release()
