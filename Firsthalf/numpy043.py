#Make an array immutable (read-only) (★★☆)
import numpy as np
a = np.arange(10)
print(a.flags)
a.flags.writeable = False
print(a.flags)