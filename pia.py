import matplotlib.pyplot as plt
import numpy as np

y = np.array([40, 20, 25, 15])
mylabel = ["Off", "Leg", "Straigt", "Cover"]

plt.pie(y,labels=mylabel)
plt.show()