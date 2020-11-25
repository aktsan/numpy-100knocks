#Consider an integer vector Z, which of these expressions are legal? (★☆☆)
import numpy as np
Z = np.array([5])
a = Z**Z
b = 2 << Z >> 2
c = Z <- Z
d = 1j*Z
f = Z/1/1
g = Z<Z>Z

print(a,b,c,d,f,g)
