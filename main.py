import numpy as np 
import matplotlib.pyplot as plt

<<<<<<< HEAD
x = np.linspace(0, 2 * np.pi, 1000)
=======
x = np.linspace(0, 2 * np.pi, 10000000)
>>>>>>> test
y = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y)
plt.plot(x, y2)
plt.show()
