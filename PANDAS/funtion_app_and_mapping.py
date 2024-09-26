import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index=['red','blue','yellow','white'],
                     columns=['ball','pen','pencil','paper'])
# Function by Element
print(np.sqrt(frame))

# Function by Row or Column
f = lambda x: x.max() - x.min()
# or
#def f(x):
    #return x.max() - x.min()

# using apply function you can apply your function on df
print(frame.apply(f))
# by default it will be apply to column by if you want you can apply it for rows
print(frame.apply(f, axis=1))

# return a series
def f(x):
    return pd.Series([x.min(), x.max()], index=['min','max'])
print(frame.apply(f))

# Statistic Functions
print(frame.sum())
print(frame.mean())

# describe
print(frame.describe())