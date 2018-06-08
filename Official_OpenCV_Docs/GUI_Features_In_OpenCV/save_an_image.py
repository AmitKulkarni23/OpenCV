# Python file to save an image to disk
# API used -> cv2.imwrite
# 1st arg -> File name to be saved
# 2nd arg -> Image that will be saved


############################

import cv2
import numpy as np

# Source image filename
src_image_filename = "opencv-logo.png"

# Destination filename
dest_file_name = "opencv.jpg"


# Read the file using imread
img = cv2.imread(src_image_filename, cv2.IMREAD_GRAYSCALE)

# Save teh file using imwrite
# This will create a grayscale image and save it in teh same folder
cv2.imwrite(dest_file_name, img)
