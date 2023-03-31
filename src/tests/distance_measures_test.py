import unittest
from math import sqrt
import numpy as np
import pandas as pd
from distance_measures import distance_d6, distance_d6_mod, distance_f2, distance_f3


class TestDistanceMeasures(unittest.TestCase):
    def setUp(self):
        self.image1 = pd.Series([0]*784)
        self.image2 = np.array([0]+[1]*27)
        for i in range(27):
            self.image2 = np.concatenate((self.image2, np.array([1]*28)))
        self.image2 = pd.Series(self.image2)
        self.image3 = np.array([1]*28)
        for i in range(26):
            self.image3 = np.concatenate((self.image3, [1]*28))
        self.image3 = np.concatenate((self.image3, [1]*27+[0]))
        self.image3 = pd.Series(self.image3)

    def test_distance_d6_calculates_distance_correctly(self):
        self.assertAlmostEqual(distance_d6(self.image1, self.image1), 0)
        self.assertAlmostEqual(distance_d6(self.image2, self.image2), 0)
        self.assertAlmostEqual(distance_d6(self.image2, self.image3), 1/1*27*sqrt(2))

    def test_distance_d6_mod_calculates_distance_correctly(self):
        self.assertAlmostEqual(distance_d6_mod(self.image1, self.image1), 0)
        self.assertAlmostEqual(distance_d6_mod(self.image2, self.image2), 0)
        self.assertAlmostEqual(distance_d6_mod(self.image2, self.image3), 1/1*27*sqrt(2))

    def test_distance_f2_calculates_distance_correctly(self):
        self.assertEqual(distance_f2(1, 1), 1)
        self.assertEqual(distance_f2(2, 2.1), 2.1)
        self.assertEqual(distance_f2(10, 5.2), 10)

    def test_distance_f3_calculates_distance_correctyle(self):
        self.assertEqual(distance_f3(1, 1), (1+1)/2)
        self.assertEqual(distance_f3(2, 2.1), (2+2.1)/2)
        self.assertEqual(distance_f3(10, 5.2), (10+5.2)/2)
