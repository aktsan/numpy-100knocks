#What is the equivalent of enumerate for numpy arrays? (★★☆)
import numpy as np
a = np.arange(9).reshape(3,3)
for i,j in np.ndenumerate(a):
    print(a,j)
for index in np.ndindex(a.shape):
    print(index, a[index])