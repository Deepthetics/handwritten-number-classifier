import unittest
from statistics import mode
import pandas as pd
from distance_measures import distance_d22
from image_data_processing import extract
from knn import classify_one, classify_many, error_rate, classification_summary

class TestKnn(unittest.TestCase):
    def setUp(self):
        # Read MNIST data into 2D-arrays
        train_data = pd.read_csv('data/mnist_train.csv')
        test_data = pd.read_csv('data/mnist_test.csv')

        # Extract image and label data
        train_X_grey, train_y = extract(train_data)
        test_X_grey, test_y = extract(test_data)

        # Read binary (black and white) image data into 2D-arrays
        train_X = pd.read_csv('data/train_x.csv').iloc[:,1:]
        test_X = pd.read_csv('data/test_x.csv').iloc[:,1:]

        distance_function = distance_d22

    def test_error_rate_calculates_error_correctly(self):
        pass

    def test_classification_summary_forms_summary_string_correctly(self):
        pass
