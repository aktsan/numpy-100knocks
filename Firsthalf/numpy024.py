#Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)
import numpy as np
a = np.arange(15).reshape(5,3)
b = np.arange(6).reshape(3,2)
print(a)
print(b)
print(np.dot(a,b))