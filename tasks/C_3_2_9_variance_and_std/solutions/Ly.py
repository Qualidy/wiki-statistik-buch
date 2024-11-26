from collections.abc import Iterable
import numpy as np


def calc_variance(values):
    if not values:
        return np.nan
    if not (isinstance(values, Iterable) and all(isinstance(elem, int | float) for elem in values)):
        # if not isinstance(values, int | float) or not (isinstance(values, Iterable) and  all(isinstance(elem, int | float) for elem in values)):
        raise ValueError("Input is invalid")
    mean = np.mean(values)
    return np.mean([(x - mean) ** 2 for x in values])


def calc_std_deviatioin(values):
    return calc_variance(values) ** 0.5


import unittest
from parameterized import parameterized


class TestDeviation(unittest.TestCase):
    @parameterized.expand([
        ([],),
        (None,),
        (set(),),
    ])
    def test_bad_input_variance(self, values):
        self.assertTrue(np.isnan(calc_variance(values)))

    # @parameterized.expand([
    #     (1, 0),
    #     (-1, 0)
    # ])
    # def test_special_input_variance(self, values, expected):
    #     result = calc_variance(values)
    #     self.assertEqual(result, expected)

    @parameterized.expand([
        (object(),),
        ("hello",),
    ])
    def test_erroneous_input_variance(self, values):
        with self.assertRaises(ValueError):
            calc_variance(values)

    @parameterized.expand([
        ([1], 0),
        ([1, 1], 0),
        ([-1, -1], 0),
        ([-1, 1], 1.0),
        ([3, 1, 2, 4, 5], 2.0),
    ])
    def test_simple_variance(self, values, expected):
        self.assertAlmostEqual(calc_variance(values), expected)


unittest.main(argv=[''], verbosity=2, exit=False)
