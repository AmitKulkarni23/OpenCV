# Python file to demonstrate template matching

##########################

import cv2
import numpy as np

# Read the template image
template = cv2.imread("template.jpg", 0)

# Read the actual frame
frame = cv2.imread("players.jpg", 0)


result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)

# get the maximum intensity of matching
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(max_val, max_loc)
cv2.circle(result, max_loc, 15, color=255, thickness=2)

# Display teh images
cv2.imshow("Frame", frame)
cv2.imshow("Template", template)

cv2.imshow("Matching", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
