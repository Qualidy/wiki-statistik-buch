import pandas as pd


def var_finder(data):
    if not data:
        return None
    if type(data) == list:
        data_mean = pd.Series(data).mean()
    else:
        data_mean = data.mean()

    var = sum([(element - data_mean) ** 2 for element in data]) / len(data)
    return var


import unittest
from unittest import TestCase
from parameterized import parameterized


class Var_Finder_Test(TestCase):
    ser = pd.Series([23, 16, 18, 17, 22, 28, 26, 22, 20, 8])

    @parameterized.expand([
        [[23, 16, 18, 17, 22, 28, 26, 22, 20, 8], 29],
        [[27, 22, 21, 26, 27, 35, 31, 24, 22, 15], 28],
        [[10, 10, 10, 10], 0],
        [[], None],
        [ser, 29]
    ])
    def test_normal_values(self, data, expected):
        self.assertEqual(var_finder(data), expected)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)

def std_dev_finder(data):
    if not data:
        return None
    return var_finder(data) ** 0.5


import unittest
from unittest import TestCase
from parameterized import parameterized


class Std_Dev_Finder_Test(TestCase):
    @parameterized.expand([
        [[23, 16, 18, 17, 22, 28, 26, 22, 20, 8], 5.39],
        [[27, 22, 21, 26, 27, 35, 31, 24, 22, 15], 5.29],
        [[10, 10, 10, 10], 0],
        [[], None],
    ])
    def test_normal_values(self, data, expected):
        self.assertAlmostEqual(std_dev_finder(data), expected, places=2)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
