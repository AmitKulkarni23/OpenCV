# Python file to scan documents which are fed to the program as images

# Credits -> https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/

# Steps Involved
# 1. Edge Detection
# 2. Fnding Contours
    # - Scanning a piece of paper
    # - A paper is assumed to be rectangle in shape
    # - Rectangle has 4 edges
    # - ASSUMPTION - Largest contour in the image with 4 points is indeed the paper
# 3. Apply 4 point perspective transformation to obatin a bird's eye-view of the
# document


# Import Statements
import numpy as np
import cv2
import argparse
import imutils
import transform
from skimage.filters import threshold_local

# Global variable
# This variable will be populated with the contour outline
# paper = None

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

cv2.imshow("Original Image", image)
cv2.imshow("After Edge Detection", edges)

# Use findContours API
im2, contours, hierarchy = cv2.findContours(edges.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

# Sort contours based on their area
# We are assuming here that the contour with the maximum area is the paper itself
contours = sorted(contours, key = cv2.contourArea, reverse= True)[:5]

# Iterate over these contours
for cont in contours:

    # Approximate the number of points in the contour
    # Use contour features
    perimeter = cv2.arcLength(cont, True)

    # approxPolyDP -> uses Douglas Peucker algorithm to approximate the shape
    # of the polygon
    approx = cv2.approxPolyDP(cont, 0.02 * perimeter, True)


    if len(approx) == 4:
        # Its a rectangle / square
        # means we have found the document in the image
        paper = approx
        break

# Show the images
cv2.drawContours(image, [paper], -1, (0, 255, 0), 2)
cv2.imshow("Contour Outline", image)



# get the TO-DOWN view
# pass the original image and the shape of the paper multiplied by the ratio

warped = transform.get_fourpoint_transform(orig_image, paper.reshape(4, 2) * ratio)

# Convert the warped image and convert it to grayscale
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)

warped = cv2.adaptiveThreshold(warped, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 251, 11)
warped = imutils.resize(warped, height = 500)

# Scanned image
cv2.imshow("Scanned Image", warped)
cv2.waitKey(0)
cv2.destroyAllWindows()
