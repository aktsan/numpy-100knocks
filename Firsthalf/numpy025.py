#Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)
import numpy as np 
a = np.arange(11)
i = (3 <= a )
j = (a <= 8)
a[i&j] *= -1
print(a)