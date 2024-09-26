# IMPORTS
import pandas as pd
import numpy as np

# Loading, Assembling, Merging, Concatenating, Combining, Reshaping(pivoting), Removing

# Merging, Concatenating, Combining

# Merging - merge() - connects rows based on one or more key. Similar to JOIN in SQL

frame1 = pd.DataFrame({'id':['ball','pencil','pen','mug','ashtray'],
                       'price':[12.33,11.44,33.21,13.23,33.62]})
print(frame1)
frame2 = pd.DataFrame({'id':['pencil','pencil','ball','pen'],
                       'color':['white','red','red','black']})
print(frame2)
print(pd.merge(frame1,frame2))  # merging by first common column 'id'

# 'on' argument define the key column
#print(pd.merge(frame1,frame2, on='price'))  # we need to have same column in both df

frame1 = pd.DataFrame({'id':['ball','pencil','pen','mug','pen'],
                       'color':['white','red','red','black','green'],
                       'brand':['OMG','ABC','ABC','POD','POD']})
print(frame1)
frame2 = pd.DataFrame({'id':['pencil','pencil','ball','pen'],
                       'brand':['OMG','POD','ABC','POD']})
print(frame2)
# merging df with the same column without a 'on' parametr give a list with last element from first df
print(pd.merge(frame1,frame2))

# we need to add specific criteria
print(pd.merge(frame1,frame2,on='id'))  # we have only results where both id exist in df so w/o 'mug' id
print(pd.merge(frame1,frame2,on='brand'))

# if we don't have same column name we can you left_on and right_on option.
frame2.columns = ['sid','brand']
# left - first df , right - second df
print(pd.merge(frame1,frame2,left_on='id', right_on='sid'))

# merging with HOW parametr
frame2.columns = ['id','brand']
print(pd.merge(frame1,frame2,on='id'))
# select the outer join
print(pd.merge(frame1,frame2,on='id',how='outer'))  # we have results existing only in own df - outer join
print(pd.merge(frame1,frame2,on='id',how='left'))   # result form frame1 and exist in both df - left join
print(pd.merge(frame1,frame2,on='id',how='right'))  # result form frame2 and exist in both df - right join

# merging by multiple keys
print(pd.merge(frame1,frame2,on=['id','brand'], how='outer'))   # all results

# MERGING on an INDEX
# left 0r right index set to True
print(pd.merge(frame1,frame2, right_index=True, left_index=True))   # result have 4 indexes like in smallest df
# or use a join, the columns shouldn't have same name
frame2.columns = ['id2','brand2']
print(frame1.join(frame2))  # we have 5 indexes with NaN insert into columns for frame2 where we dont have 5th index

# Concatenating
array1 = np.arange(9).reshape((3,3))
array2 = np.arange(9).reshape((3,3))+6
print(np.concatenate([array1,array2], axis=1))  # concat through rows
print(np.concatenate([array1,array2], axis=0))  # concat through columns

# Concat labeled on Series
ser1 = pd.Series(np.random.rand(4), index=[1,2,3,4])
ser2 = pd.Series(np.random.rand(4), index=[5,6,7,8])
print(pd.concat([ser1,ser2]))   # by default it will work on axis = 0 (col) and return Series but in axis =1 (rows) return dataframe
print(pd.concat([ser1,ser2], axis=1)) # but concat parts are not identifiable in results
# hierarchical indexes by keys argument
print(pd.concat([ser1,ser2], keys=[1,2]))
print(pd.concat([ser1,ser2], keys=[1,2], axis=1))

# Concat on DataFrame
frame1 = pd.DataFrame(np.random.rand(9).reshape(3,3), index=[1,2,3], columns=['A','B','C'])
frame2 = pd.DataFrame(np.random.rand(9).reshape(3,3), index=[4,5,6], columns=['A','B','C'])
print(pd.concat([frame1,frame2]))
print(pd.concat([frame1,frame2],axis=1))

# Combining
ser1 = pd.Series(np.random.rand(5), index=[1,2,3,4,5])
print(ser1)
ser2 = pd.Series(np.random.rand(4), index=[2,4,5,6])
print(ser2)
print(ser1.combine_first(ser2)) #ser1 will be add on the top of ser2 soo, we see only 6th index from ser2
print(ser2.combine_first(ser1))

# Partial Combining
print(ser1[:3].combine_first(ser2[:3])) #ser1 (1,2,3) ser2(4,5)