import pandas as pd
import numpy as np

data ={
    'color': ['blue', 'red', 'green', 'yellow', 'white'],
    'object': ['ball', 'pen', 'pencil', 'paper', 'mug'],
    'price': [1.2, 1.0, 0.6, 0.9, 1.7]
}

frame = pd.DataFrame(data)
print(frame)

# Assign a Label for Indexes and Columns
frame.index.name = 'id'
frame.columns.name = 'item'
print(frame)

# Adding a new column to df
frame['new'] = 12
print(frame)

frame['new'] = [3.0, 1.3, 2.2, 0.8, 1.1]
print(frame)

series_arange = pd.Series(np.arange(5))
frame['new'] = series_arange
print(frame)

# Change Single Value
#frame['price'][2] = 3.3 # cause an error of set on a copy of a slice from df
#print(frame)
# most clean and correct version of modify single value is through the .loc
frame.loc[2, 'price'] = 3.3
print(frame)

# Membership of value
print(frame.isin([1.0, 'pen']))
print(frame[frame.isin([1.0, 'pen'])])

# Deleting a column
del frame['new']
print(frame)

# Filtering
print(frame[frame['price'] < 1.2])

# df from nested dict
nestdict = {
    'red': {2012: 22, 2013:33},
    'white': {2011: 13, 2012: 22, 2013: 16},
    'blue': {2011: 17, 2012: 27, 2013: 18}
}
frame2 = pd.DataFrame(nestdict) # main dict are columns, nested are rows with value
print(frame2)

# Transposition of df
print(frame2.T) # .T make a transposition, so rows becomes col and col becomes rows

# Index Objects
ser = pd.Series([5, 0, 3, 8, 4], index=['red','blue', 'yellow', 'white', 'green'])
print(ser.index)    # indexes are immutable

# Methods on Index
print(ser.idxmax()) # max value of index
print(ser.idxmin()) # min value of index

# Index with Duplicate Labels
serd = pd.Series(range(6), index=['white','white','blue','green', 'green', 'yellow'])
print(serd)
print(serd['white'])    # when we have duplicated labels we get Series

print(serd.index.is_unique) # .is_unique function check if all indexes are unique
print(frame.index.is_unique)

# Other functionalities on Indexes: Reindexing, Dropping, Alignment

# Reindexing
ser = pd.Series([2, 5, 7, 4], index=['one', 'two', 'three', 'four'])
print(ser)

print(ser.reindex(['three', 'four', 'five', 'one']))    # we can reorder indexes and add or delete. For new label pandas adds NaN to value

ser3 = pd.Series([1, 5, 6, 3], index=[0, 3, 5, 6])
print(ser3)

print(ser3.reindex(range(6), method='ffill'))   # interpolation with lowest met value in series

print(ser3.reindex(range(6), method='bfill'))   # interpolation with highest met value in series

print(frame.reindex(range(5), method='ffill', columns=['colors', 'price', 'new', 'object']))    # reindex could be use also in df

# Dropping

ser = pd.Series(np.arange(4.), index=['red', 'blue', 'yellow', 'white'])
print(ser.drop('yellow'))

# more items to drop
print(ser.drop(['blue', 'white']))

# dropping in df
frame = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index=['red', 'blue', 'yellow', 'white'],
                     columns=['ball', 'pen', 'pencil', 'paper'])
print(frame)
# to drop rows you just pass indexes of rows
print(frame.drop(['blue', 'yellow']))

# to drop columns you need to specify indexes of columns and axis = 1 for columns
print(frame.drop(['pen', 'pencil'], axis=1))


# Arithmetic and Data Alignment
s1 = pd.Series([3,2,5,1], ['white','yellow','green','blue'])
s2 = pd.Series([1,4,7,2,1], ['white','yellow','black','blue','brown'])
print(s1+s2)    # when the labels are present in both operators their values will be added

# for df
frame1 = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index=['red', 'blue', 'yellow', 'white'],
                     columns=['ball', 'pen', 'pencil', 'paper'])
frame2 = pd.DataFrame(np.arange(12).reshape((4,3)),
                     index=['blue','green','white','yellow'],
                     columns=['mug','pen','ball'])
print(frame1+frame2)    # when the labels are present in both operators their values will be added

