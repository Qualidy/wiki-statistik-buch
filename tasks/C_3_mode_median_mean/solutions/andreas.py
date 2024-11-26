
import unittest



X = 'pink; silbern; silbern; pink; pink; silbern; silbern; pink; silbern; pink; silbern; pink; silbern; silbern; blau; blau; blau; silbern; silbern; blau'

def modus(lst: str) -> str:
    if lst:
        # return max({word: lst.count(word) for word in lst.split('; ')}.items(), key=lambda x: x[1])[0]
        tmp_lst = {word: lst.count(word) for word in lst.split('; ')}
        # [(k, v) for k, v in lst.items() if v == max(lst.values())]
        return tmp_lst
    else:
        raise ValueError('nix leere Strings')

display(modus(X))


X_even = '10.320; 18.430; 15.240; 12.490; 21.310; 17.310; 18.100; 25.560; 7.440; 16.370'
X_uneven = '10.320; 18.430; 15.240; 12.490; 17.310; 18.100; 25.560; 7.440; 16.370'

def median(lst: str) -> int | float:
    tmp_lst = sorted([int(num.replace('.', '')) for num in lst.split('; ')])
    # display(tmp_lst)
    if len(tmp_lst) % 2 == 0:
        result = (tmp_lst[int(len(tmp_lst) / 2 - 1)] + tmp_lst[int(len(tmp_lst) / 2)]) / 2
    else:
        result = tmp_lst[int(len(tmp_lst) / 2)]
    return result

display(median(X_even))

X_even = '10.320; 18.430; 15.240; 12.490; 21.310; 17.310; 18.100; 25.560; 7.440; 16.370'
X_uneven = '10.320; 18.430; 15.240; 12.490; 17.310; 18.100; 25.560; 7.440; 16.370'

def arithmetic_mean(lst: str) -> int | float:
    return sum(int(num.replace('.', '')) for num in lst.split('; ')) / (len(lst.split('; ')))

display(arithmetic_mean(X_even))


class TestModus(unittest.TestCase):

    def test_00(self):
        given = 'pink; silbern; silbern; pink; pink; silbern; silbern; pink; silbern; pink; silbern; pink; silbern; silbern; blau; blau; blau; silbern; silbern; blau'
        expected = ('silbern', 10)
        self.assertEqual(modus(given), expected)

    def test_01(self):
        given = ''
        expected = ('', 0)
        self.assertEqual(modus(given), expected)

    def test_02(self):
        given = 'pink; pink; pink; blau; blau; blau'
        expected = ('silbern', 10)
        self.assertEqual(modus(given), expected)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
