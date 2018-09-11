##### QR Code and bar Code Reader
Project related to a QR code reader and a bar code scanner in OpenCV

##### Credits
[Learn OpenCV ](https://www.learnopencv.com/barcode-and-qr-code-scanner-using-zbar-and-opencv/)
[PyImage Search](https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/)

##### Library for reading bar codes
[ZBar](http://zbar.sourceforge.net/)

##### Dependencies
- Python package pyzbar ( pip install pyzbar )

##### QR Code and Bar Code Structure
## There are 3 main fields
- Type : Type of QR Code is QR-Code. Type of barcode is CODE-128
- Data : Data embedded inside the barcode / QR code
- Location : Collection of points that locate the QR Code or bar code
             Eg: List of 4 points corresponding to four corners of the QR Code quad
