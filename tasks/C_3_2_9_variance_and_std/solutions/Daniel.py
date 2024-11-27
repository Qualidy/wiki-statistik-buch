import unittest
from parameterized import parameterized

def var(values: list):
    if not isinstance(values, list):
        raise TypeError('Values must be a list')
    if not values:  # Überprüfung auf leere Liste
        raise ValueError('Values list is empty')

    return ((sum([val**2 for val in values]))/len(values))-((sum(values)/len(values))**2)

def std(values: list):
    return var(values)**0.5


class TestMathFunctions(unittest.TestCase):

    # Tests für Varianz
    @parameterized.expand([
        ([1, 2, 3, 4, 5], 2.0),
        ([2, 4, 6, 8, 10], 8.0),
        ([1, 1, 1, 1, 1], 0.0),
        ([1], 0.0)
    ])
    def test_var(self, values, expected):
        self.assertAlmostEqual(var(values), expected, places=5)

    @parameterized.expand([
        ('not a list', TypeError),
        ([], ValueError),
    ])
    def test_var_exceptions(self, values, expected_exception):
        with self.assertRaises(expected_exception):
            var(values)

    #Tests für Standardabweichung
    @parameterized.expand([
        ([1, 2, 3, 4, 5], 1.41421356237),
        ([2, 4, 6, 8, 10], 2.82842712475),
        ([1, 1, 1, 1, 1], 0.0),
        ([1], 0.0)
    ])
    def test_std(self, values, expected):
        self.assertAlmostEqual(std(values), expected, places=5)


    @parameterized.expand([
        ('not a list', TypeError),
        ([], ValueError),
    ])
    def test_std_exceptions(self, values, expected_exception):
        with self.assertRaises(expected_exception):
            std(values)

if __name__ == '__main__':
    unittest.main()
