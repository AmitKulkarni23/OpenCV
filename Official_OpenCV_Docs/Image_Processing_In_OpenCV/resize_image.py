# Resizing the image

# API Used -> cv2.resize()
# 1st argument -> src image
# 2nd argument -> output image

# 3rd argument - dsize - size of teh output image
# If it is 0, it is calculated as dsize = Size(round(fx*src.cols), round(fy*src.rows))}

# 4th argument fx -> scale factor along the horizontal axis
# 5th argument fy -> scale factor along the vertical axis

# 6th argument interpolation -> See src documentation

##################################

import cv2


# Read the image first
img = cv2.imread("opencv-logo.png")

resulting_image = cv2.resize(img, None, fx=0.5, fy = 0.5, interpolation=cv2.INTER_LINEAR)


cv2.imshow("Original Image", img)

cv2.imshow("Resized image", resulting_image)

cv2.waitKey(0)

cv2.destroyAllWindows()
