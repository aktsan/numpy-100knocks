#How to find the memory size of any array (★☆☆)
import numpy as np
a = np.zeros(10)
print(a.size * a.itemsize)