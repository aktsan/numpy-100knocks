#How to convert a float (32 bits) array into an integer (32 bits) in place?
import numpy as np 
a = np.arange(10, dtype=float)
print(a)
a = a.astype(np.int32)
print(a)