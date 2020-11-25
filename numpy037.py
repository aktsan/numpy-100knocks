#Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)
import numpy as np
a = np.zeros((5,5))
a += np.arange(5)
print(a)