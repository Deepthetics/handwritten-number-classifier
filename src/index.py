import pandas
#import os

#print(os.getcwd())

train_data = pandas.read_csv('data/mnist_train.csv')
print(train_data)
print()

test_data = pandas.read_csv('data/mnist_test.csv')
print(test_data)
print()
