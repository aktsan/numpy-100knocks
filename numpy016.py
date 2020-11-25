#How to add a border (filled with 0's) around an existing array? (★☆☆)
#pad：第一引数に配列、二に囲む数、第三に囲む数字を指定
import numpy as np
a = np.arange(1,26).reshape(5,5)
print(a)
nums = np.pad(a,(1,1),'constant')
print(nums)