#Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
#6,7,8行列の１００番目のインデックスは？
import numpy as np
a = np.unravel_index(99,(6,7,8))
print(a)
a1 = np.arange(336).reshape(6,7,8)
print(a1[1][5][3])