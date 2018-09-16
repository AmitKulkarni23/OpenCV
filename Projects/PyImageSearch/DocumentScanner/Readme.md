##### Document Scanner
- A Python and OpenCV application that acts a document scanner

##### Credits
  - https://tinyurl.com/y7vwm4lz


##### Steps Involved
  - Edge Detection
  - Finding Contours
      - Scanning a piece of paper
      - A paper is assumed to be rectangle in shape
      - Rectangle has 4 edges
      - ASSUMPTION - Largest contour in the image with 4 points is indeed the paper
  - Apply 4 point perspective transformation to obatin a bird's eye-view of the document

##### Screenshots
![Finding Edges](https://github.com/AmitKulkarni23/OpenCV/blob/master/Projects/PyImageSearch/DocumentScanner/Step_1.JPG)

![Contour Outline](https://github.com/AmitKulkarni23/OpenCV/blob/master/Projects/PyImageSearch/DocumentScanner/contour_outline.JPG)

![Final Image](https://github.com/AmitKulkarni23/OpenCV/blob/master/Projects/PyImageSearch/DocumentScanner/Final_Image.JPG)
