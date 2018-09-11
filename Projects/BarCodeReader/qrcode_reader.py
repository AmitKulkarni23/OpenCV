# Python file which reads the bar code or QR code presented to it
# Credits:
# 1) https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/
# 2) https://www.learnopencv.com/barcode-and-qr-code-scanner-using-zbar-and-opencv/

# Import Statements
from pyzbar import pyzbar
import cv2
import argparse

# Accept and parse user arguments using argparse
arg_parse = argparse.ArgumentParser()
arg_parse.add_argument("-i", "--image", required=True,
help="Enter the path to the input image")

# Creates a dictionary of arguments parse using argument parser
user_args = vars(arg_parse.parse_args())
print(user_args["image"])

# The color of the rectangle that will be drawn on teh image
rect_color = (0, 255, 0)

# Load the input image
image = cv2.imread(user_args["image"])

# Get all the barcodes or barcodes in this image
# Call the decode function from the
all_codes = pyzbar.decode(image)


# Iterate through all the codes
for item in all_codes:
    # Now extract the bounding box co-ordinates
    (x, y, w, h) = item.rect

    # Draw a cv2 rectangle which wil help us to localize where in the image
    # the bar code or the QR code actually is
    cv2.rectangle(image, (x, y), (x+w, y+h), rect_color, 2)

    # Convert the barcode data(is a bytes object. Needs to be converted to string first)
    code_data = item.data.decode("utf-8")
    code_type = item.type

    # Put this data as a text on teh image
    text = "{} ({})".format(code_data, code_type)
    cv2.putText(image, text, (x, y - 10), cv2.FONT_ITALIC, 0.5, (0, 0, 255), 2)

    # Print the same info on teh console
    print("Code info: Type : {}, Data : {}".format(code_type, code_data))


cv2.imshow("QR/Bar Code Image", image)
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
