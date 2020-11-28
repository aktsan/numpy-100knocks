#Extract the integer part of a random array of positive numbers using 4 different methods (★★☆)
import numpy as np
a = np.random.uniform(1,10,10)
print(a)
print(a-a%1)
print(np.floor(a))
print(np.trunc(a))
print(a // 1)