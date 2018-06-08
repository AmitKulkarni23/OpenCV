# Python file which demontrates mouse button events in OpenCV
# Example sof mouse events
# EVENT_LBUTTONDBLCLK
# EVENT_LBUTTONDOWN
# EVENT_LBUTTONUP
# EVENT_MBUTTONDBLCLK
# EVENT_MBUTTONDOWN
# EVENT_MBUTTONUP
# EVENT_MOUSEHWHEEL
# EVENT_MOUSEMOVE
# EVENT_RBUTTONDBLCLK
# EVENT_RBUTTONDOWN
# EVENT_RBUTTONUP
#########################################
import numpy as np
import cv2

# This is the callback function
# The callback function takes 5 arguments
def show_event_names(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Left Button down pressed")

    if event == cv2.EVENT_RBUTTONDOWN:
        print("Right mouse button down pressed")

    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("Left button double clicked")

    if event == cv2.EVENT_RBUTTONDBLCLK:
        print("Right button double clickde")


# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',show_event_names)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
