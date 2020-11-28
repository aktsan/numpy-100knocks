#How to find the closest value (to a given scalar) in a vector? (★★☆)
import numpy as np
Z = np.arange(100)
v = np.random.uniform(0,100)
print(Z)
print(v)
#最小のところのインデックスを返す
index = (np.abs(Z-v)).argmin()
print(Z[index])