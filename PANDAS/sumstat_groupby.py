# IMPORTS
import pandas as pd
import numpy as np

# Summary Statistics with groupby Instead of with Level

mframe = pd.DataFrame(np.random.randn(16).reshape((4,4)),
                      index=[['white','white','red','red'],['up','down','up','dwon']],
                      columns=[['pen','pen','paper','paper'],[1,2,1,2]])
mframe.columns.names = ['objects','id']
mframe.index.names = ['colors','status']

#print(mframe.sum(level='colors')) old version

print(mframe.groupby('colors').sum())

print(mframe.groupby('id',axis=1).sum())
print(mframe.T.groupby('id').sum()) # the most newest version T stands for transpose table
