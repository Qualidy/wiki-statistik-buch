import unittest
from parameterized import parameterized

def variance(lst: list) -> int | float:
    if not lst:
        raise ValueError('give not a empty list u can')

    mean = (sum(lst) / len(lst))
    return sum((num - mean) ** 2 for num in lst) / len(lst)


def standard_deviation(lst: list) -> int | float:
    return variance(lst) ** 0.5


class TestUnit(unittest.TestCase):

    @parameterized.expand([
        ([23, 16, 18, 17, 22, 28, 26, 22, 20, 8], 29.0),
        ([27, 22, 21, 26, 27, 35, 31, 24, 22, 15], 28.0),
        ([27], 0.0),
        ([27, 27, 27], 0.0),
    ])
    def test_variance_values(self, get, expected):
        self.assertAlmostEqual(variance(get), expected, places=2)

    @parameterized.expand([
        ([23, 16, 18, 17, 22, 28, 26, 22, 20, 8], 5.39),
        ([27, 22, 21, 26, 27, 35, 31, 24, 22, 15], 5.29),
        ([27], 0.0),
        ([27, 27, 27], 0.0),
    ])
    def test_standard_devation(self, get, expected):
        self.assertAlmostEqual(standard_deviation(get), expected, places=2)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
