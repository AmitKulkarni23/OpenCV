# Python file which demonstrates image filtering
# Used a 5x5 kernel

# Operation is like this: keep this kernel above a pixel, add all the 25 pixels below this kernel,
# take its average and replace the central pixel with the new average value. It continues this operation for all the pixels in the image.

# API used
# cv2.filter2D
# 1st arg-> src image
# 2nd arg -> desired depth of the destination image; if it is negative, it will be the same as src.depth()
# 3rd arg -> kernel

# Credit -> https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_filtering/py_filtering.html
#########################

import cv2
import numpy as np


image_file_name = "lena.png"

# Read the image
img = cv2.imread(image_file_name)

# Create a 5x5 kernel
kernel = np.ones((5,5),np.float32)/25

# The filtered image
dst = cv2.filter2D(img,-1,kernel)


# Display the images
cv2.imshow("Original Image", img)

cv2.imshow("Smoothed Image", dst)

# Wait for user input
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
