#Is the following expressions true? (★☆☆)
import numpy as np
a = np.sqrt(-1) == np.emath.sqrt(-1) #wmathは複素数を使うときに使う
#a = nan == 1j
print(a)