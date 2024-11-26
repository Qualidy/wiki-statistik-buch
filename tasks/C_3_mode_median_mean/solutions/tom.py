import unittest
from unittest import TestCase
from parameterized import parameterized

def modalwert(x):
    haeufigkeit = {key: x.count(key) for key in set(x)}

    max_haeufigkeit = max(haeufigkeit.values(), default=0)

    return sorted([key for key, val in haeufigkeit.items() if val == max_haeufigkeit])


class TestModalwert(TestCase):
    @parameterized.expand([
        (["a", "b", "a", "c", "a"], ["a"]),
        ([1, 2, 3, 1, 1], [1]),
        (["a", "b", "b", "a", "c"], ["a", "b"]),
        ([1, 2, 2, 3, 3], [2, 3]),
        ([], []),
        (["a", "b", "c"], ["a", "b", "c"]),
        ([1, 2, 3], [1, 2, 3]),
        (["apple", "banana", "apple", "orange", "banana", "banana"], ["banana"]),
        (["single"], ["single"]),
        ([42], [42])
    ])
    def test_modalwert(self, x, expected):
        self.assertEqual(modalwert(x), expected)


def median(x):
    if not x:
        return None

    x = sorted(x)
    anzahl = len(x)
    if anzahl % 2 == 0:
        mitte_1 = x[anzahl // 2 - 1]
        mitte_2 = x[anzahl // 2]
        return (mitte_1 + mitte_2) / 2 if isinstance(mitte_1, (int, float)) else mitte_1
    else:
        return x[anzahl // 2]


class TestMedian(TestCase):
    @parameterized.expand([

        ([1], 1),
        ([], None),
        ([1, 3, 5], 3),
        ([1, 3, 5, 7], 4),
        ([10, 20, 30, 40, 50], 30),
        ([10, 20, 30, 40], 25),
        ([3, 1, 4, 1, 5, 9], 3.5),
        (["apple", "banana", "cherry"], "banana"),
        (["apple", "banana", "cherry", "date"], "banana"),

    ])
    def test_median(self, input_list, expected):
        self.assertEqual(median(input_list), expected)


def artemetische_mitte(x):
    if not x:
        return None
    if not all(isinstance(i, (int, float)) for i in x):
        raise ValueError("Nur Numerische Wert in der Liste erlaubt.")
    return sum(x) / len(x)


class TestArtemetischeMitte(TestCase):
    @parameterized.expand([
        ([1, 2, 3, 4, 5], 3),
        ([10, 20, 30, 40], 25),
        ([0, 0, 0], 0),
        ([100], 100),
        ([-1, -2, -3, -4], -2.5),
        ([-10, 10], 0),
        ([1.5, 2.5, 3.5], 2.5),
        ([], None),
    ])
    def test_artemetische_mitte(self, input_list, expected):
        self.assertEqual(artemetische_mitte(input_list), expected)

    @parameterized.expand([
        (["a", "b", "c"],),
        ([1, 2, "a", 4],),
    ])
    def test_artemetische_mitte_invalid(self, input_list):
        with self.assertRaises(ValueError) as context:
            artemetische_mitte(input_list)
        self.assertEqual(str(context.exception), "Nur Numerische Wert in der Liste erlaubt.")


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
