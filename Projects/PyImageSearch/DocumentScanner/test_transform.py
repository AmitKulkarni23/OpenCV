# Driver code to test top-down view of image

# Import statements
import cv2
import numpy as np
import argparse
import transform

# Parse the user arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="The path to the image")
ap.add_argument("-c", "--coords", help="Comma spearated coordinates of ROi in the image")

args = vars(ap.parse_args())

# Read the image
image = cv2.imread(args["image"])

# Create the points array
pts = np.array(eval(args["coords"]), dtype="float32")

# Call the helper function form the transfor.py file
warped_img = transform.get_fourpoint_transform(image, pts)

# Display both the images
cv2.imshow("Original Image", image)
cv2.imshow("Bird's Eye View", warped_img)

# COORDINATES OF example_01.png image are [(73, 239), (356, 117), (475, 265), (187, 443)]

cv2.waitKey(0)
