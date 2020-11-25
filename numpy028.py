#What are the result of the following expressions?
import numpy as np
a = np.array(0) / np.array(0) #0は割れない
b = np.array(0) // np.array(0) #0は割れない
c = np.array([np.nan]).astype(int).astype(float) #nanをint②変換すると
#intの最小数に変換されるらしい、
print(a,b,c)