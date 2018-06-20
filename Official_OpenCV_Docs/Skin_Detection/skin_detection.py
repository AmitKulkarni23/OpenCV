# Python file which demonstrates skin detectiop in faces

# THRESHOLDING

# Taking a look at skin tones, no single simple / adaptive thresholding would work
# Therefore we neew to combine 2 or more thresholding


#####################

import cv2
import numpy as np


img = cv2.imread("faces.jpeg", 1)

# Convert the image to hsv file format
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h = hsv[:, :, 0]
s = hsv[:, :, 1]
v = hsv[:, :, 2]

# Display each of theschannels side by side
# axis = 1 -> Concatenate horizontally
hsv_split = np.concatenate((h, s, v), axis=1)
cv2.imshow("Split HSV", hsv_split)

# Apply a thresholding to teh saturation channel
ret, min_sat = cv2.threshold(s, 40, 255, cv2.THRESH_BINARY)
cv2.imshow("Saturation Filter",min_sat)


# Apply thresholding to HUE channel
# cv2.THRESH_BINARY_INV - is the opposite of cv2.THRESH_BINARY
# SO this will make everything from 0 - 15 as white and everything else will be black
ret, max_hue = cv2.threshold(h, 15, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Hue Filter", max_hue)

# Combine the results of both threshold
final = cv2.bitwise_and(min_sat, max_hue)
# Display teh final image
cv2.imshow("Final Combined Image", final)


# Wiat for user input
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
