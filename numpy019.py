#Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
import numpy as np
a = np.zeros((8,8),dtype=int)
a[1::2,::2] = 1
a[::2,1::2] = 1
print(a)