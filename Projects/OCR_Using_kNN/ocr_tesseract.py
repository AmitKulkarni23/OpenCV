# OCR using tesseract

# tesseract was developed by HP
# tesseract - In version 4, Tesseract has implemented a Long Short Term Memory (LSTM)
# based recognition engine. LSTM is a kind of Recurrent Neural Network (RNN).

# cmd> pip install tesseract

# Tesseract Basic Usage
# input file name:
# OCR languagae -> can be set using the -l option
# OCR Engine Mode (oem) - Tesseract 4 has 2 engines
# a) Legacy Tesseract Engine
# b) LSTM engine
#
# 0 - Legacy Tesseract Engine Only
# 1 - Neural nest LSTM engine only
# 2 - Legacy + LSTM engine
# 3 - Default, based on what is available

# page segmentation mode(psm)

# Credits -> https://www.learnopencv.com/deep-learning-based-text-recognition-ocr-using-tesseract-and-opencv/
######################################################

import cv2
import sys
import pytesseract

if len(sys.argv) < 2:
    print("Usage: python ocr_tesseract.py <image_file_path>")
    sys.exit(1)

image_file_name = sys.argv[1]

# Define teh config paramteres
config = ('-l eng --oem 1 --psm 3')

# Read teh image
img = cv2.imread(image_file_name)

# Call teh tesseract API
text = pytesseract.image_to_string(img, config=config)

# Print the text
print(text)
