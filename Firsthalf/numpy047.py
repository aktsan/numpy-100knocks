#Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj))
import numpy as np
a = np.arange(10)
b = a + 0.5
c = 1.0 / np.subtract.outer(a,b)
print(np.linalg.det(c))