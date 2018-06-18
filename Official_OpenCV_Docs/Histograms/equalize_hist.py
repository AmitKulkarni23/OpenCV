# Python file to demonstrate histogram equalization
# Increases teh contrast of teh image

# Histogram Equalzation - Stretching teh image to either ends


# API Used:
# cv2.equalizeHist()

# input -> grayscale image
# output -> equalize histrogram image


############################

import cv2
import numpy as np

# Read the image
img = cv2.imread("opencv-logo.png", 0)

# Call equalizeHist API
equlaized_hist_iamge = cv2.equalizeHist(img)

# Stack teh images side-by side
result = np.hstack((img, equlaized_hist_iamge))

# Show teh image
cv2.imshow("Stacked images", result)

# Wait ofr user input
cv2.waitKey(0)

# Destroy all open widows
cv2.destroyAllWindows()
