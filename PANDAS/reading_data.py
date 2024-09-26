# IMPORTS
import pandas as pd
import numpy as np

# I/O API Tools
# read_csv, read_excel, read_hdf, read_sql, read_json, read_html, read_stata, read_clipboard, read_pickle, read_msgpack, read_gbp
# to_csv, to_excel etc.

csvframe = pd.read_csv('ch05_01.csv')
print(csvframe)

# also you can use this
csvframe = pd.read_table('ch05_01.csv', sep=',')    # you need to specify separator
print(csvframe)

csvframe_test = pd.read_csv('ch05_02.csv')  # function take first row as a header to avoid it try with header=None
print(csvframe_test)

# now columns names will be number starts from 0
csvframe_test = pd.read_csv('ch05_02.csv', header=None)
print(csvframe_test)

# you can also assign the list of names for columns
csvframe_test = pd.read_csv('ch05_02.csv', names=['white','red','blue','green','animal'])
print(csvframe_test)

# for hierarchical indexes pass the index_col parametr
csvframe = pd.read_csv('ch05_03.csv', index_col=['color','status'])
print(csvframe)


# Using REGEXP to parse txt files

file = pd.read_table('ch05_04.txt', sep='\s+', engine='python')
print(file)

file2 = pd.read_table('ch05_05.txt', sep='\D+', header=None, engine='python')
print(file2)

file3 = pd.read_table('ch05_06.txt', sep=',', skiprows=[0,1,3,6])
print(file3)

# Reading TXT files into parts

file4 = pd.read_csv('ch05_02.csv', skiprows=[2], nrows=3, header=None)  # we skip row 2 and take only first 3 so last one wasn't read
print(file4)

out = pd.Series(dtype='float64')
i = 0
pieces = pd.read_csv('ch05_01.csv', chunksize=3)    # chunksize == portion to store, 3 rows
for piece in pieces:
    out.at[i] = piece['white'].sum()    # at == loc
    i = i + 1
print(out)

# Read HTML - need install lxml module
web_frames = pd.read_html('myFrame.html')
print(web_frames[0])

ranking = pd.read_html('https://www.fiaformula3.com/Standings/Driver')
print(ranking[0])

from lxml import objectify

xml = objectify.parse('books.xml')
print(xml)
root = xml.getroot()    # tree of tags from XML file like Book Author PublishDate etc

print(root.Book.Author)
print(root.Book.PublishDate)

print(root.getchildren())   # getchildren stands for all child elements from node root (we got 2, 2x Book inside xml file)

print([child.tag for child in root.Book.getchildren()]) # geting back all tag attribute from node Book
print([child.text for child in root.Book.getchildren()])    # geting back all text between tags in Book node

# to make df from lxml.etree structure you need to convert it

def etree2df(root):
    columns_names = []
    for i in range(0,len(root.getchildren()[0].getchildren())):
        columns_names.append(root.getchildren()[0].getchildren()[i].tag)    # tags as a columns names: Author, Price etc.
    xml_frame = pd.DataFrame(columns=columns_names)     # assign columns names
    for j in range(0, len(root.getchildren())):
        obj = root.getchildren()[j].getchildren()
        texts = []
        for k in range(0, len(columns_names)):
            texts.append(obj[k].text)   # scrape text from tags (whole row)
        row = dict(zip(columns_names, texts))   # put columns and row together
        row_s = pd.Series(row)  # single node as a Series
        row_s.name = j  # index for Series
        xml_frame = pd.concat([xml_frame, row_s.to_frame().T], ignore_index=True)   # Transpose Series to fit into df
    return xml_frame
print(etree2df(root))

# Excel write/read data

print(pd.read_excel('ch05_data.xlsx'))  # default load the data in first spreadsheet
print(pd.read_excel('ch05_data.xlsx', 'Sheet2'))
# or
print(pd.read_excel('ch05_data.xlsx', 1))

# JSON format
print(pd.read_json('frame.json'))

# Usually JSON format is not tabular soo you need to change dictionary structure into tabular form.
from pandas import json_normalize
import pandas.io.json as json

file = open('books.json', 'r')
text = file.read()
text = json.ujson_loads(text)
print(pd.json_normalize(text,'books'))  # we get a nested value by default
print(pd.json_normalize(text,'books',['writer','nationality'])) # we need to pass the key value


