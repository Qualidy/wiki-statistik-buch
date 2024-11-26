from unittest import TestCase
from parameterized import parameterized
import pandas as pd

def modus(data):
    counts = {data.count(d): d for d in set(data)}
    return counts[max(counts.keys())]


def median(data):
    sorted_data = sorted(data)
    n = len(data)
    if n % 2:
        return sorted_data[(n + 1) // 2 - 1]
    else:
        return (sorted_data[(n // 2) - 1] + sorted_data[(n // 2)]) / 2


def arith_mean(data):
    return sum(data) / len(data)


def modus_pd(data):
    return pd.Series(data).mode()[0]


def median_pd(data):
    return pd.Series(data).median()


def arith_mean_pd(data):
    return pd.Series(data).mean()


class ModusTest(TestCase):
    @parameterized.expand([
        [["schlecht", "schlecht", "mittel", "gut", "mittel", "schlecht"], "schlecht"],
        [["gut"], "gut"],
        [["mittel", "mittel", "mittel", "mittel", "mittel", "mittel"], "mittel"]
    ])
    def test_modus(self, data, expected):
        self.assertEqual(modus(data), expected)

    @parameterized.expand([
        [["schlecht", "schlecht", "mittel", "gut", "mittel", "schlecht"], "schlecht"],
        [["gut"], "gut"],
        [["mittel", "mittel", "mittel", "mittel", "mittel", "mittel"], "mittel"]
    ])
    def test_modus_pd(self, data, expected):
        self.assertEqual(modus_pd(data), expected)


class MedianTest(TestCase):
    @parameterized.expand([
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5],
        [[1], 1],
        [[1, 2], 1.5],
        [[1, 40, 1000, 30, 2000000], 40]
    ])
    def test_median(self, data, expected):
        self.assertEqual(median(data), expected)

    @parameterized.expand([
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5],
        [[1], 1],
        [[1, 2], 1.5],
        [[1, 40, 1000, 30, 2000000], 40]
    ])
    def test_median_pd(self, data, expected):
        self.assertEqual(median_pd(data), expected)


class ArithMeanTest(TestCase):
    @parameterized.expand([
        [[1, 2, 3, 4, 5], 3],
        [[1, 2], 1.5],
        [[5], 5],
        [[1, 13, 44, 1000, 123, 4, 7], 170.29]
    ])
    def test_arit_mean(self, data, expected):
        self.assertAlmostEqual(round(arith_mean(data), 2), expected)

    @parameterized.expand([
        [[1, 2, 3, 4, 5], 3],
        [[1, 2], 1.5],
        [[5], 5],
        [[1, 13, 44, 1000, 123, 4, 7], 170.29]
    ])
    def test_arit_mean_pd(self, data, expected):
        self.assertAlmostEqual(round(arith_mean_pd(data), 2), expected)
