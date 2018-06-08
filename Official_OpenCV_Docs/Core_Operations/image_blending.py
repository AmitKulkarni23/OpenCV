# Python file which demonstartes blending of 2 images
# cv2.addWeighted is the API used

##############################3

import cv2

# Read the 2 images
messi_argentina = cv2.imread("messi_argentina.jpg")
messi_barca = cv2.imread("messi_barca.jpg")

# print(type(messi_argentina))
# print(type(messi_barca))
# print(messi_barca.size)
# print(messi_argentina.sizes)

# Blend the 2 images
# NOTE: For addWeighted to work both teh images should be of the same size
dst = cv2.addWeighted(messi_argentina, 0.4, messi_barca, 0.6, 0)

# Show teh blended image
cv2.imshow("Messi", dst)

# Wait for user input
cv2.waitKey(0)

cv2.destroyAllWindows()
