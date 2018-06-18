# Python fiel to demonstrate calculation of histrogram for an image and plotting
# it using matplotlib

# API Used:
# cv2.calcHist()
# 1st arg -> image source - grayscale image - [img]
# 2nd arg -> channels
             # [0] - grayscale( for a graysce image)
             # [0] - blue - ( for color image)
             # [1] - green - ( for color image)
             # [2] - red - ( for red image)

# 3rd arg -> mask
    # - to find histogram of full image -> None
    # - otherwise create a mask and pass it

# 4th arg - histSize
# 5th arg - range

# Credits -> https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_histograms/py_histogram_begins/py_histogram_begins.html#histograms-getting-started
#############################

import cv2
import numpy as np
from matplotlib import pyplot as plt

image_file_name = "messi_barca.jpg"

# Read the image
img = cv2.imread(image_file_name, 0);

# Calculate histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Now plot teh histogram
plt.hist(img.ravel(),256,[0,256])
plt.show()


# We can show teh histogram color wise
# color = ("b", "g", "r")
# for i, col in enumerate(color):
#     histr = cv2.calcHist([img],[i],None,[256],[0,256])
#     plt.plot(histr,color = col)
#     plt.xlim([0,256])
# plt.show()
