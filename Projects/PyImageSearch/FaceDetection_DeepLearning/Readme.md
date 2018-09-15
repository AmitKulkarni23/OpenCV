##### Credits -> [PyImageSearch Face Detection](https://www.pyimagesearch.com/2018/02/26/face-detection-with-opencv-and-deep-learning/)

##### Face Detection using Deep Learning
- OpenCV 3.3 was released with dnn module( Deep Neural Networks)
- Comes with a Caffe based face detector
- Can be found in opencv/samples/dnn/face_detecor

- To use OpenCV's DNN module with Caffe models we need 2 sets of files
- .prototxt file - which defines the model architecture
- .caffemodel - which contains the weights for the actual layers

- OpenCV's Haar cascade do not work perfectly on faces that are at an angle
  The deep learning method works perfectly fine

##### How Does OpenCV's deep learning face detector work?
- Works on a single shot face detector


##### Screenshots
![DNN Face Recognition](https://github.com/AmitKulkarni23/OpenCV/blob/master/Projects/PyImageSearch/FaceDetecion_DeepLearning/face_recognition.JPG)
