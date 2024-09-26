# IMPORTS
import pandas as pd
import numpy as np

# Writing Data
frame = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index=['red','blue','yellow','white'],
                     columns=['ball','pen','pencil','paper'])
frame.to_csv('ch05_07.csv')

# no defaults header and indexes write
frame.to_csv('ch05_07b.csv', index=False, header=False)     # we dont have first values from left (interpret as indexes) and columns names

frame2 = pd.DataFrame([[6,np.nan,np.nan,6,np.nan],
                       [np.nan,np.nan,np.nan,np.nan,np.nan,],
                       [np.nan,np.nan,np.nan,np.nan,np.nan,],
                       [20,np.nan,np.nan,20.0,np.nan,],
                       [19,np.nan,np.nan,19.0,np.nan,]
                       ],
                      index=['blue','green','red','white','yellow'],
                      columns=['ball','mug','paper','pan','pencil'])
frame2.to_csv('ch05_08.csv')    # we get a no value if nan like 19,,,,19.0,,
# to avoid this we can use na_rep
frame2.to_csv('ch05_09.csv', na_rep='NaN')
frame2.to_csv('ch05_09b.csv', na_rep=0)

# Writing Data in HTML
frame = pd.DataFrame(np.arange(4).reshape((2,2)))
print(frame)
print(frame.to_html())

frame = pd.DataFrame(np.random.random((4,4)),
                     index=['white','black','red','blue'],
                     columns=['up','down','right','left'])
print(frame)

# writing HTML through pandas
s = ['<HTML>']
s.append('<HEAD><TITLE>My DataFrame</TITLE></HEAD>')
s.append('<BODY>')
s.append(frame.to_html())
s.append('</BODY></HTML>')
html = "".join(s)

html_file = open('myFrame.html','w')
html_file.write(html)
html_file.close()

# Excel

frame = pd.DataFrame(np.random.random((4,4)),
                     index=['exp1','exp2','exp3','exp4'],
                     columns=['Jan2015','Fab2015','Mar2015','Apr2005'])
print(frame)
print(frame.to_excel('ch05-data2.xlsx'))

# JSON format
frame = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index=['white','black','red','blue'],
                     columns=['up','down','right','left'])
frame.to_json('frame.json')