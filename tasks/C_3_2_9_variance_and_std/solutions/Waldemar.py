import pandas as pd
from collections.abc import Iterable

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 40, 20, 10, 22, 30]


def calculate_variance_standart_deviation(iterable):
    if not isinstance(iterable, Iterable):
        raise ValueError("parameter must be iterable")

    df_iterable = pd.Series(iterable)
    arith_middle = df_iterable.mean()
    len_iter = len(iterable)

    variance = sum((x - arith_middle) ** 2 for x in iterable) / len_iter

    standard_deviation = variance ** 0.5

    return variance, standard_deviation