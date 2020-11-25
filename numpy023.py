#Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)
import numpy as np
colors = np.dtype([('r',np.ubyte),('g',np.ubyte),('b',np.ubyte),('a',np.ubyte)])
print(colors)