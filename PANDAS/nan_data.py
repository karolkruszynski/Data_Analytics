# IMPORTS
import pandas as pd
import numpy as np

ser = pd.Series([0,1,2,np.NaN,9],
                index=['red','blue','yellow','white','green'])
print(ser)
ser['white'] = None
print(ser)

# Filtering Out NaN Values
print(ser.dropna())
# or filtering like
print(ser[ser.notnull()])

# Droping NaN on df
frame3 = pd.DataFrame([[6,np.nan,6],[np.nan,np.nan,np.nan],[2,np.nan,5]],
                      index=['blue','green','red'],
                      columns=['ball','mug','pen'])
print(frame3)
print(frame3.dropna())  # everything disappear cause of default option which delete rows and columns if there is nan

# dropna for df options
print(frame3.dropna(how='all')) # if nan exist for all elements in index
print(frame3.dropna(axis=1))    # also can be usefull to choose axis 0 - indexes 1 - columns


# Filling in NaN Occurrences
print(frame3.fillna(0)) # fill the nan values

# replace NaN depending on the columns
print(frame3.fillna({'ball': 1, 'mug': 0, 'pen': 99}))
