import pandas as pd
import numpy as np

data_steps = [1,2,3,4]

def my_variance(liste):
    if not liste:
        return np.nan
    return sum([(n-np.mean(liste)) ** 2 for n in liste]) / len(liste)

print(pd.Series(data_steps).var())
print(np.var(data_steps))
print(my_variance(data_steps))

def my_st_dev(liste):
    return np.sqrt(my_variance(liste))

print(pd.Series(data_steps).std())
print(np.std(data_steps))
print(my_st_dev(data_steps))
