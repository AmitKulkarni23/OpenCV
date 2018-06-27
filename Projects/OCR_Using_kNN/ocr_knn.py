# Python file which demonstrates usage of kNN algorithm to perform OCR

# Training data - digits.png - which has 5000 handwritten digits (500 for each digit).
# Each digit is a 20x20 image.

# Idea:
# 1) Split the image into 5000 different digits
# 2) For each digiit we flatten it into a single row with 400 pixels( This is our feature set)
# 3) Use first 250 samples as train_data and next 250 samples as test_data

# Credits -> https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_ml/py_knn/py_knn_opencv/py_knn_opencv.html

#############################################

import cv2
import numpy as np

# Image file name
img_file_name = "digits.png"

# Read the image
img = cv2.imread(img_file_name)

# Convert tit to grayscale
gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# numpy.vsplit -> Split an array into multiple sub-arrays vertically (row-wise).
# Example:

# x = array([[  0.,   1.,   2.,   3.],
#        [  4.,   5.,   6.,   7.],
#        [  8.,   9.,  10.,  11.],
#        [ 12.,  13.,  14.,  15.]])

# np.vsplit(x, 2)

# [array([[ 0.,  1.,  2.,  3.],
#        [ 4.,  5.,  6.,  7.]]),
#  array([[  8.,   9.,  10.,  11.],
#        [ 12.,  13.,  14.,  15.]])]


# Similarly numpy.hsplit -> Split an array into multiple sub-arrays horizontally (column-wise).

cells = [np.hsplit(row, 100) for row in np.vsplit(gray_scale, 50)]

# Ok we have got the cells. Convert this into a numpy array
img_array = np.array(cells)


# Prepare test data and train data
# Note: numpy.reshape -> -1 is passed we are indicating to numpy that we do not
# know the dimension in 1 direction

# numpy.repeat -> Repeat the elements op an array for n number of times
train = img_array[:,:50].reshape(-1,400).astype(np.float32) # Size = (2500,400)
test = img_array[:,50:100].reshape(-1,400).astype(np.float32) # Size = (2500,400)

# Create labels
labels = np.arange(10)
# labels = array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Note: np.newasxis is used to increase the dimension of teh existing array
# by one more dimension
# 1D array will become 2D array
# 2D array will become 3D array

# Here labels is a 1D array.
# train_labels -> 2D array

train_labels = np.repeat(labels,250)[:,np.newaxis]

# test_lables is just a copy of train_lables
test_labels = train_labels.copy()


# Start the kNN
kNN = cv2.ml.KNearest_create()
# print(dir(kNN))

# Train the data
kNN.train(train, cv2.ml.ROW_SAMPLE, train_labels)

# Call the find_nearest algorithm on teh test data
# find_nearest returns the following
# result -> label given to a new comer
# neighbours -> the labels of teh k-Nearest neighbours
# dist -> corresponding distance from new-comer to each nearest neighbour


ret,result,neighbours,dist = kNN.findNearest(test,k=5)


# Check teh accuracy of teh classification
matches = result == test_labels
# print("Matches are :", matches)
# print(type(matches))
# print("The shape of the numpy array matches is ", matches.shape)
correct = np.count_nonzero(matches)

# What is teh accurracy
accuracy = correct * 100.0 / result.size

print(accuracy)
