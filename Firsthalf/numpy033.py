#How to get the dates of yesterday, today and tomorrow? (★☆☆)
import numpy as np
a = np.datetime64('today')
b = np.timedelta64(1)
print(a-b)
print(a)
print(a+b)