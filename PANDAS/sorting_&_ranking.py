# IMPORTS
import pandas as pd
import numpy as np

ser = pd.Series([5,0,3,8,4],
                index=['red','blue','yellow','white','green'])
# sort_index A - Z
print(ser.sort_index())
print(ser.sort_index(ascending=False))

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index=['red','blue','yellow','white'],
                     columns=['ball','pen','pencil','paper'])
print(frame)
# sort index by row
print(frame.sort_index())
# sort index by columns
print(frame.sort_index(axis=1))

# Sorting Values

# sorting Series
print(ser.sort_values())

# sorting df columns
print(frame.sort_values(by=['pen']))
print(frame.sort_values(by=['pen','pencil']))

# Ranking - number mean the position / ascending mean highest value is number 1 of rank
print(ser.rank())
print(ser.rank(method='first'))
print(ser.rank(ascending=False))
