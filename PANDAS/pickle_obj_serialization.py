# IMPORTS
import pandas as pd
import numpy as np
import _pickle as pickle

# PICKLING by _pickle module
# What is Serialization - change data format into ASCII format

data = {'color': ['white','red'], 'value': [5, 7]}

# performing serialization of the data obj
pickled_data = pickle.dumps(data)
print(pickled_data)

# deserialization
nframe = pickle.loads(pickled_data)
print(nframe)

# PICKLING by pandas module
# pickling by pandas is not completely in ASCII format

frame = pd.DataFrame(np.arange(16).reshape(4,4), index=['up','down','left','right'])
frame.to_pickle('frame.pkl')    # serialization into file that pickle data
print(pd.read_pickle('frame.pkl'))

# be carefull what file do you open which is pickling this format was not designed to be protected against erroneous and maliciously constructed data