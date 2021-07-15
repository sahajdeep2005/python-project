

import matplotlib.pyplot as plt
student={'sam':23,'Bob':45,'matt':67}
names=list(student.keys())
marks=list(student.values())
plt.barh(names,marks,color='green')
plt.show()