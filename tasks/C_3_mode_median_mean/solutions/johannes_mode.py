import pandas as pd
import unittest
from collections.abc import Iterable
from parameterized import parameterized


# doctest.testmod()
def modalwert(values: list):
    counted = {i: values.count(i) for i in values}
    occ = max(counted.items(), key=lambda x: x[1])[1]
    return {k for k, v in counted.items() if v == occ}


print(f"{modalwert([4, 4, 5, 5])}")


class Test_Modus(unittest.TestCase):
    @parameterized.expand([
        ([1, 2, 3, 4, 1], {1}),
        ([1, 1, 1, 1], {1}),
        ([1, 1, 2, 2], {1, 2}),
        ([100, 2000, 333, 7], {2000, 100, 333, 7})])
    def test_parametrized(self, values, expected):
        self.assertEqual(modalwert(values), expected)


if __name__ == '__main__':
    unittest.main()
