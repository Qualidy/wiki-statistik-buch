def get_modal_value(data):
    if not data:
        raise ValueError("Cant calculate Modal value for empty array like sequence.")
    my_dict = {}
    for num in sorted(data):
        my_dict[num] = my_dict.get(num, 0) + 1

    max_val = max(my_dict.values())
    modal_val = [key for key, value in my_dict.items() if max_val == value]
    return modal_val


data = [127, 120, 133, 94, 133, 120, 133, 133, 113, 94, 230, 120, 230, 80, 113, 80, 120, 250, 133, 106, 44, 44, 44, 44,
        44]
get_modal_value(data)

import unittest
from parameterized import parameterized


class TestModalValue(unittest.TestCase):

    @parameterized.expand([
        [[127, 120, 133, 94, 133, 120, 133, 133, 113, 94, 230, 120, 230, 80, 113, 80, 120, 250, 133, 106, 44, 44, 44,
          44, 44], [44, 133]],
        [[1, 2, 3, 3, 3, 4, 5, 6, 6, 7], [3]],
        [[1, 1, 1, 2, 3, 4, 5, 5, 5, 5], [5]],
        [["pink", "silber", "pink"], ["pink"]],
        [["a", "b", "b", "a", "c", "a"], ["a"]],
        [["dog", "cat", "dog", "dog", "mouse", "cat"], ["dog"]]
    ])
    def test_modal_val_success(self, values, expected):
        self.assertEqual(get_modal_value(values), expected)

    def test_value_error(self):
        with self.assertRaises(ValueError) as context:
            get_modal_value([])
        self.assertEqual(str(context.exception), "Cant calculate Modal value for empty array like sequence.")


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    