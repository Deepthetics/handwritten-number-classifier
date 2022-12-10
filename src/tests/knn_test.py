import unittest
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
        self.train_y = train_y
        self.test_y = test_y

        # Read binary (black and white) image data into 2D-arrays
        train_X = pd.read_csv('data/train_x.csv').iloc[:,1:]
        test_X = pd.read_csv('data/test_x.csv').iloc[:,1:]

        distance_function = distance_d22

    #def test_classify_one(self):
        #pass

    #def test_classify_many(self):
        #pass

    def test_error_rate_calculates_error_correctly(self):
        predicted_labels_1 = [1, 2, 3, 4]
        real_labels_1 = [1, 2, 3, 4]
        self.assertEqual(error_rate(predicted_labels_1, real_labels_1), 0)

        predicted_labels_2 = [0, 9, 1, 8, 2, 7]
        real_labels_2 = [9, 0, 8, 1, 7, 2]
        self.assertEqual(error_rate(predicted_labels_2, real_labels_2), 1)

        predicted_labels_3 = [7, 6, 5, 4, 3, 2, 1, 0]
        real_labels_3 = [7, 9, 5, 9, 3, 9, 1, 9]
        self.assertEqual(error_rate(predicted_labels_3, real_labels_3), 0.5)

    def test_classification_summary_forms_summary_string_correctly(self):
        predicted_labels = [7, 2, 1, 0, 4, 1, 4, 9, 0, 0]
        real_labels = self.test_y.iloc[0:10]

        correct_summary = 'Classified 10 images:\nPredicted labels: [7, 2, 1, 0, 4, 1, 4, 9, 0, 0]\nReal labels: [7, 2, 1, 0, 4, 1, 4, 9, 5, 9]\nError rate: 20.0%'
        self.assertEqual(classification_summary(predicted_labels, real_labels), correct_summary)
