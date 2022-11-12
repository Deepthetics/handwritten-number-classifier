from image_data_processing import extract, to_binary
import pandas as pd
#import os


#print(os.getcwd())

train_data = pd.read_csv('data/mnist_train.csv')
test_data = pd.read_csv('data/mnist_test.csv')

train_X_grey, train_y = extract(train_data)
#print(train_X_grey)
#print(type(train_X_grey))
#print(train_y)
#print(type(train_y))
test_X_grey, test_y = extract(test_data)

train_X = to_binary(train_X_grey)
#test_X = to_binary(test_X_grey)
