def mode(values: list, multiple: bool = False):
    if not isinstance(values, list):
        raise TypeError('Values must be a list')
    if not values:  # Überprüfung auf leere Liste
        raise ValueError('Values list is empty')

    haeufigkeit = {val: values.count(val) for val in values}
    max_count = max(haeufigkeit.values())
    modi = [key for key, count in haeufigkeit.items() if count == max_count]

    if multiple:
        return modi
    else:
        return modi[0]

# Allgemeinere Typehints und Prüfungen:
# from collections.abc import Iterable
#
# def mode_chatgpt(values, multiple=False):
#     if not isinstance(values, Iterable):
#         raise TypeError('Values must be Iterable.')




def median(values: list):
    if not isinstance(values, list):
        raise TypeError('Values must be a list')
    if not values:  # Überprüfung auf leere Liste
        raise ValueError('Values list is empty')
    values.sort()
    n = len(values)
    mid = n // 2
    if n % 2 == 0:
        return (values[mid + 1] + values[mid]) / 2
    else:
        return values[mid]


def mean(values: list):
    if not isinstance(values, list):
        raise TypeError('Values must be a list')
    if not values:  # Überprüfung auf leere Liste
        raise ValueError('Values list is empty')
    return sum(values) / len(values)


from unittest import TestCase, main, skip
from parameterized import parameterized


class GroupTest(TestCase):
    @parameterized.expand([
        ([1, 2, 2, 3, 4], 2),
        ([1, 1, 1, 1, 1], 1),
        ([1, 2, 3, 4, 4, 4, 5], 4),
        ([1, 2, 2, 3, 3, 4], [2, 3])
    ])
    def test_modal(self, values, expected):
        if isinstance(expected, list):
            self.assertListEqual(mode(values, multiple=True), expected)
        else:
            self.assertEqual(mode(values), expected)

    @parameterized.expand([
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4], 3.5),
        ([7, 8, 9, 10, 11], 9)
    ])
    def test_median(self, values, expected):
        self.assertAlmostEqual(median(values), expected)

    @parameterized.expand([
        ([1, 2, 3, 4, 5], 3),
        ([10, 20, 30, 40, 50], 30),
        ([1, 1, 1, 1, 1], 1)
    ])
    def test_mean(self, values, expected):
        self.assertAlmostEqual(mean(values), expected)


if __name__ == '__main__':
    main()
