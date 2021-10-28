import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
y2 = np.cos(x)

for i in range(100):
    plt.plot(x+ 2*np.pi/100 * i, y)
plt.show()
