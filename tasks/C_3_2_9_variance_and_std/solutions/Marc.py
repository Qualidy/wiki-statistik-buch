import pandas as pd

daten = [2, 3, 4, 2, 1, 6, 9, 14, 25, 2, 6]


def varianz(data):
    if data:
        series = pd.Series(data)
        mean = series.mean()
        result = 0
        for i in data:
            result += (i - mean) ** 2
        return result / len(data)
    else:
        return 0


def standardabweichung(data):
    return varianz(data) ** (1 / 2)


# unittest
import unittest
from parameterized import parameterized


class Testvarianz(unittest.TestCase):
    @parameterized.expand([
        ([2, 3, 4, 2, 1, 6, 9, 14, 25, 2, 6], 46.74),
        ([], 0),
    ])
    def test_varianz(self, values, expected):
        result = round(varianz(values), 2)
        self.assertAlmostEqual(result, expected)


    @parameterized.expand([
        ([2, 3, 4, 2, 1, 6, 9, 14, 25, 2, 6], 6.84),
    ])  #
    def test_standardabweichung(self, values, expected):
        result = round(standardabweichung(values), 2)
        self.assertAlmostEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
