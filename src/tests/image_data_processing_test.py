import unittest
import numpy as np
import pandas as pd
import pandas.testing as pd_testing
from image_data_processing import to_array, extract, to_binary


class TestImageDataProcessing(unittest.TestCase):
    def assertSeriesEqual(self, a, b, msg):
        try:
            pd_testing.assert_series_equal(a, b)
        except AssertionError as e:
            raise self.failureException(msg) from e

    def assertDataframeEqual(self, a, b, msg):
        try:
            pd_testing.assert_frame_equal(a, b)
        except AssertionError as e:
            raise self.failureException(msg) from e

    def setUp(self):
        self.addTypeEqualityFunc(pd.Series, self.assertSeriesEqual)
        self.addTypeEqualityFunc(pd.DataFrame, self.assertDataframeEqual)

    def test_to_array_converts_data_structure_correctly(self):
        correct_array1 = np.zeros((28, 28), dtype=int)
        aux_array = np.array([[1]+[0]*27], dtype=int)
        correct_array2 = np.array([[1]+[0]*27], dtype=int)
        for i in range(27):
            correct_array2 = np.concatenate((correct_array2, aux_array))
        correct_array3 = np.eye(28, dtype=int)

        input_series1 = pd.Series([0 for i in range(784)])
        input_series2 = pd.Series([0 if i % 28 != 0 else 1 for i in range(784)])
        input_series3 = correct_array3[0, :]
        for i in range(1, 28):
            input_series3 = np.concatenate((input_series3, correct_array3[i, :]))
        input_series3 = pd.Series(input_series3)

        output_array1 = to_array(input_series1)
        output_array2 = to_array(input_series2)
        output_array3 = to_array(input_series3)

        self.assertTrue(np.array_equal(output_array1, correct_array1))
        self.assertTrue(np.array_equal(output_array2, correct_array2))
        self.assertTrue(np.array_equal(output_array3, correct_array3))

    def test_extract_extracts_data_correctly(self):
        row1 = [1, 0, 220, 0, 0, 200, 0, 0, 180, 0]
        row2 = [3, 200, 180, 180, 0, 240, 40, 160, 220, 200]
        row3 = [7, 240, 200, 0, 180, 200, 180, 0, 220, 0]
        columns = ['label', '1x1', '1x2', '1x3', '2x1', '2x2', '2x3', '3x1', '3x2', '3x3']
        df = pd.DataFrame([row1, row2, row3], columns=columns)

        images, labels = extract(df)

        row1_X = [0, 220, 0, 0, 200, 0, 0, 180, 0]
        row2_X = [200, 180, 180, 0, 240, 40, 160, 220, 200]
        row3_X = [240, 200, 0, 180, 200, 180, 0, 220, 0]
        columns_X = ['1x1', '1x2', '1x3', '2x1', '2x2', '2x3', '3x1', '3x2', '3x3']
        correct_X = pd.DataFrame([row1_X, row2_X, row3_X], columns=columns_X)
        self.assertEqual(images, correct_X)

        correct_y = pd.Series([1, 3, 7], name='label')
        self.assertEqual(labels, correct_y)

    def test_to_binary_converts_data_correctly(self):
        row1 = [0, 220, 0, 0, 200, 0, 0, 180, 0]
        row2 = [200, 180, 180, 0, 240, 40, 160, 220, 200]
        row3 = [240, 200, 0, 180, 200, 180, 0, 220, 0]
        columns = ['1x1', '1x2', '1x3', '2x1', '2x2', '2x3', '3x1', '3x2', '3x3']
        df = pd.DataFrame([row1, row2, row3], columns=columns)

        converted_df = to_binary(df)

        correct_row1 = [0, 1, 0, 0, 1, 0, 0, 1, 0]
        correct_row2 = [1, 1, 1, 0, 1, 0, 1, 1, 1]
        correct_row3 = [1, 1, 0, 1, 1, 1, 0, 1, 0]
        correct_df = pd.DataFrame([correct_row1, correct_row2, correct_row3], columns=columns)
        self.assertEqual(converted_df, correct_df)
