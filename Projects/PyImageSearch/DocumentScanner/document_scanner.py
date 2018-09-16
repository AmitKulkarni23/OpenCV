# Python file to scan documents which are fed to the program as images

# Credits -> https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/

# Steps Involved
# 1. Edge Detection


# Import Statements
import numpy as np
import cv2
import argparse
import imutils
import transform
from skimage.filters import threshold_local

# parse the user arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="The image that needs to be scanned")

args = vars(ap.parse_args())

# PERFORM EDGE DETECTION(Use Canny Edge Detection method)
image = cv2.imread(args["image"])

# Resize the image to have a height of 500 pixels
ratio = image.shape[0] / 500.0

# Keep a copy of the image
orig_image = image.copy()

# Now resize the image
# imutils.resize -will maintain the aspect ratio
image = imutils.resize(image, height=500)

# Convert the image to grayscale
# Apply Gaussian Blur to remove noise
# Perform Canny edge detection

grayscale_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grayscale_img = cv2.GaussianBlur(grayscale_img, (5, 5), 0)
edges = cv2.Canny(grayscale_img, 75, 200)


# Show the images
cv2.imshow("original Image", image)
cv2.imshow("After Edge Detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
