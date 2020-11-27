#How to print all the values of an array? (★★☆)
import numpy as np
a = np.arange(10000)

print(a)
np.set_printoptions(threshold=np.inf)
print(a)