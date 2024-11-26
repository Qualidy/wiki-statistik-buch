import unittest
from unittest import TestCase
from parameterized import parameterized


# Varianz
def varianz(values):
    if not values:
        return 0
    artmetische_mitte = sum(values) / len(values)

    return sum([(val - artmetische_mitte) ** 2 for val in values]) / len(values)


# Standardabweichung
def standardabweichung(value):
    return value ** 0.5


class TestVarianz(TestCase):
    @parameterized.expand([
        ([23, 16, 18, 17, 22, 28, 26, 22, 20, 8], 29),
        ([27, 22, 21, 26, 27, 35, 31, 24, 22, 15], 28),
        ([], 0),
        ([2, 2, 2, 2, 2], 0),
        ([-1, -2, -3, -6], 3.5)
    ])
    def test_varianz(self, values, expected):
        self.assertEqual(varianz(values), expected)


class TestStandardabweichung(TestCase):
    @parameterized.expand([
        (4, 2),
        (9, 3),
        (16, 4),
        (0, 0),
        (1, 1),
        (2.25, 1.5),
        (100, 10),
    ])
    def test_standardabweichung(self, value, expected):
        self.assertAlmostEqual(standardabweichung(value), expected)


unittest.main(argv=[''], verbosity=2, exit=False)
