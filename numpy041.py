#How to sum a small array faster than np.sum? (★★☆)
import time
import numpy as np
a = np.arange(10)
b = [i for i in range(10)]
t1 = time.time()
s = sum(b)
t2 = time.time()
print(t2-t1)
print(s)
t1 = time.time()
sums = np.add.reduce(a)
t2 = time.time()
#比較的小さい配列飲のみこの手法が有効
print(t2-t1)
print(sums)
t1 = time.time()
sums1 = np.sum(a)
t2 = time.time()
print(t2-t1)
print(sums1)