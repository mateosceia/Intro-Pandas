import pandas as pd
from pandas.core import series
from pandas.core.algorithms import value_counts
serie = pd.Series([1, 3, 5, 7, 9]) 
serie2 = pd.Series([1, 4, 10, 14, 19])
print(serie + serie2)
print(serie - serie2)
print(serie * serie2) 
print(serie / serie2)  