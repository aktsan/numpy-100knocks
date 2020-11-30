#Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆)
import numpy as np
a = np.zeros(10, [ ('posi',     [ ('x', float, 1),
                                  ('y', float, 1)]),
                   ('color',    [ ('r', float, 1),
                                  ('g', float, 1),
                                  ('b', float, 1)])])
print(a)