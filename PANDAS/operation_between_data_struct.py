import pandas as pd
import numpy as np

frame1 = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index=['red', 'blue', 'yellow', 'white'],
                     columns=['ball', 'pen', 'pencil', 'paper'])
frame2 = pd.DataFrame(np.arange(12).reshape((4,3)),
                     index=['blue','green','white','yellow'],
                     columns=['mug','pen','ball'])

# Flexible Arithmetic Methods
print(frame1.add(frame2))   # add
print(frame1.sub(frame2))   # substract
print(frame1.div(frame2))   # divide
print(frame1.mul(frame2))   # multiply

# Operation Between Dataframes and Series
frame = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index=['red', 'blue', 'yellow', 'white'],
                     columns=['ball', 'pen', 'pencil', 'paper'])
ser = pd.Series(np.arange(4), index=['ball', 'pen', 'pencil', 'paper'])

print(frame - ser) # the value is substracted for all values of the column, regardless of their index (rows label)

ser['mug'] = 9
print(frame - ser) # if index will not present in both of data_struct it will be add as new column full of NaN value


