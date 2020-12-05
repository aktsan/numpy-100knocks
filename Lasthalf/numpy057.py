#How to randomly place p elements in a 2D array? (★★☆)
#put(arr,indice,values,)
import numpy as np
a = np.zeros((10,10))
np.put(a,np.random.choice(range(10*10),3,replace=False),1)
print(a)