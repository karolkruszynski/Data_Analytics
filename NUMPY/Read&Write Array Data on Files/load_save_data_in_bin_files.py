# Imports
import numpy as np

data = np.random.random((3,3))
print(data)
np.save('saved_data', data)

loaded_data = np.load('saved_data.npy')
print(loaded_data)

# Reading Files with Tabular Data
data = np.genfromtxt('ch3_data.csv', delimiter=',', names=True)
print(data)
print(data.dtype)   # heading become the fields names

# Error handling if missing Value
data2 = np.genfromtxt('ch3_data2.csv', delimiter=',', names=True)
print(data2)
print(data2.dtype)
print(data2['id'])  # column by field name
print(data2[0]) #row