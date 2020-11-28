#Create a 2d array with 1 on the border and 0 inside (★☆☆)
#二次元配列,0を1で囲む
import numpy as np
a = np.ones((5,5))
a[1:-1,1:-1] = 0
print(a)