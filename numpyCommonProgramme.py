import numpy as np
n1=np.array([20,30,40,50])
n2=np.array([40,50,60,70])
print(np.intersect1d(n1,n2))
# difference method
n1=np.array([20,30,40,50])
n2=np.array([40,50,60,70])
print(np.setdiff1d(n1,n2))