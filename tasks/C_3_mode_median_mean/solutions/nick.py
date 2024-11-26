import pandas as pd
import unittest
from parameterized import parameterized


#Modus

def modus(data):
    dict_count = {number:data.count(number) for number in data}
    for key, value in dict_count.items():
        if value == max(dict_count.values()):
            return key


class Test_Modus(unittest.TestCase):
    @parameterized.expand([
        ([1, 2, 3, 4, 1], 1),
        ([1, 1, 1, 1], 1),
        ([1, 2, 1, 1, 2, 2], 1),
        ([100, 2000, 333, 7], 100)])
    def test_parametrized(self, values, expected):
        self.assertEqual(modus(values),expected)


#Median

def median(data):
    data = sorted(data)
    if len(data) % 2 == 0:
        mid1 = len(data) // 2 - 1  
        mid2 = len(data) // 2      
        med = (data[mid1] + data[mid2]) / 2  
        return med
    
    else:
        index = int((len(data) + 1) / 2)
        return data[index - 1]
    
class Test_Modus(unittest.TestCase):
    @parameterized.expand([
        ([1, 2, 3, 4, 1], 2),
        ([1, 1, 1, 1], 1),
        ([1, 2, 1, 1, 2, 2], 1.5),
        ([100, 2000, 333, 7], 216.5)])
    def test_parametrized(self, values, expected):
        self.assertEqual(median(values),expected)


def arith(data):
    return sum(data) / len(data)


class Test_Modus(unittest.TestCase):
    @parameterized.expand([
        ([1, 2, 3, 4, 1], 2.2),
        ([1, 1, 1, 1], 1),
        ([1, 2, 1, 1, 2, 2], 1.5),
        ([100, 2000, 333, 7], 610)])
    def test_parametrized(self, values, expected):
        self.assertEqual(arith(values),expected)
