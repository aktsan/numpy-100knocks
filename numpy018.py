#Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
import numpy as np
a = np.arange(1,26).reshape(5,5)
print(a)
print(np.diag(a))