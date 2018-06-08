# Python file to check bitwise opeatiosn on images
# bitwise not -> inverts evey pixel in the image
import cv2

messi_image_file_name = "messi_argentina.jpg"
img = cv2.imread(messi_image_file_name)

# Show the original image
cv2.imshow("Original Image", img)
cv2.waitKey(0)

# Show the bitwise_not image
bit_and_img = cv2.bitwise_not(img)
cv2.imshow("Bitwise Not Image", bit_and_img)

cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
