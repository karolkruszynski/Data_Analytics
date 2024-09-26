# Imports
import numpy as np

structured = np.array([(1, 'First', 0.5, 1+2j), (2, 'Second', 1.3, 2-2j), (3, 'Third', 0.8, 1+3j)], dtype=('i2, a6, f4, c8'))
print(structured)

structured = np.array([(1, 'First', 0.5, 1+2j), (2, 'Second', 1.3, 2-2j), (3, 'Third', 0.8, 1+3j)], dtype=('int16, a6, float32, complex64'))
print(structured.dtype)

print(structured['f1']) # f1 == to string values (6char), f stands for FIELD

structured = np.array([(1, 'First', 0.5, 1+2j), (2, 'Second', 1.3, 2-2j), (3, 'Third', 0.8, 1+3j)], dtype=[('id','i2'),('position','a6'),('value', '<f4'),('complex','<c8')])
print(structured.dtype) # here we assign name to the fields  f0-id f1-position f2-value f3-complex

# or you can redefining it by the tupels
structured.dtype.names = ('id', 'order', 'value', 'cmplx')
print(structured.dtype)
print(structured['order'])

