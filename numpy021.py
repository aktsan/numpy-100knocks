#Create a checkerboard 8x8 matrix using the tile function (★☆☆)
import numpy as np
a = np.array([0,1])
b = np.array([1,0])
print(np.tile(np.array([a,b]),(4,4)))
