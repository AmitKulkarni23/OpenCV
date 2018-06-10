# Python file to rotate an image
# Rotation is nothing but translation

# API used -> cv2.warpAffine()

# 1st arg -> source image
# 2nd arg -> teh rotation matrix
# 3rd argument -> output image dimensions

#####################

import cv2

# Constants
angle_of_rotation = 180
img_file_name = "opencv-logo.png"

# Read the image first
img = cv2.imread(img_file_name)

# Okay, now get the width and height of the image
# img is nothing but a numpy array

# img.shape will return us a tuple of teh form ( rows, cols, channels)

w, h = img.shape[:2]

# Calculate teh center of the image
# Why?
# Because we want to rotate teh image around its center point

center = (w / 2, h / 2)

# Now that we have got the center, rotate the image
# We dont want to resize teh image
# Therefore, scale= 1.0
matrix = cv2.getRotationMatrix2D(center, angle_of_rotation, scale = 1.0)

# Perform teh actual rotation
rotated_image = cv2.warpAffine(img, matrix, (w, h))

# Display the images
cv2.imshow("original Image", img)

# Rotated_Image
cv2.imshow("Rotated Image", rotated_image)

# Wait for user input
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
