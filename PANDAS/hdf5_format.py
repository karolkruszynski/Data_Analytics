# IMPORTS
import pandas as pd
import numpy as np
from pandas.io.pytables import HDFStore

frame = pd.DataFrame(np.arange(16).reshape(4,4),
                     index=['white','black','red','blue'],
                     columns=['up','down','right','left'])
store = HDFStore('mydata.h5')
store['obj1'] = frame
print(frame)
store['obj2'] = frame
print(store)    # store include 2 data structures in single file represented by the store variable
print(store['obj2'])    # variable obj2
