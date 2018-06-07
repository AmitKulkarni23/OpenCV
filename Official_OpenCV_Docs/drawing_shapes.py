# Python file to draw shapes like line, rectangle, ellipse etc..
# cv2.line(), cv2.circle() , cv2.rectangle(), cv2.ellipse(), cv2.putText()
# img : The image where you want to draw the shapes
# color : Color of the shape. for BGR, pass it as a tuple, eg: (255,0,0) for blue.
 # For grayscale, just pass the scalar value.
# thickness : Thickness of the line or circle etc. If -1 is passed for closed figures
# like circles, it will fill the shape. default thickness = 1
# lineType : Type of line, whether 8-connected, anti-aliased line etc. By default,
# it is 8-connected. cv2.LINE_AA gives anti-aliased line which looks great for curves.


#########################
import numpy as np
import cv2


# Draw a line
# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),5)


# draw a rectangle
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Draw a circle
cv2.circle(img,(447,63), 63, (0,0,255), -1)

# Adding text to image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)


cv2.imshow("Geometrical Figures", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
