import pandas as pd
import numpy as np

data ={
    'color': ['blue', 'red', 'green'],
    'object': ['ball', 'pen', 'pencil'],
    'price': [1.2, 1.0, 0.6]
}

frame = pd.DataFrame(data)
print(frame)

frame2 = pd.DataFrame(data, columns=['object', 'price']) # select specfic columns from dict to put into dataframe
print(frame2)

frame3 = pd.DataFrame(data, index=['one', 'two', 'three'])  # add custom indexes
print(frame3)

frame4 = pd.DataFrame(np.arange(16).reshape((4,4)),
                      index=['red', 'blue', 'yellow', 'white'],
                      columns=['ball', 'pen', 'pencil', 'paper'])
print(frame4)

# Selecting
print(frame.columns)
print(frame.values)
print(frame['price'])
# or
print(frame.price)  # this can cause an error (price) can be also name of the variable
print(frame.loc[2]) # return the row number 2
print(frame.loc[[0,2]]) # multiple rows select

# portion of rows
print(frame[0:2]) # 2 is excluded soo we have 0 and 1 index

print(frame['object'][2])   # we took 2 element from object column
