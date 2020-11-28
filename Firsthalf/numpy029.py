#How to round away from zero a float array ? (★☆☆)
import numpy as np
a = np.ceil(3.12) #切り上げ
b = np.floor(3.12) #切り捨て
c = np.round(3.1215192,4) #四捨五入
print(a)
print(b)
print(c)