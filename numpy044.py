#Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)
import numpy as np
#座標にする
a = np.random.random((10,2))
print(a)
x,y = a[:,0], a[:,1]
R = np.sqrt(x**2+y**2)
T = np.arctan2(y,x)
print(R)
print(T)