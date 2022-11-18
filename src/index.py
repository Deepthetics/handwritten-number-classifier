#import numpy as np
import pandas as pd
#from distance_measures import distance_d22, distance_d23, distance_d23_mod
from image_data_processing import extract, to_binary
from image_plotting import plot_image_data

# Read MNIST data into 2D-arrays
train_data = pd.read_csv('data/mnist_train.csv')
test_data = pd.read_csv('data/mnist_test.csv')

# Extract image and label data
train_X_grey, train_y = extract(train_data)
test_X_grey, test_y = extract(test_data)

# Convert greyscale image data to binary (black and white) image data
#train_X = to_binary(train_X_grey)
#test_X = to_binary(test_X_grey)

# Store converted data in ./data as 'train_x.csv' and 'test_x.csv'
#train_X.to_csv('train_x.csv')
#test_X.to_csv('test_x.csv')

# Read binary (black and white) image data into 2D-arrays
train_X = pd.read_csv('data/train_x.csv').iloc[:,1:]
test_X = pd.read_csv('data/test_x.csv').iloc[:,1:]

#Plot corresponding greyscale and black and white images side by side
plot_image_data(train_X_grey.iloc[0], train_X.iloc[0])
