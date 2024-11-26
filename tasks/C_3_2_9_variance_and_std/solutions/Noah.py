def variance(data):
    if not isinstance(data, (list, tuple)):
        raise TypeError("Data must be a list or tuple of numbers.")
    if not data:
        raise ValueError("Cannot calculate variance of an empty dataset.")
    if not all(isinstance(num, (int, float)) for num in data):
        raise ValueError("All elements in the dataset must be numeric.")

    arithmetic_mean = sum(data) / len(data)
    return sum([(num - arithmetic_mean) ** 2 for num in data]) / len(data)


def standard_deviation(data):
    if not isinstance(data, (list, tuple)):
        raise TypeError("Data must be a list or tuple of numbers.")
    if not data:
        raise ValueError("Cannot calculate standard deviation of an empty dataset.")
    if not all(isinstance(num, (int, float)) for num in data):
        raise ValueError("All elements in the dataset must be numeric.")

    return variance(data) ** 0.5


import unittest
from parameterized import parameterized


class TestVariance(unittest.TestCase):

    @parameterized.expand([
        [[23, 16, 18, 17, 22, 28, 26, 22, 20, 8], 29],
        [[27, 22, 21, 26, 27, 35, 31, 24, 22, 15], 28]
    ])
    def test_variance_success(self, values, expected):
        self.assertEqual(variance(values), expected)

    @parameterized.expand([
        [[23, 16, 18, 17, 22, 28, 26, 22, 20, 8], 5.39],
        [[27, 22, 21, 26, 27, 35, 31, 24, 22, 15], 5.29]
    ])
    def test_standard_deviation_success(self, values, expected):
        self.assertAlmostEqual(standard_deviation(values), expected, delta=0.01)

    # Tests für Fehlerfälle
    def test_variance_empty_dataset(self):
        with self.assertRaises(ValueError) as context:
            variance([])
        self.assertEqual(str(context.exception), "Cannot calculate variance of an empty dataset.")

    def test_variance_non_numeric(self):
        with self.assertRaises(ValueError) as context:
            variance([1, "a", 3])
        self.assertEqual(str(context.exception), "All elements in the dataset must be numeric.")

    def test_variance_invalid_type(self):
        with self.assertRaises(TypeError) as context:
            variance("not a list")
        self.assertEqual(str(context.exception), "Data must be a list or tuple of numbers.")

    def test_standard_deviation_empty_dataset(self):
        with self.assertRaises(ValueError) as context:
            standard_deviation([])
        self.assertEqual(str(context.exception), "Cannot calculate standard deviation of an empty dataset.")

    def test_standard_deviation_non_numeric(self):
        with self.assertRaises(ValueError) as context:
            standard_deviation([1, "a", 3])
        self.assertEqual(str(context.exception), "All elements in the dataset must be numeric.")

    def test_standard_deviation_invalid_type(self):
        with self.assertRaises(TypeError) as context:
            standard_deviation({"a": 1})
        self.assertEqual(str(context.exception), "Data must be a list or tuple of numbers.")


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    