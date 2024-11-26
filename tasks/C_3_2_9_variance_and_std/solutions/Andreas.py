import unittest
from parameterized import parameterized

def variance(lst: list) -> int | float:
    if not lst:
        raise ValueError('give not a empty list u can')

    return sum((num - (sum(lst) / len(lst))) ** 2 for num in lst) / len(lst)


def standard_deviation(variance: int | float) -> int | float:
    if not variance:
        raise ValueError('give a number above zero u have')

    return round(variance ** 0.5, 2)


class TestUnit(unittest.TestCase):

    @parameterized.expand([
        ([23, 16, 18, 17, 22, 28, 26, 22, 20, 8], 29.0),
        ([27, 22, 21, 26, 27, 35, 31, 24, 22, 15], 28.0),
        ([27], 0.0)
    ])
    def test_variance_values(self, get, expected):
        self.assertEqual(variance(get), expected)

    @parameterized.expand([
        (29.0, 5.39),
        (28.0, 5.29)
    ])
    def test_standard_devation(self, get, expected):
        self.assertEqual(standard_deviation(get), expected)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
