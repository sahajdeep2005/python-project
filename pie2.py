import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "mango", "orange"]

myexplode = [0.2, 0.1, 0, 0]
plt.pie(y, labels = mylabels,explode=myexplode,shadow=True, )

plt.show()
