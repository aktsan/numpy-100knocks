#What is the output of the following script? (★☆☆)
print(sum(range(5),-1)) #9
#第二引数からスタート、0,1,2,3 4

import numpy as np
print(np.sum(range(5),-1)) #10
#第二引数はaxisを指定、axis-1はaxis0と同じ
print(np.arange(5))
