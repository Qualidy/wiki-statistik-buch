import numpy as np
from unittest import TestCase, main
from parameterized import parameterized

def regression(x, y):
    ones_x = np.vstack((
        np.ones(len(x)),  # Erste Zeile: Einsen
        x  # Zweite Zeile: Die unabhängige Variable
    ))

    return np.linalg.inv(ones_x @ ones_x.T) @ ones_x @ np.array(y).T



class TestDeviation(TestCase):
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
        result = regression(x, y)
        self.assertAlmostEqual(float(result[0]), a)
        self.assertAlmostEqual(float(result[1]), b)

if __name__ == '__main__':
    main()
