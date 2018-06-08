# Placing image over another image using ROI
# Use of bitwise operations and image thresholding

# API used
# cv2.threshold
# 1st arg -> gray scale image
# 2nd arg -> threshold value used to classify the images
# 3rd arg -> Value to be given if pixel value is more than threshold value
# 4th arg -> different styles of thresholding


###################################

import cv2

# File names for images
messi_file_name = "messi_barca.jpg"
opencv_logo_file_name = "opencv-logo.png"

# Read the images
messi_image = cv2.imread(messi_file_name)
opencv_image = cv2.imread(opencv_logo_file_name)


# Get the rows, columns and channels for opencv image
rows, columns, channels = opencv_image.shape

# Now create a region of interest in teh first image
# Top left corner
roi = messi_image[0:rows, 0:columns]



# Now perform image thresholding
# Image thresholding requires a gray scale image
opencv_image_gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)

# Show opencv_image_gray
# cv2.imshow("OpenCV Gray Wimdow", opencv_image_gray)


# Actual image thresholding
ret, mask = cv2.threshold(opencv_image_gray, 10, 255, cv2.THRESH_BINARY)

# Calculate the inverse of mask as well
mask_inv = cv2.bitwise_not(mask)

# Lets display the thresholded image
# cv2.imshow("Thresholded Image", mask)


# print(roi)
# lets show teh region of interest
# cv2.imshow("ROI Window", roi)


# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
# cv2.imshow("img1_bg Window", img1_bg)


# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(opencv_image,opencv_image,mask = mask)
# cv2.imshow("img2_fg Window", img2_fg)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
messi_image[0:rows, 0:columns] = dst


# Final Dipslay
cv2.imshow("Mesi Image After Operation", messi_image)

# Wait for user input from keyboard
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
