#How to ignore all numpy warnings (not recommended)? (★☆☆)
import numpy as np
np.seterr(divide='ignore') #0除算を無視扱いとする
a = np.array(0)
print(1/a)