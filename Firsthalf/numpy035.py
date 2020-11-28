#How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)
import numpy as np
a = np.ones(3)*1
b = np.ones(3)*2
print(np.add(a,b,out=b))
print(np.divide(a,2,out=a))
print(np.negative(a,out=a))
print(np.multiply(a,b,out=a))