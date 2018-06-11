# Contours -> curve joining all the continuous points ( along the boundary) haveing same color or intensity
# used in Object Detection adn recognition

# API used -> cv2.findContours()
# 1st arg -> surce image
# 2nd arg -> contour retrieval mode
# 3rd arg -> Contour approximation method
#
# Output:
# contours -> python list of all contours
# hierarchy ->
#
# How to draw contours?
# cv2.drawContours()
# 1st arg -> src image
# 2nd arg -> list of contours
# 3rd arg -> index of contours( to draw all contours pass -1)
# 4th arg -> color
# 5th arg -> thickness


#########################33

import cv2

# Constants
image_file_name = "lena.png"
contours_color = (0, 255, 0) # Green

# Read the image
img = cv2.imread(image_file_name)

# Convert the image to gray scale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Now apply thresholding on the images( beacuse we want to use binary images)
ret,thresh = cv2.threshold(img_gray,127,255,0)


# Use findContours API
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# print teh number of contours
print(type(contours))
print(len(contours))

# Draw all teh contours in teh image
cv2.drawContours(img, contours, -1, contours_color, 3)

# Display the image with contours
cv2.imshow("After Drawing Contours", img)

# Wait for user input
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
