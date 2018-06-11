# Canny Edge detection

# API used -> cv2.Canny()
# 1st arg -> Src Image
# 2nd arg -> minVal
# 3rd arg -> maxVal
# 4th arg -> aperture_size -> size of kernel used to find Sobel derivatives(optional)
#            by default this is 3
# 5th arg -> L2gradient -> specifies the equation for finding gradient magnitude


###############################

import cv2

image_file_name = "lena.png"

# Read the image
img = cv2.imread(image_file_name)

canny = cv2.Canny(img, 200, 200)

# Display teh images
cv2.imshow("Original Image", img)

cv2.imshow("Canny Edges", canny)

# Wait for user input
cv2.waitKey(0)

#Destroy all windows
cv2.destroyAllWindows()
