# Python file to save a video file
# API used -> VideoWriter object
# Arguments -> dest_video_file_name, fourcc code, fps, (frame_width, frame_height), isColor flag

# FOURCC -> video codec, XVID, DIVX, X264, MJPG etc..

################################

# Imprt numpy and cv2 modules
import numpy as np
import cv2

# Create a video cpature object
cap = cv2.VideoCapture(0)

# Create the fourcc code
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# Create a VideoWriter object
video_writer = cv2.VideoWriter("my_output.avi", fourcc, 30.0, (900, 600))

while 1:
    return_code, frame = cap.read()

    if return_code == True:
        # Save the video

        # Write this fram
        video_writer.write(frame)

        # Show teh video as well
        cv2.imshow("Video Window", frame)

        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
    else:
        # cap is uninitizlized
        break

# Release everything
cap.release()
video_writer.release()

# Destroy all windows
cv2.destroyAllWindows()
