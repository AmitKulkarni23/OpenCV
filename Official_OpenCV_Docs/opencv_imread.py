# Import numpy and opencv modules
import numpy as np
import cv2

# Load images
# API used -> cv2.imread

# String constant representing image file name
img_file_name = "opencv-logo.png"

# String constant for window name
window_name = "Show_Image_Window"

# Load the default image
default_img = cv2.imread(img_file_name, cv2.IMREAD_COLOR)

# Display the image using imshow
cv2.imshow(window_name, default_img)

# Wait for user response
cv2.waitKey(0)

# Load teh image in gray scale format
gray_scale_format = cv2.imread(img_file_name, cv2.IMREAD_GRAYSCALE)


# Display the gray scale image
cv2.imshow(window_name, gray_scale_format)

# Wait for user input
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
