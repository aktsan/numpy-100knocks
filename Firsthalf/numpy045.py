#Create random vector of size 10 and replace the maximum value by 0 (★★☆)
import numpy as np
a = np.random.random(10)
i = a.argmax()
a[i] = 0
print(a)