# IMPORTS
import pandas as pd
import numpy as np

# docker pull mongo
# docker run --name mymongo -p 27017:27017 -d mongo
# pip install pymongo

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.mydatabase
# to look if db was created you can
print(db)
# or
print(client['mydatabase'])

# after creating db you have to define the collection (group of stored documents, similar to tables)
collection = db.mycollection
print(db['mycollection'])
# or
print(collection)

frame = pd.DataFrame(np.arange(20).reshape(4,5),
                     columns=['white','red','blue','black','green'])
print(frame)

# WRITE DATA
# before added data to collection you need to convert it to JSON. you need to recorded on the DB in order to be re-extracted as df.
import json
# transpose frame and take values
record = json.loads(frame.T.to_json()).values()
print(record)
# now you are ready to insert document in to the collection
collection.mydocument.insert_many(record)
print('\n')
# READ DATA using find and list to df
result = collection['mydocument'].find()
df = pd.DataFrame(list(result))
del df['_id']
print(df)
