# IMPORTS
import numpy as np
import pandas as pd

s = pd.Series([12, -4, 7 ,9])
print(s)

s = pd.Series([12, -4, 7 ,9], index=['a', 'b', 'c', 'd'])
print(s)

print(s.values)
print(s.index)

# Selecting Internal Elements
print(s[2])
print(s['c'])   # its more clear to use selecting by index name
print(s[0:2])   # slicing
print(s[['b', 'c']]) # multiple labels show in array list

# Evaluating Vales
serd = pd.Series([1, 0, 2, 1, 2, 3], index=['white', 'white', 'blue', 'green', 'green', 'yellow'])
print(serd)

# Unique Values
print(serd.unique())

# Value Counts
print(serd.value_counts())  # left column - unique items | right column - count

# isin
print(serd.isin([0,3])) # boolean value return

print(serd[serd.isin([0,3])])   # show result that contains 0 or 3 value inside

# Nan Values
s2 = pd.Series([5, -3, np.NaN, 14])
print(s2)

# isnull notnull
print(s2.isnull())
print(s2.notnull())

# inside a filter
print(s2[s2.isnull()])
print(s2[s2.notnull()])

# Series as Dictionary
mydict = {
    'red': 2000,
    'blue': 1000,
    'yellow': 500,
    'orange': 1000
}
myseries = pd.Series(mydict)
print(myseries)

colors = ['red', 'yellow', 'orange', 'blue', 'green']
myseries = pd.Series(mydict, index=colors)  # for missmatch it will be NaN value
print(myseries)

# Operations Between Series
mydict2 = {
    'red': 400,
    'yellow': 1000,
    'black': 700
}

myseries2 = pd.Series(mydict2)
print(myseries + myseries2) # only data with the same labels will be sum, others will be shown as NaN