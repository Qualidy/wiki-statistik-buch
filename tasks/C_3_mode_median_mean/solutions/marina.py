import numpy as np
import unittest
from parameterized import parameterized


def median(liste):
    if liste:
        liste = sorted(liste)
        mid = int(len(liste) // 2)

        if len(liste) % 2 == 1:
            return liste[mid]

        return (liste[mid - 1] + liste[mid]) / 2
    return np.nan


def mode(liste):
    if not liste:
        return np.nan

    return _mode_impl(liste)


def _mode_impl(liste):
    frequency = {value: liste.count(value) for value in set(liste)}
    return max(frequency, key=frequency.get)


def mean(liste):
    return sum(liste) / len(liste)


class TestStatistics(unittest.TestCase):
    @parameterized.expand([
        ([1, 2, 3, 4, 5], 3),
        ([10, 20], 15),
        ([-1, 0, 1], 0),
    ])
    def test_mean(self, data, expected):
        self.assertAlmostEqual(mean(data), expected)

    def test_mean_empty(self):
        self.assertTrue(np.isnan(mean([])))

    @parameterized.expand([
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4], 2.5),
        ([7], 7),
    ])
    def test_median(self, data, expected):
        self.assertEqual(median(data), expected)

    def test_median_empty(self):
        self.assertTrue(np.isnan(median([])))

    @parameterized.expand([
        ([1, 2, 2, 3, 4], 2),
        ([4, 4, 4, 1, 2], 4),
        ([1, 2, 3, 4, 5, 5, 6, 7], 5),
    ])
    def test_mode(self, data, expected):
        self.assertEqual(mode(data), expected)


if __name__ == '__main__':
    unittest.main()
