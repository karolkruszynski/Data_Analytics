# IMPORTS
import pandas as pd
import numpy as np

# Corr and Cov for Series

seq2 = pd.Series([3,4,3,4,5,4,3,2],['2006','2007','2008','2009','2010','2011','2012','2013'])
seq = pd.Series([1,2,3,4,4,3,2,1],['2006','2007','2008','2009','2010','2011','2012','2013'])

print(seq.corr(seq2))
print(seq.cov(seq2))

# Corr and Cov for df

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index=['red','blue','yellow','white'],
                     columns=['ball','pen','pencil','paper'])

frame2 = pd.DataFrame([[1,4,3,6],[4,5,6,1],[3,3,1,5],[4,1,6,4]],
                      index=['red','blue','yellow','white'],
                      columns=['ball','pen','pencil','paper'])
print(frame2)
print(frame2.corr())
print(frame2.cov())

# corrwith function

ser = pd.Series([0,1,2,3,9],
                index=['red','blue','yellow','white','green'])

# corr between indexes df / ser
print(frame2.corrwith(ser))
# corr between columns df / df
print(frame2.corrwith(frame, axis=0))
# corr between indexes df / df
print(frame2.corrwith(frame, axis=1))