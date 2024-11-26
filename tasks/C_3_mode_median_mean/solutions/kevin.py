import unittest

def get_modus(values: list, multiple_modi=False):
    amounts = {value: values.count(value) for value in values}
    max_amount = max(amounts.values())
    modi = [key for key, count in amounts.items() if count == max_amount]

    if multiple_modi:
        return modi
    else:
        return modi[0]


def get_median(values: list):
    values.sort()

    if len(values) % 2 != 0:
        return values[len(values) // 2]
    else:
        mitte_rechts_pos = len(values) // 2
        mitte_links_pos = mitte_rechts_pos - 1
        return (values[mitte_links_pos] + values[mitte_rechts_pos]) / 2


def get_arithm_mittelwert(values: list):
    return sum(values) / len(values)


class GetModusTest(unittest.TestCase):

    def test_single_modus(self):
        self.assertEqual(get_modus([1, 2, 2, 3, 4]), 2)

    def test_multiple_modi(self):
        self.assertEqual(get_modus([1, 2, 2, 3, 3], multiple_modi=True), [2, 3])

    def test_no_modus(self):
        self.assertEqual(get_modus([1, 2, 3, 4], multiple_modi=True), [1, 2, 3, 4])


class GetMedianTest(unittest.TestCase):

    def test_odd_length(self):
        self.assertEqual(get_median([3, 1, 2]), 2)

    def test_even_length(self):
        self.assertEqual(get_median([4, 2, 3, 1]), 2.5)

    def test_sorted_values(self):
        self.assertEqual(get_median([1, 2, 3, 4, 5]), 3)


class GetArithmMittelwertTest(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(get_arithm_mittelwert([1, 2, 3, 4, 5]), 3.0)

    def test_mixed_numbers(self):
        self.assertEqual(get_arithm_mittelwert([-2, 0, 2, 4]), 1.0)

    def test_single_value(self):
        self.assertEqual(get_arithm_mittelwert([42]), 42.0)


unittest.main(argv=[''], verbosity=2, exit=False)
