import numpy as np
array1 = np.array(range(30))
a=array1.reshape((5,6),order="f")
b=np.where(a%6==1)
