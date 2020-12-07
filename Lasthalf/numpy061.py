#Find the nearest value from a given value in an array (★★☆)
import numpy as np
a = np.random.uniform(0,1,10)
num = 0.5
m = a.flat[np.abs(a-num).argmin()]
print(m)