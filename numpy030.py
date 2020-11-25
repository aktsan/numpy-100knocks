#How to find common values between two arrays? (★☆☆)
import numpy as np
a = np.arange(1,11)
b = np.arange(5,16)
print(np.intersect1d(a,b))