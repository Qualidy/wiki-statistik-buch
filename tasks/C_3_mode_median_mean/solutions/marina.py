import pandas as pd
import numpy as np
import unittest


data_steps = [127,120,133,94,133,120,133,133,113,94,230,120,230,80,113,80,120,250,133,106]

def my_median(liste):
    if liste:
        liste = sorted(liste)
        mid = int(len(liste)//2)

        if len(liste) % 2 == 1:
            return liste[mid]
        
        return (liste[mid-1] + liste[mid])/2
    return np.nan

# print(pd.Series(data_steps).median())
# print(my_median(data_steps))


def my_modus(liste):
    if liste:
        frequency = {value: liste.count(value) for value in set(liste)}
        return max(frequency, key=frequency.get)
    return np.nan

# print(pd.Series(data_steps).mode())
# print(my_modus(data_steps))


def my_mean(liste):
    if liste:
        return sum(liste)/len(liste)
    return np.nan

# print(pd.Series(data_steps).mean())
# print(my_mean(data_steps))



class TestFunctions(unittest.TestCase):

    def test_my_mean_1(self):
        self.assertAlmostEqual(my_mean([1, 2, 3, 4, 5]), 3)
    
    def test_my_mean_2(self):
        self.assertAlmostEqual(my_mean([10, 20]), 15)
    
    def test_my_mean_3(self):
        self.assertAlmostEqual(my_mean([-1, 0, 1]), 0)

    def test_my_mean_4(self):
        self.assertTrue(np.isnan(my_mean([])))

    def test_my_median_1(self):
        self.assertEqual(my_median([1, 2, 3, 4, 5]), 3)

    def test_my_median_2(self):
        self.assertEqual(my_median([1, 2, 3, 4]), 2.5)

    def test_my_median_3(self):
        self.assertEqual(my_median([7]), 7)

    def test_my_median_4(self):
        self.assertTrue(np.isnan(my_median([])))

    def test_my_modus_1(self):
        self.assertEqual(my_modus([1, 2, 2, 3, 4]), 2)

    def test_my_modus_2(self):
        self.assertEqual(my_modus([4, 4, 4, 1, 2]), 4)
    
    def test_my_modus_3(self):
        self.assertEqual(my_modus([1, 2, 3, 4, 5, 5, 6, 7]), 5)
   


if __name__ == '__main__':
    unittest.main()