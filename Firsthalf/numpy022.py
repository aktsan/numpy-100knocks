#Normalize a 5x5 random matrix (★☆☆)
import numpy as np
a = np.random.random((5,5))
norm = (a-np.mean(a)) / np.std(a)
print(norm)