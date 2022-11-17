import time
import pandas as pd
from image_data_processing import extract, to_binary
#import os


#print(os.getcwd())

train_data = pd.read_csv('data/mnist_train.csv')
test_data = pd.read_csv('data/mnist_test.csv')

train_X_grey, train_y = extract(train_data)
test_X_grey, test_y = extract(test_data)

train_X = to_binary(train_X_grey)
test_X = to_binary(test_X_grey)
train_X.to_csv('train_x.csv')
test_X.to_csv('test_x.csv')
