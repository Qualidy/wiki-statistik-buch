# implementiere ensprechende funktionen für varianz und standardabweichung
import pandas as pd
from unittest import TestCase, main
from parameterized import parameterized


def var(values):
    # 1/n * ( sum(x1 - x_)**2 + sum(x2 - x_)**2 + ... + sum(xn - x_)**2 )
    value_series = pd.Series(values)
    n = len(values)
    x_ = value_series.mean()
    return sum([(x - x_) ** 2 for x in values]) / n


def std(values: list | int | float):
    if isinstance(values, list):
        return var(values) ** 0.5
    elif isinstance(values, (int | float)):
        return values ** 0.5
    else:
        return TypeError("Values must be list, int or float")


# Unittests
class TestVarStd(TestCase):
    # Listen
    x = [23, 16, 18, 17, 22, 28, 26, 22, 20, 8]
    y = [27, 22, 21, 26, 27, 35, 31, 24, 22, 15]

    # Varianz
    @parameterized.expand([
        [x, 29.0],
        [y, 28.0],
        [[10], 0],
    ])
    def test_var(self, values, expected):
        self.assertAlmostEqual(var(values), expected, places=2)

    @parameterized.expand([
        [["1", "2", "3"], TypeError]
    ])
    def test_var_errors(self, values, expected):
        with self.assertRaises(expected):
            var(values)

    # Standardabweichung
    @parameterized.expand([
        [x, 5.39],
        [y, 5.29],
        [[10], 0],
        [25, 5],
        [0, 0]
    ])
    def test_std(self, values, expected):
        self.assertAlmostEqual(std(values), expected, places=2)

    @parameterized.expand([
        ["Test", TypeError]
    ])
    def test_std_errors(self, values, expected):
        with self.assertRaises(expected):
            std(values)


if __name__ == "__main__":
    main()