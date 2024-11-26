def get_median_value(data):
    if not data:
        raise ValueError("The input data is empty. Cannot calculate median value.")

    if not isinstance(data, (list, tuple, set)):
        raise TypeError("Input data must be a list, tuple, or set.")

    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements in the input data must be numeric.")

    data = sorted(data)
    n = len(data)

    if n % 2 != 0:
        return data[n // 2]
    else:
        return 0.5 * (data[(n // 2) - 1] + data[n // 2])


import unittest
from parameterized import parameterized


class TestMedianValue(unittest.TestCase):

    @parameterized.expand([
        [[1, 2, 3, 4, 5], 3],
        [[1, 2, 3, 4, 5, 6], 3.5],
        [[10], 10],
        [[2, 8, 4, 6], 5.0],
        [[0, 0, 0, 0], 0],
        [[-5, -10, -3], -5]
    ])
    def test_median_value_success(self, values, expected):
        self.assertEqual(get_median_value(values), expected)

    def test_empty_data(self):
        with self.assertRaises(ValueError) as context:
            get_median_value([])
        self.assertEqual(str(context.exception), "The input data is empty. Cannot calculate median value.")

    def test_invalid_type(self):
        with self.assertRaises(TypeError) as context:
            get_median_value("string instead of list")
        self.assertEqual(str(context.exception), "Input data must be a list, tuple, or set.")

    def test_non_numeric_values(self):
        with self.assertRaises(ValueError) as context:
            get_median_value([1, 2, "three", 4])
        self.assertEqual(str(context.exception), "All elements in the input data must be numeric.")


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)