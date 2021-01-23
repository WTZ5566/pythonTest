import numpy as np
V0=20
V1=20000
gdb=20*(np.log10(V1/V0))
v1_30=10**(30/20)*V0
v1_50=10**(50/20)*V0
print(v1_30/v1_50)