#IMPORTS
import pandas as pd
import numpy as np

frame3 = pd.DataFrame([[6,np.nan,6],[np.nan,np.nan,np.nan],[2,np.nan,5]],
                      index=['blue','green','red'],
                      columns=['ball','mug','pen'])

# Hierarhical Indexing and Leveling

mser = pd.Series(np.random.rand(8),
                 index=[['white','white','white','blue','blue','red','red','red'],
                        ['up','down','right','up','down','up','down','left']])
print(mser)
print(mser.index)
# selecting through first index
print(mser['white'])
# or select throug second index
print(mser[:,'up'])
# so first indexes are nearest left and second are to their right
# to check specific value type both indexes
print(mser['white','up'])

# We can make df from Series by unstack a hierarchical indexing, second set of indexes converted into new set of columns
print(mser.unstack())

# to convert df to series use stack()
print(frame3.stack())

mframe = pd.DataFrame(np.random.randn(16).reshape((4,4)),
                      index=[['white','white','red','red'],['up','down','up','dwon']],
                      columns=[['pen','pen','paper','paper'],[1,2,1,2]])
print(mframe)

# Reordering and Sorting Levels

# swaplevel() / level means indexes
mframe.columns.names = ['objects','id']
mframe.index.names = ['colors','status']
print(mframe)
print(mframe.swaplevel('colors','status'))   # w/o a modify data inside df

# sorting - funct orders data cosnidering only by levels specifying it as parameter
print(mframe.sort_index(level='status'))

# Level = sub index or sub column