# Consider a generator function that generates 10 integers and use it to build an array
import numpy as np
def generate():
    for i in range(10):
        yield i
a = np.fromiter(generate(),dtype=int)
print(a)
