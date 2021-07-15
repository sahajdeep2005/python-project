import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, ])
y = np.array([240, 250, 260, 270, 280])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()

plt.show()
