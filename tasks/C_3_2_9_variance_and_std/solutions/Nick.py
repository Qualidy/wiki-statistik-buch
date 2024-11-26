import pandas as pd
from parameterized import parameterized
import unittest
import numpy as np


def varianz(data):
    if len(data) == 0:
        raise ValueError("Bitte keine leere Liste übergeben")

    data = pd.Series(data)
    return sum([(number - data.mean()) ** 2 for number in data]) / len(data)


class Test_Varianz(unittest.TestCase):
    def test_empty(self):
        with self.assertRaises(ValueError):
            varianz([])

    @parameterized.expand([
        ([1, 2, 3, 4, -5, -7], 17.22),
        ([1, 1, 1, 1], 0),
        ([-1, -2, -1, -1, -2, -2], 0.25),
        ([100, 2000, 333, 7], 658134.5),
        ([1.2, 5.5, 7.7], 7.29)])
    def test_parametrized(self, values, expected):
        self.assertAlmostEqual(varianz(values), expected, places=2)


def standardabweichung(data):
    return np.sqrt(varianz(data))


class Test_stdabw(unittest.TestCase):
    def test_empty(self):
        with self.assertRaises(ValueError):
            standardabweichung([])

    @parameterized.expand([
        ([1, 2, 3, 4, -5, -7], 4.15),
        ([1, 1, 1, 1], 0),
        ([-1, -2, -1, -1, -2, -2], 0.5),
        ([100, 2000, 333, 7], 811.25),
        ([1.2, 5.5, 7.7], 2.7)])
    def test_parametrized(self, values, expected):
        self.assertAlmostEqual(standardabweichung(values), expected, places=2)


if __name__ == "__main__":
    unittest.main()
