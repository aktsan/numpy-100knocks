#Consider two random array A and B, check if they are equal (★★☆)
import numpy as np
a = np.random.random((5,5))
b = np.random.random((5,5))
c = np.array_equal(a,b)
print(c)
d = np.arange(10)
e = np.arange(10)
print(np.array_equal(d,e))