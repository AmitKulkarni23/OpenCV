# Contour Features
# - Image Moments
# - Contour Area
# - Contour Perimeter
# - Contour approximation
# - Convex Hull
# - Checking Convexity
# - Bounding Rectangle
# - Minimum Enclosing Circle

###############################

import cv2

# Constants
image_file_name = "contours.png"
contours_color = (255, 0, 0)


# Read the image
img = cv2.imread(image_file_name)

# COnvert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Add thresholding
ret, thresh = cv2.threshold(src=img_gray, thresh=127, maxval=255, type=cv2.THRESH_BINARY)

# Find contours
im2, contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

# Print number of contours
print("Number of contours = ", len(contours))

# Draw the contours
cv2.drawContours(image=img, contours=contours, contourIdx=-1, color=contours_color, thickness=3)

# Display the image
cv2.imshow("Display Contours", img)

# Wait for user input
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
