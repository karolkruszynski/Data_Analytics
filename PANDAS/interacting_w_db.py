# IMPORTS
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# for PostgreSQL
# engine = create_engine('postgresql://karol:karol@localhost:5432/mydatabase')

# Loading and Writing Data with SQLite3 using I/O API

frame = pd.DataFrame(np.arange(20).reshape(4,5),
                     columns=['white','red','blue','black','green'])
print(frame)
engine = create_engine('sqlite:///foo.db')  # creating db in sqlite3
#frame.to_sql('colors', engine)  # insert frame df into table colors to db engine
print(pd.read_sql('colors',engine)) # reading data inside db, colors table

# Loading and Writing Data with SQLite3 without using I/O API
import sqlite3
query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20), c REAL, d INTEGER);
"""
conn = sqlite3.connect(':memory:')
conn.execute(query)
conn.commit()
data = [
    ('white','up',1,3),
    ('black','down',2,8),
    ('green','up',4,4),
    ('red','down',5,5)
]
stmt = "INSERT INTO test VALUES(?,?,?,?)"
conn.executemany(stmt,data)
conn.commit()
cursor = conn.execute('select * from test')
print(cursor)
rows = cursor.fetchall()
print(rows)
# name of the columns
print(cursor.description)
# we create column name list form cursor.description
column_names = [desc[0] for desc in cursor.description]
df = pd.DataFrame(rows, columns=column_names)
print(df)