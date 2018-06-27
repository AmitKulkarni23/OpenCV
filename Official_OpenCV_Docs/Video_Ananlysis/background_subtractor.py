# Python file that demonstrates background subtraction

# Background Subtraction - extract moving foreground from static background
# - Preprocessing step in many vision based applications

# 3 algorithms

# 1)BackgroundSubtractorMOG
# 2)BackgroundSubtractorMOG2
# 3) BackgroundSubtractorGMG
#####################

import cv2

# Create a video capture object
cap = cv2.VideoCapture(0)

# Ok, now create a background object
back_obj = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()

    # get the foreground mask
    foreground_mask = back_obj.apply(frame)

    # Display teh foreground only
    cv2.imshow("Background Subtractor", foreground_mask)


    k = cv2.waitKey(1) & 0Xff
    if k == 27:
        # esc key was pressed
        # break out of while loop
        break

# Release teh resource
cap.release()
cv2.destroyAllWindows()
