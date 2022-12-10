import unittest
from math import sqrt
from calculation_utilities import euclidean_distance, generate_coordinates_by_distance


class Calculation_Utilities(unittest.TestCase):
    def setUp(self):
        self.coordinates_by_distance = generate_coordinates_by_distance()

    def test_euclidean_distance_calculates_correct_distance(self):
        self.assertEqual(euclidean_distance((0, 0), (1, 1)), sqrt(2))
        self.assertEqual(euclidean_distance((2, 3), (5, 4)), sqrt(10))
        self.assertEqual(euclidean_distance((11, 5), (8, 21)), sqrt(265))

    def test_generate_coordinates_by_distance_returns_dictionary_with_correct_amount_of_items(self):
        self.assertEqual(len(self.coordinates_by_distance.items()), 784)
