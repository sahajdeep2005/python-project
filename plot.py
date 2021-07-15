import matplotlib.pyplot as plt
import numpy as np
x=np.array(range(1,11))
print(x)
y1=2*x
y2=3*x
print(y1)
print(y2)
plt.plot(x,y1,color='black',linestyle=':')
plt.plot(x,y2,color='orange',linestyle=':')
plt.xlabel("this is x axis")
plt.ylabel('this is y axis')
plt.show()






