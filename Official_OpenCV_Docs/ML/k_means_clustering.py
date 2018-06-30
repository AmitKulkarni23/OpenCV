# Python file that demonstrates k-means-clustering for only 1 feature

# API Used -> cv2.kmeans()
# Paramters:
# 1.samples : It should be of np.float32 data type,
# and each feature should be put in a single column.
#
# 2.nclusters(K) : Number of clusters required at end
#
# 2.criteria : It is the iteration termination criteria. When this criteria is satisfied,
# algorithm iteration stops. Actually, it should be a tuple of 3 parameters.
#
# They are ( type, max_iter, epsilon ):
#
# 3.a - type of termination criteria : It has 3 flags as below:
# cv2.TERM_CRITERIA_EPS - stop the algorithm iteration if specified accuracy, epsilon, is reached.
# cv2.TERM_CRITERIA_MAX_ITER - stop the algorithm after the specified number of iterations, max_iter.
# cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER - stop the iteration when any of the above condition is met.
#
# 3.b - max_iter - An integer specifying maximum number of iterations.
#
# 3.c - epsilon - Required accuracy
#
# attempts : Flag to specify the number of times the algorithm is
# executed using different initial labellings.
# The algorithm returns the labels that yield the best compactness.
# This compactness is returned as output.
#
# flags : This flag is used to specify how initial centers are taken.
# Normally two flags are used for this : cv2.KMEANS_PP_CENTERS and cv2.KMEANS_RANDOM_CENTERS.

# Credits -> https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_ml/py_kmeans/py_kmeans_opencv/py_kmeans_opencv.html


##############################################################################

# Data with only feature

# Consider teh T-Shirt problem with only teh height feature

# Preapare teh data first
import numpy as np
import cv2
from matplotlib import pyplot as plt

# high = 100, low = 25
x = np.random.randint(25,100,25)

# low = 175. high = 175
y = np.random.randint(175,255,25)

# np.hstack - Stack arrays horizontally i.e column wise
z = np.hstack((x,y))

# np.reshape -> Give a new shape to an array without changing its data elements
z = z.reshape((50,1))

# Change all data to np.float32 type
z = np.float32(z)


# Define criteria = ( type, max_iter = 10 , epsilon = 1.0 )
max_iter = 10
epislon = 1.0
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, max_iter, epislon)

# Set flags (Just to avoid line break in the code)
flags = cv2.KMEANS_RANDOM_CENTERS

# Apply KMeans
num_of_clusters = 2
attempts = 10
compactness,labels,centers = cv2.kmeans(z,num_of_clusters,None,criteria,attempts,flags)

# Cneters = (60, 211)
# Split teh data into different clusters depending on their labels
A = z[labels==0]
B = z[labels==1]

# Plot A in red color and B in blue color and centroids in yelow color
plt.hist(A,256,[0,256],color = 'r')
plt.hist(B,256,[0,256],color = 'b')
plt.hist(centers,32,[0,256],color = 'y')
plt.show()
