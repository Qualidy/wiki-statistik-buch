from collections.abc import Iterable
import numpy as np


def lin_reg_1D(x, y):
    if not isinstance(x, Iterable) or not isinstance(y, Iterable):
        raise ValueError("x and y must be iterable")
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")
    if len(x) < 2:
        raise ValueError("x and y must contain at least two elements")
    if not all(isinstance(x_i, int | float | np.integer | np.floating) for x_i in x):
        raise ValueError("All elements in x must be numbers")
    if not all(isinstance(y_i, int | float | np.integer | np.floating) for y_i in y):
        raise ValueError("All elements in y must be numbers")

    x_array = np.asarray(x)
    y_array = np.asarray(y)

    # Linalg calc
    n = len(y_array)
    b = (n * (x_array * y_array).sum() - x_array.sum() * y_array.sum()) / (
            n * (x_array ** 2).sum() - x_array.sum() ** 2
    )
    a = y_array.mean() - b * x_array.mean()

    return a, b


import unittest
from parameterized import parameterized


class TestDeviation(unittest.TestCase):
    @parameterized.expand([
        ([1, 2, 3], [1, 2, 3], 0, 1),  # no bias
        ([1, 2, 3], [2, 4, 6], 0, 2),  # no bias
        ([0, 1, 2], [3, 2, 1], 3, -1),  # negative
        ([0, 1, 2], [1, 2, 3], 1, 1),  # basic
        ([1, 2, 3], [3, 5, 7], 1, 2),  # basic
        ([0, 1, 2], [1, 1, 1], 1, 0),  # constant function
        ([1, 2, 3], [3, 3, 3], 3, 0),  # contant function
    ])
    def test_basic_lin_reg(self, x, y, a, b):
        self.assertAlmostEqual(lin_reg_1D(x, y), (a, b))

    @parameterized.expand([
        ([1], [1, 2]),
        ([1], [2]),
        # ([], []),
        # (1, 1 ),
    ])
    def test_erroneous_input_lin_reg(self, x, y):
        with self.assertRaises(ValueError):
            lin_reg_1D(x, y)


unittest.main(argv=[''], verbosity=2, exit=False)

# tom

import unittest
from unittest import TestCase
from parameterized import parameterized
import matplotlib.pyplot as plt


def regression(x, y):
    x_quer = sum(x) / len(x)
    y_quer = sum(y) / len(y)

    result_xi_x_quer = [(x[i] - x_quer) for i in range(len(x))]
    result_yi_y_quer = [(y[i] - y_quer) for i in range(len(y))]

    x_mal_y = [a * b for a, b in zip(result_xi_x_quer, result_yi_y_quer)]
    sum_x_mal_y = sum(x_mal_y)

    fehlerquadrat_x = sum([(x[i] - x_quer) ** 2 for i in range(len(x))])
    fehlerquadrat_y = sum([(y[i] - y_quer) ** 2 for i in range(len(y))])

    b_yx = sum_x_mal_y / fehlerquadrat_x
    a_yx = y_quer - b_yx * x_quer

    return a_yx, b_yx


class TestRegressionParameterized(unittest.TestCase):
    @parameterized.expand([

        (
                [1, 2, 3, 4],
                [2, 4, 6, 8],
                0,
                2
        ),

        (
                [1, 2, 3, 4],
                [8, 6, 4, 2],
                10,
                -2
        ),

        (
                [1, 2, 3, 4],
                [5, 5, 5, 5],
                5,
                0
        ),

        (
                [1, 2, 3, 4],
                [3, 5, 7, 10],
                0.5,
                2.3
        )
    ])
    def test_regression(self, x, y, expected_a, expected_b):
        a, b = regression(x, y)
        self.assertAlmostEqual(a, expected_a, places=2, msg=f"Achsenabschnitt falsch: {a}")
        self.assertAlmostEqual(b, expected_b, places=2, msg=f"Steigung falsch: {b}")


if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)

# Daniel:
import pandas as pd


def linReg(values):
    n = len(values)
    if isinstance(values, pd.DataFrame):
        sum_xi_yi = (values['x'] * values['y']).sum()
        sum_xi = values['x'].sum()
        sum_xi2 = (values['x'] ** 2).sum()
        sum_yi = values['y'].sum()
    else:
        sum_xi_yi = sum([x * y for x, y in values])
        sum_xi = sum([x for x, _ in values])
        sum_xi2 = sum([x ** 2 for x, _ in values])
        sum_yi = sum([y for _, y in values])

    b = (n * sum_xi_yi - sum_xi * sum_yi) / (n * sum_xi2 - (sum_xi ** 2))
    a = sum_yi / n - b * sum_xi / n

    return {'a': a, 'b': b}


def linReg_2(values):
    n = len(values)
    if isinstance(values, pd.DataFrame):
        x_mean = values['x'].mean()
        y_mean = values['y'].mean()
        sum_xi_xmean2 = sum((values['x'] - x_mean) ** 2)
        sum_xi_xmean_yi_ymean = sum((values['x'] - x_mean) * (values['y'] - y_mean))
    else:
        x_mean = sum([x for x, _ in values]) / n
        y_mean = sum([y for _, y in values]) / n

        sum_xi_xmean2 = sum([(x - x_mean) ** 2 for x, _ in values])
        sum_xi_xmean_yi_ymean = sum([(x - x_mean) * (y - y_mean) for x, y in values])

    b = sum_xi_xmean_yi_ymean / sum_xi_xmean2
    a = y_mean - b * x_mean

    return {'a': a, 'b': b}


import unittest
from parameterized import parameterized
import pandas as pd


class TestMathFunctions(unittest.TestCase):

    # Tests für linreg
    @parameterized.expand([
        ([(4, 50), (7, 80), (11, 70), (2, 45)], {'a': 41.68, 'b': 3.26}),
        ([(-2, 0), (-1, 0.5), (3, 2), (4, 2), (6, 5)], {'a': 0.835, 'b': 0.533}),
        ([(1.55, 51), (1.57, 50), (1.62, 55), (1.68, 52), (1.75, 60), (1.75, 68),
          (1.81, 78), (1.83, 91), (1.87, 84), (1.89, 81), (1.9, 90), (1.92, 105),
          (1.95, 95), (1.95, 99), (1.99, 100), (2.02, 101)], {'a': -152.168, 'b': 127.184}),
        ([(0, 0), (1, 1)], {'a': 0, 'b': 1}),
    ])
    def test_linreg(self, values, expected):
        ergebnis = linReg(values)
        self.assertAlmostEqual(ergebnis['a'], expected['a'], places=2)
        self.assertAlmostEqual(ergebnis['b'], expected['b'], places=2)

    @parameterized.expand([
        ([], ZeroDivisionError),
        ([1], TypeError),
        ([(1, 1)], ZeroDivisionError),
        ([(1, 1), (1, 1), (1, 1)], ZeroDivisionError),
    ])
    def test_linreg_exceptions(self, values, expected_exception):
        with self.assertRaises(expected_exception):
            linReg(values)

    @parameterized.expand([
        (pd.DataFrame({'x': [4, 7, 11, 2], 'y': [50, 80, 70, 45]}), {'a': 41.68, 'b': 3.26}),
        (pd.DataFrame({'x': [-2, -1, 3, 4, 6], 'y': [0, 0.5, 2, 2, 5]}), {'a': 0.835, 'b': 0.533}),
        (pd.DataFrame(
            {'x': [1.55, 1.57, 1.62, 1.68, 1.75, 1.75, 1.81, 1.83, 1.87, 1.89, 1.9, 1.92, 1.95, 1.95, 1.99, 2.02],
             'y': [51, 50, 55, 52, 60, 68, 78, 91, 84, 81, 90, 105, 95, 99, 100, 101]}), {'a': -152.168, 'b': 127.184}),
        (pd.DataFrame({'x': [0, 1], 'y': [0, 1]}), {'a': 0, 'b': 1}),
    ])
    def test_linreg_dataframe(self, values, expected):
        ergebnis = linReg(values)
        self.assertAlmostEqual(ergebnis['a'], expected['a'], places=2)
        self.assertAlmostEqual(ergebnis['b'], expected['b'], places=2)

    # Tests für linReg2
    @parameterized.expand([
        ([(4, 50), (7, 80), (11, 70), (2, 45)], {'a': 41.68, 'b': 3.26}),
        ([(-2, 0), (-1, 0.5), (3, 2), (4, 2), (6, 5)], {'a': 0.835, 'b': 0.533}),
        ([(1.55, 51), (1.57, 50), (1.62, 55), (1.68, 52), (1.75, 60), (1.75, 68),
          (1.81, 78), (1.83, 91), (1.87, 84), (1.89, 81), (1.9, 90), (1.92, 105),
          (1.95, 95), (1.95, 99), (1.99, 100), (2.02, 101)], {'a': -152.168, 'b': 127.184}),
        ([(0, 0), (1, 1)], {'a': 0, 'b': 1})
    ])
    def test_linreg_2(self, values, expected):
        ergebnis = linReg_2(values)
        self.assertAlmostEqual(ergebnis['a'], expected['a'], places=2)
        self.assertAlmostEqual(ergebnis['b'], expected['b'], places=2)

    @parameterized.expand([
        (pd.DataFrame({'x': [4, 7, 11, 2], 'y': [50, 80, 70, 45]}), {'a': 41.68, 'b': 3.26}),
        (pd.DataFrame({'x': [-2, -1, 3, 4, 6], 'y': [0, 0.5, 2, 2, 5]}), {'a': 0.835, 'b': 0.533}),
        (pd.DataFrame(
            {'x': [1.55, 1.57, 1.62, 1.68, 1.75, 1.75, 1.81, 1.83, 1.87, 1.89, 1.9, 1.92, 1.95, 1.95, 1.99, 2.02],
             'y': [51, 50, 55, 52, 60, 68, 78, 91, 84, 81, 90, 105, 95, 99, 100, 101]}), {'a': -152.168, 'b': 127.184}),
        (pd.DataFrame({'x': [0, 1], 'y': [0, 1]}), {'a': 0, 'b': 1}),
    ])
    def test_linreg2_dataframe(self, values, expected):
        ergebnis = linReg_2(values)
        self.assertAlmostEqual(ergebnis['a'], expected['a'], places=2)
        self.assertAlmostEqual(ergebnis['b'], expected['b'], places=2)

    @parameterized.expand([
        ([], ZeroDivisionError),
        ([1], TypeError),
        ([(1, 1)], ZeroDivisionError),
        ([(1, 1), (1, 1), (1, 1)], ZeroDivisionError),
    ])
    def test_linreg_2_exceptions(self, values, expected_exception):
        with self.assertRaises(expected_exception):
            print(linReg_2(values))


if __name__ == '__main__':
    unittest.main()


# Marina:

def distance_from_mean(ser):
    if ser.empty:
        return pd.Series(dtype=float)
    ser_mean = ser.mean(axis=0)
    return ser - ser_mean


def multiple_two_distances(dis_1, dis_2):
    return [x * y for x, y in zip(dis_1, dis_2)]


def calculate_a_b(x_ser, y_ser):
    if len(x_ser) != len(y_ser):
        raise ValueError("Input series must have the same length.")
    if x_ser.empty or y_ser.empty:
        raise ValueError("Input series must not be empty.")

    x_distance_from_mean, y_distance_from_mean = distance_from_mean(x_ser), distance_from_mean(y_ser)

    if sum(multiple_two_distances(x_distance_from_mean, x_distance_from_mean)) == 0:
        raise ValueError("Cannot calculate regression coefficients; x_series has no variance.")

    b = sum(multiple_two_distances(x_distance_from_mean, y_distance_from_mean)) / sum(
        multiple_two_distances(x_distance_from_mean, x_distance_from_mean))
    a = y_ser.mean(axis=0) - b * x_ser.mean(axis=0)
    return a, b


def cal_prediction_y(x_ser, y_ser, x_val):
    a, b = calculate_a_b(x_ser, y_ser)
    return b * x_val + a


def cal_prediction_x(x_ser, y_ser, y_val):
    a, b = calculate_a_b(x_ser, y_ser)
    return (y_val - a) / b


------------------------------------------------------------------------------------------------------------------------------------------
Noah
import numpy as np


def linear_regression(data):
    if not isinstance(data, list):
        raise TypeError("Input data must be a list of tuples.")
    if len([x for x, y in data]) != len([y for x, y in data]):
        raise ValueError("The number of values for x and y must be the same.")
    if len(data) < 2:
        raise ValueError("At least two data points are required for linear regression.")
    if not all(isinstance(x, (int, float)) and isinstance(y, (int, float)) for x, y in data):
        raise ValueError("All elements in the tuples must be numeric values.")

    x_vals = [x[0] for x in data]
    y_vals = [y[1] for y in data]

    if len(set(x_vals)) == 1:
        raise ValueError("All x-values are the same. Linear regression is undefined.")

    x_mean, y_mean = np.mean(x_vals), np.mean(y_vals)
    nominator = sum((xi - x_mean) * (yi - y_mean) for xi, yi in data)
    denominator = sum((xi - x_mean) ** 2 for xi in x_vals)
    byx = nominator / denominator
    ayx = y_mean - byx * x_mean

    return ayx, byx


def calculate_y(data, value):
    ayx, byx = linear_regression(data)
    return ayx + byx * value


import unittest
from parameterized import parameterized


class TestLinearRegression(unittest.TestCase):

    @parameterized.expand([
        [[(4, 50), (7, 80), (11, 70), (2, 45)], (41.68, 3.26)],
        [[(1, 2), (2, 4), (3, 6), (4, 8)], (0, 2)],
        [[(10, 20), (20, 40)], (0, 2)],

        [[], None],
        [[(1, 2)], None],
        [[(1, 2), (1, 3)], None],
        [[("a", 2), (3, 4)], None]
    ])
    def test_linear_regression(self, data, expected):
        if expected is None:
            with self.assertRaises(Exception):
                linear_regression(data)
        else:
            ayx, byx = linear_regression(data)
            self.assertAlmostEqual(ayx, expected[0], delta=0.01)
            self.assertAlmostEqual(byx, expected[1], delta=0.01)


class TestCalculateY(unittest.TestCase):

    @parameterized.expand([
        [[(1, 2), (2, 4)], 3, 6.0],
        [[(10, 20), (20, 40)], 15, 30.0],
        [[(1, 2), (2, 4), (3, 6), (4, 8), (5, 10)], 6, 12.0],
        [[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], 10, 10.0],

        # Grenzwerte
        [[(1, 1), (2, 3)], 1.5, 2.0],
        [[(1, 1), (2, 2), (3, 3)], -1, -1.0],  # Negativer x-Wert
        [[(1, 1), (2, 2), (3, 3)], 0, 0.0],  # x-Wert im Bereich der Extrapolation
    ])
    def test_calculate_y(self, test_list, value, expected):
        self.assertAlmostEqual(calculate_y(test_list, value), expected, delta=0.01)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)

------------------------------------------------------------------------------------------------------------------------------------------

Marc
import numpy as np

daten = [(0.5, 65, 2), (1.7, 42.7), (3.2, 39.4), (4.7, 19.6), (6.3, 12.4)]
daten2 = [(1.55, 51), (1.57, 50), (1.62, 55), (1.68, 52), (1.75, 60), (1.75, 68), (1.81, 78), (1.83, 91), (1.87, 84),
          (1.89, 81), (1.9, 90), (1.92, 105), (1.95, 95), (1.95, 99), (1.99, 100), (2.02, 101)]


# 1. Wert im tuple = x     2. wert = y
def my_linreg(data: list):
    if data:
        n = len(data)
        xsum = 0
        ysum = 0
        xsumsqr = 0
        xysum = 0
        for i in range(len(data)):
            xsum += data[i][0]
            ysum += data[i][1]
            xsumsqr += (data[i][0]) ** 2
            xysum += (data[i][0] * data[i][1])
        b = (n * (xysum) - (xsum * ysum)) / (n * xsumsqr - xsum ** 2)
        a = (ysum - b * xsum) / n
    else:
        return "Keine leere liste eingeben"
    return a, b
    # unittest


import unittest
from parameterized import parameterized

import unittest
from parameterized import parameterized


class Testlinreg(unittest.TestCase):
    @parameterized.expand([
        ([(0.5, 65, 2), (1.7, 42.7), (3.2, 39.4), (4.7, 19.6), (6.3, 12.4)], (64.38, -8.72)),
        ([(4, 50), (7, 80), (11, 70), (2, 45)], (41.69, 3.26)),
        ([(-2, 0), (-1, 0.5), (3, 2), (4, 2), (6, 5)], (0.835, 0.533)),
        ([(1.55, 51), (1.57, 50), (1.62, 55), (1.68, 52), (1.75, 60), (1.75, 68), (1.81, 78), (1.83, 91), (1.87, 84),
          (1.89, 81), (1.9, 90), (1.92, 105), (1.95, 95), (1.95, 99), (1.99, 100), (2.02, 101)], (-152.16, 127.18))
    ])
    def test_linreg(self, values, expected):
        a, b = my_linreg(values)
        self.assertAlmostEqual(a, expected[0], delta=0.02)
        self.assertAlmostEqual(b, expected[1], delta=0.02)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)

-------------------------------------------------------------------------------------------

nick


def reg(data):
    if not data:
        raise ValueError("Bitte keine leere Liste übergeben")
    data_x = [x[0] for x in data]
    data_y = [y[1] for y in data]
    data_x_mean = np.mean(data_x)
    data_y_mean = np.mean(data_y)
    sum_numerator = sum((x - data_x_mean) * (y - data_y_mean) for x, y in data)
    sum_denominator = sum((x - data_x_mean) ** 2 for x in data_x)
    b = sum_numerator / sum_denominator
    a = data_y_mean - b * data_x_mean

    return a, b


class TestReg(unittest.TestCase):
    def test_empty(self):
        with self.assertRaises(ValueError):
            reg([])

    @parameterized.expand([
        ([(4, 50), (7, 80), (11, 70), (2, 45)], (41.69, 3.26)),
        ([(1, 2), (2, 4), (3, 6), (4, 8)], (0, 2)),
        ([(1, 10), (2, 8), (3, 6), (4, 4)], (12, -2)),
        ([(1, 2), (3, 6)], (0, 2)),

    ])
    def test_parametrized(self, values, expected):
        a, b = reg(values)
        self.assertAlmostEqual(a, expected[0], delta=0.01)
        self.assertAlmostEqual(b, expected[1], delta=0.01)


if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)

-----------------------------------------------------------------------------------------
Fabian

from _collections_abc import Iterable


def linear_regression(data: list[tuple] | pd.DataFrame = None, x: Iterable = None, y: Iterable = None):
    if isinstance(data, list) and all(isinstance(el, tuple) for el in data) and all((len(tup) == 2) for tup in data):
        x_data, y_data = [x for x, _ in data], [y for _, y in data]
    elif isinstance(data, pd.DataFrame):
        x_data, y_data = data.iloc[:, 0], data.iloc[:, 1]
    elif x and y and not data:
        x_data = x
        y_data = y
    else:
        raise ValueError(f"Can only handle <class 'list[tuple]'>, <class 'pd.Dataframe'> or seperate lists for x and y")

    if not (all(isinstance(el, int | float) for el in x_data) and all(isinstance(el, int | float) for el in y_data)):
        raise ValueError("Can only handle int or float values")

    x_mean = np.mean(x_data)
    y_mean = np.mean(y_data)
    sum_x_minus_x_mean_square = np.sum([(x - x_mean) ** 2 for x in x_data])
    x_y_mult = np.sum([(x - x_mean) * (y - y_mean) for x, y in zip(x_data, y_data)])
    b = x_y_mult / sum_x_minus_x_mean_square
    a = y_mean - b * x_mean
    return a, b


from unittest import TestCase, main
from parameterized import parameterized


class TestForLinearRegression(TestCase):

    @parameterized.expand([
        ([(4, 50), (7, 80), (11, 70), (2, 45)], (41.68, 3.26)),
        ([(-2, 0), (-1, 0.5), (3, 2), (4, 2), (6, 5)], (0.83, 0.53))
    ])
    def test_tuple(self, values, expected):
        result = linear_regression(data=values)
        for res, exp in zip(result, expected):
            self.assertAlmostEqual(res, exp, places=2)

    @parameterized.expand([
        (pd.DataFrame({'Alter': [4, 7, 11, 2], 'Bremsweg': [50, 80, 70, 45]}), (41.68, 3.26)),
        (pd.DataFrame({'x': [-2, -1, 3, 4, 6], 'y': [0, 0.5, 2, 2, 5]}), (0.83, 0.53))
    ])
    def test_dataframe(self, values, expected):
        result = linear_regression(data=values)
        for res, exp in zip(result, expected):
            self.assertAlmostEqual(res, exp, places=2)

    @parameterized.expand([
        ([4, 7, 11, 2], [50, 80, 70, 45], (41.68, 3.26)),
        ([-2, -1, 3, 4, 6], [0, 0.5, 2, 2, 5], (0.83, 0.53))
    ])
    def test_seperate_list_for_x_and_y(self, x, y, expected):
        result = linear_regression(x=x, y=y)
        for res, exp in zip(result, expected):
            self.assertAlmostEqual(res, exp, places=2)

    @parameterized.expand([
        ([0, 1, 2, 3], "Can only handle <class 'list[tuple]'>, <class 'pd.Dataframe'> or seperate lists for x and y"),
        (dict(), "Can only handle <class 'list[tuple]'>, <class 'pd.Dataframe'> or seperate lists for x and y"),
        (10, "Can only handle <class 'list[tuple]'>, <class 'pd.Dataframe'> or seperate lists for x and y"),
        (set(), "Can only handle <class 'list[tuple]'>, <class 'pd.Dataframe'> or seperate lists for x and y"),
        ([(4, 50, 10), (7, 80, 10), (11, 70, 20), (2, 45, 40)],
         "Can only handle <class 'list[tuple]'>, <class 'pd.Dataframe'> or seperate lists for x and y")
    ])
    def test_wrong_dtype(self, values, expected):
        with self.assertRaises(ValueError) as context:
            linear_regression(values)
        self.assertEqual(str(context.exception), expected)

    @parameterized.expand([
        (pd.DataFrame({'Alter': ['String', 'String', 'String', 2], 'Bremsweg': [50, 80, 'String', 45]}),
         "Can only handle int or float values"),
        (pd.DataFrame({'Alter': [None], 'Bremsweg': [None]}), "Can only handle int or float values"),
        ([(None, None), (7, 80), (11, 70), (2, 45)], "Can only handle int or float values"),
        ([('String', 50), (7, 80), (11, 70), (2, 45)], "Can only handle int or float values")
    ])
    def test_wrong_values_in_correct_dtype(self, values, expected):
        with self.assertRaises(ValueError) as context:
            linear_regression(values)
        self.assertEqual(str(context.exception), expected)


main(argv=[''], verbosity=2, exit=False)

-----------------------------------------------------------------------------------------

waldemar

import pandas as pd
from unittest import TestCase, main
from parameterized import parameterized
from collections.abc import Iterable

vehicle_list = [(4, 50), (7, 80), (11, 70), (2, 45)]

df_veh = pd.DataFrame(vehicle_list)


def calc_a_b(iterable):
    if isinstance(iterable, pd.DataFrame):
        if iterable.shape[1] < 2:
            raise ValueError("dataframe must have at least two columns")
        iterable = list(iterable.itertuples(index=False, name=None))

    if not isinstance(iterable, Iterable):
        raise ValueError("parameter must be iterable")
    elif len(iterable) == 0:
        raise ValueError("iterable is empty")

    x_list = [iterable[i][0] for i in range(len(iterable))]
    x_cross = sum(x_list) / len(x_list)

    y_list = [iterable[i][1] for i in range(len(iterable))]
    y_cross = sum(y_list) / len(y_list)

    x_minus_x_cross = [(x_list[i] - x_cross) for i in range(len(x_list))]
    sum_x_minus_x_cross_square = sum([x_minus_x_cross[i] ** 2 for i in range(len(x_minus_x_cross))])

    y_minus_y_cross = [(y_list[i] - y_cross) for i in range(len(y_list))]

    x_y_cross_minus = [(x_minus_x_cross[i] * y_minus_y_cross[i]) for i in range(len(x_minus_x_cross))]
    sum_xy_cross = sum(x_y_cross_minus)

    if sum_x_minus_x_cross_square == 0:
        raise ZeroDivisionError("zero division error")

    b_yx = sum_xy_cross / sum_x_minus_x_cross_square

    a_yx = y_cross - b_yx * x_cross

    return b_yx, a_yx


def calc_breaking_distance(values, vehicle_age):
    result = calc_a_b(values)
    y = result[0] * vehicle_age + result[1]
    return y


class TestClassAB(TestCase):

    @parameterized.expand([
        ([(4, 50), (7, 80), (11, 70), (2, 45)], (3.260869565217391, 41.684782608695656)),
        (pd.DataFrame([(1, 4), (4, 3)]), (-0.3333333333333333, 4.333333333333333))
    ])
    def test_case_1(self, values, expcted):
        result = calc_a_b(values)
        self.assertAlmostEqual(result[0], expcted[0], places=6)
        self.assertAlmostEqual(result[1], expcted[1], places=6)

    @parameterized.expand([
        (1234,),
        (None),
    ])
    def test_not_iterable(self, invalid_input):
        with self.assertRaises(ValueError):
            calc_a_b(invalid_input)


if __name__ == "__main__":
    main()

------------------------------------------------------------------------------------------------------------------------------------------------------------------
Johannes

import unittest


def arithmetische_mittel(values: list):
    return sum(values) / len(values)


def steigung(x, y):
    x_mean = arithmetische_mittel(x)
    y_mean = arithmetische_mittel(y)
    return sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(len(x))) / sum(
        (x[i] - x_mean) ** 2 for i in range(len(x)))


def y_achsenabschnitt(x, y):
    return arithmetische_mittel(y) - steigung(x, y) * arithmetische_mittel(x)


class Test(unittest.TestCase):
    def test_steigung_1(self):
        data = {"Alter (Jahre)": [4, 7, 11, 2],
                "Bremsweg (m)": [50, 80, 70, 45]
                }
        given = steigung(data['Alter (Jahre)'], data['Bremsweg (m)'])
        expected = 3.26
        self.assertAlmostEqual(given, expected, places=2)

    def test_steigung_2(self):
        data = {"Alter (Jahre)": [-2, -1, 3, 4, 6],
                "Bremsweg (m)": [0, 0.5, 2, 2, 5]
                }
        given = steigung(data['Alter (Jahre)'], data['Bremsweg (m)'])
        expected = 0.533
        self.assertAlmostEqual(given, expected, places=3)

    def test_y_achsenabschnitt_1(self):
        data = {"Alter (Jahre)": [4, 7, 11, 2],
                "Bremsweg (m)": [50, 80, 70, 45]
                }
        given = y_achsenabschnitt(data['Alter (Jahre)'], data['Bremsweg (m)'])
        expected = 41.69
        self.assertAlmostEqual(given, expected, places=1)

    def test_y_achsenabschnitt_2(self):
        data = {"Alter (Jahre)": [-2, -1, 3, 4, 6],
                "Bremsweg (m)": [0, 0.5, 2, 2, 5]
                }
        given = y_achsenabschnitt(data['Alter (Jahre)'], data['Bremsweg (m)'])
        expected = 0.835
        self.assertAlmostEqual(given, expected, places=3)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)

------------------------------------------------------------------------------------------------

christoph


def preprocess_values(values)
    ...


def x_sum(values):
    return sum(xi for xi, yi in values)


def y_sum(values):
    return sum(yi for xi, yi in values)


def xy_sum(values):
    return sum(xi * yi for xi, yi in values)


def x_square_sum(values):
    return sum(xi ** 2 for xi, yi in values)


def n(values):
    return len(values)


def lin_reg(values):
    x_sum = x_sum(values)
    y_sum = y_sum(values)
    xy_sum = xy_sum(values)
    x_square_sum = x_square_sum(values)
    n = n(values)

    m = (xy_sum - (x_sum * y_sum / n)) / (x_square_sum - (x_sum * x_sum / n))
    b = (y_sum / n) - (m * x_sum / n)

    return m, b


import unittest
from unittest import TestCase
from parameterized import parameterized


class Lin_Reg_Test(TestCase):
    @parameterized.expand([
        [[(0.5, 65.2), (1.7, 42.7), (3.2, 39.4), (4.7, 16.9), (6.3, 12.4)], (-8.911830774990637, 64.55080494196929)],
        [[(4, 50), (7, 80), (11, 70), (2, 45)], (3.260869565217391, 41.684782608695656)]
    ])
    def test_normal_values(self, values, expected):
        self.assertAlmostEqual(lin_reg(values), expected, places=3)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
-----------------------------------------------------------------------------------------

Tobias


def regression_ab(x, y):
    if len(x) == 1:
        return y[0], 0
    x, y = pd.Series(x), pd.Series(y)
    print(x, y)
    x_mean = x.mean()
    y_mean = y.mean()
    sum_xi = x.sum()
    sum_yi = y.sum()
    sum_xiyi = (x * y).sum()
    sum_xi2 = (x ** 2).sum()
    n = len(x)
    print(n, x_mean, y_mean, sum_xi, sum_yi, sum_xiyi, sum_xi2)
    b = (n * sum_xiyi - sum_xi * sum_yi) / (n * sum_xi2 - sum_xi ** 2)
    a = y_mean - x_mean * b
    return a, b


class RegressionABTest(TestCase):

    @parameterized.expand([
        [pd.Series([0.5, 1.7, 3.2, 4.7, 6.3]), pd.Series([65.2, 42.7, 39.4, 19.6, 12.4]), 64.5, -8.73],
        [pd.Series([4, 7, 11, 2]), pd.Series([50, 80, 70, 45]), 41.69, 3.26],
        [pd.Series([-2, -1, 3, 4, 6]), pd.Series([0, 0.5, 2, 2, 5]), 0.83, 0.53],
        [pd.Series([1.55, 1.57, 1.62, 1.68, 1.75, 1.75, 1.81, 1.83, 1.87, 1.89, 1.9, 1.92, 1.95, 1.95, 1.99, 2.02]),
         pd.Series([51, 50, 55, 52, 60, 68, 78, 91, 84, 81, 90, 105, 95, 99, 100, 101]), -152.17, 127.18],
        [[0.5, 1.7, 3.2, 4.7, 6.3], [65.2, 42.7, 39.4, 19.6, 12.4], 64.5, -8.73],
        [[1], [2], 2, 0],
    ])
    def test_regression_ab(self, x, y, a_expected, b_expected):
        a, b = regression_ab(x, y)
        self.assertAlmostEqual(a, a_expected, delta=0.01)
        self.assertAlmostEqual(b, b_expected, delta=0.01)


DAVEWAVE
's super simple solution:


def linear_regression(df: pd.DataFrame, x: str, y: str) -> dict:
    # a + b*x
    mean_x = df[x].mean()
    mean_y = df[y].mean()
    covariance = ((df[x] - mean_x) * (df[y] - mean_y)).mean()  # s_xy
    variance_x = df[x].var(ddof=0)  # s^2_x

    b = covariance / variance_x
    a = mean_y - b * mean_x
    return {'a': float(a), 'b': float(b)}


____________________________________________________________________________
Kevin


def get_a_and_b_for_regression(data_a: list[int | float], data_b: list[int | float]) -> tuple[float, float]:
    import pandas as pd

    data = pd.DataFrame({
        'X': data_a,
        'Y': data_b
    })

    data['Xi - X_'] = [xi - data['X'].mean() for xi in data['X']]
    data['Yi - Y_'] = [yi - data['Y'].mean() for yi in data['Y']]
    data['(Xi - X_) * (Yi - Y_)'] = data['Xi - X_'] * data['Yi - Y_']
    data['(Xi - X_)**2'] = data['Xi - X_'] ** 2
    data['(Yi - Y_)**2'] = data['Yi - Y_'] ** 2

    b_yx = sum(data['(Xi - X_) * (Yi - Y_)']) / sum(data['(Xi - X_)**2'])
    a_yx = data['Y'].mean() - b_yx * data['X'].mean()

    # print(data)
    return float(a_yx), float(b_yx)


import unittest


class TestGetAAndBForRegression(unittest.TestCase):

    def test_simple_linear_data(self):
        """Testet a und b für lineare Daten mit einer positiven Steigung."""
        data_a = [1, 2, 3, 4, 5]
        data_b = [2, 4, 6, 8, 10]
        a, b = get_a_and_b_for_regression(data_a, data_b)
        self.assertAlmostEqual(a, 0.0, places=5)
        self.assertAlmostEqual(b, 2.0, places=5)

    def test_negative_slope(self):
        """Testet a und b für lineare Daten mit einer negativen Steigung."""
        data_a = [1, 2, 3, 4, 5]
        data_b = [10, 8, 6, 4, 2]
        a, b = get_a_and_b_for_regression(data_a, data_b)
        self.assertAlmostEqual(a, 12.0, places=5)
        self.assertAlmostEqual(b, -2.0, places=5)

    def test_floating_point_values(self):
        """Testet a und b für nicht-ganzzahlige Werte."""
        data_a = [1.0, 2.5, 3.5, 4.0, 5.0]
        data_b = [1.5, 3.0, 4.5, 6.0, 7.5]
        a, b = get_a_and_b_for_regression(data_a, data_b)
        self.assertAlmostEqual(a, -0.40323, places=5)
        self.assertAlmostEqual(b, 1.53226, places=5)


unittest.main(argv=[''], verbosity=2, exit=False)

_______________________________________________________________________________________

Elias:


def erstelle_tupel(liste1, liste2):
    if len(liste1) != len(liste2):
        raise ValueError("Die Listen müssen die gleiche Länge haben.")
    return list(zip(liste1, liste2))


def mittelwert(liste):
    return sum(liste) / len(liste)


def diff_mw(liste):
    mw = mittelwert(liste)
    return [i - mw for i in liste]


def produkt_aus_diff(liste1, liste2):
    diff1 = diff_mw(liste1)
    diff2 = diff_mw(liste2)
    return [d1 * d2 for d1, d2 in zip(diff1, diff2)]


def quadratsumme(liste):
    diff = diff_mw(liste)
    return sum([d ** 2 for d in diff])


def regression(liste_x, liste_y):
    x_mittel = mittelwert(liste_x)
    y_mittel = mittelwert(liste_y)

    # Steigung
    summe_diff_prod = sum(produkt_aus_diff(liste_x, liste_y))
    summe_diff_quad = quadratsumme(liste_x)
    m = summe_diff_prod / summe_diff_quad

    # Achsenabschnitt
    b = y_mittel - m * x_mittel

    return m, b


alter = [4, 7, 11, 2]
bremsweg = [50, 80, 70, 45]

m, b = regression(alter, bremsweg)
print(f"Formel (a+b * x) /n Steigung (a): {m}, Achsenabschnitt (b): {b}")


def berechnen_neuer_wert(liste1, liste2, x):
    m, b = regression(liste1, liste2)
    return m * x + b


berechnen_neuer_wert(alter, bremsweg, 15)

Andreas

age = [4, 7, 11, 2]
breaking_distance = [50, 80, 70, 45]


def regression(lst_01, lst_02):
    df = pd.DataFrame({
        'age': age,
        'breaking_distance': breaking_distance
    })

    arithmetic_mean_x = sum(df['age']) / len(df['age'])
    arithmetic_mean_y = sum(df['breaking_distance']) / len(df['breaking_distance'])

    df['x_i-x'] = df['age'] - arithmetic_mean_x

    df['y_i-y'] = df['breaking_distance'] - arithmetic_mean_y

    df['(x_i-x)*(y_i-y)'] = df['x_i-x'] * df['y_i-y']

    df['(x_i-x)**2'] = df['x_i-x'] ** 2

    df['(y_i-y)**2'] = df['y_i-y'] ** 2

    df.loc['sum'] = df.sum()

    b_yx = df['(x_i-x)*(y_i-y)'].iloc[-1] / df['(x_i-x)**2'].iloc[-1]

    a_yx = arithmetic_mean_y - b_yx * arithmetic_mean_x

    return a_yx, b_yx


regression(age, breaking_distance)


