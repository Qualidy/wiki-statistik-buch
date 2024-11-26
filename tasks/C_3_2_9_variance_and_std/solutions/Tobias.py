from unittest import TestCase
from parameterized import parameterized
import numpy as np
import math


def varianz(data):
    if not isinstance(data, list):
        raise ValueError("Data has to be a list")
    if not data:
        return np.nan
    mean = arith_mean(data)
    return sum((d - mean) ** 2 for d in data) / len(data)


def standardabweichung(data):
    if not isinstance(data, list):
        raise ValueError("Data has to be a list")
    if not data:
        return np.nan
    return math.sqrt(varianz(data))


class VarianzTest(TestCase):
    @parameterized.expand([
        [[1, 2, 3, 4, 5], 2],
        [[1], 0],
        [[10, -10, 20, 45, 33, 123, 150], 3097.14],
        [[2, 2, 2, 2, 2, 2, 2, 2, 2], 0],
    ])
    def test_varianz(self, data, expected):
        self.assertEqual(round(varianz(data), 2), expected)

    def test_varianz_error(self):
        with self.assertRaises(ValueError):
            varianz("string")

    def test_varianz_empty(self):
        self.assertTrue(np.isnan(varianz([])))


class StandardabweichungTest(TestCase):
    @parameterized.expand([
        [[1, 2, 3, 4, 5], round(math.sqrt(2), 2)],
        [[1], 0],
        [[10, -10, 20, 45, 33, 123, 150], round(math.sqrt(3097.14), 2)],
        [[2, 2, 2, 2, 2, 2, 2, 2, 2], 0],
    ])
    def test_std(self, data, expected):
        self.assertEqual(round(standardabweichung(data), 2), expected)

    def test_std_error(self):
        with self.assertRaises(ValueError):
            varianz(23)

    def test_std_empty(self):
        self.assertTrue(np.isnan(standardabweichung([])))
        