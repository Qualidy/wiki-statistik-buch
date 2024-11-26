#  der Median,
import pandas as pd


import doctest
doctest.testmod()
data = [1,2,3,4]
def median(values:list):
    """
    >>> median([1,2])
    1.5
    >>> median([1,2,3])
    2
    >>> median([3,2,3])
    3
    >>> median([1])
    1
    >>> median([1,10])
    5.5
    """
    if values:
        values.sort()
        l = len(values)
        return values[l//2] if l %2 else (values[l //2]+values[l //2-1])/2
print(f"{median(data)}")
pd.Series(data).median()
