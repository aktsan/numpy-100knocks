# Create a structured array with x and y coordinates covering the [0,1]x[0,1] area (★★☆)
import numpy as np
Z = np.zeros((5,5),[('x',float),('y',float)])
print(Z)
Z['x'], Z['y'] = np.meshgrid(np.linspace(0,1,5),
                             np.linspace(0,1,5))
print(Z)
