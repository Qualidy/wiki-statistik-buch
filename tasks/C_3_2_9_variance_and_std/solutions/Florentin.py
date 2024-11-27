import math
import pandas as pd

buchzahlen = pd.Series([27, 22, 21, 26, 27, 35, 31, 24, 22, 15])


def varianz(zahlen):
    sum_of_squares = sum([x * x for x in zahlen])
    return (sum_of_squares / len(zahlen)) - (zahlen.mean() ** 2)


def standardabweichung(zahlen):
    return math.sqrt(varianz(zahlen))


# doofes parameter ddof auf 0 damit pandas var und std wie im Buch sind
print(f"Die Varianz laut mir {varianz(buchzahlen)}")
print(f"Die Varianz laut pandas {buchzahlen.var(ddof=0)}")
print()
print(f"Die standardabweichung laut mir {standardabweichung(buchzahlen)}")
print(f"Die standardabweichung laut pandas {buchzahlen.std(ddof=0)}")
