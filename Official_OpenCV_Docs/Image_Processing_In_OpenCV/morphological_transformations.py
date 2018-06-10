# Python file to demonstrate morphological transformations
# Credits -> https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html

# 1) Erosion
# - erodes away the boundaries of a foreground object
# - The kernel slides through the image (as in 2D convolution). A pixel in the
#   original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).
# - thickness or size f teh foreground object decreases
# - white region decreases in the image

# 2) Dilation
# - opposite of erosion
# - pixel element is 1 if atleast 1 element under teh kernel is 1
# - increases white region in the image


# 3) Morphological Gradient
# - dilation - erosion
# - result will look like the outline of an image


#####################
import cv2
import numpy as np

# Constants
image_file_name = 'morph.png'

# Read the image as grayscale image
img = cv2.imread(image_file_name,0)

# Create 5x5 kernel
kernel = np.ones((5,5),np.uint8)

# Call eroison API
erosion = cv2.erode(img,kernel,iterations = 1)

dilation = cv2.dilate(img, kernel=kernel, iterations=1)


morph_gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)



# Create Windows
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Original Image", 300, 300)
cv2.namedWindow('Eroded Image',cv2.WINDOW_NORMAL)
cv2.resizeWindow("Eroded Image", 300, 300)
cv2.namedWindow("Dilated Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Dilated Image", 300, 300)
cv2.namedWindow("Morph Gradient Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Morph Gradient Image", 300, 300)

# Display the images
cv2.imshow("Original Image", img)

cv2.imshow("Eroded Image", erosion)

cv2.imshow("Dilated Image", dilation)

cv2.imshow("Morph Gradient Image", morph_gradient)

# Wait for use input
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
