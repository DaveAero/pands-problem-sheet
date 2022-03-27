# plottask.py
# This program is used to graph x being raised to different powers
# author: David Burke

import matplotlib.pyplot as plt
import numpy as np

xSmooth = np.array(np.arange(0,4.05,0.05))

# f(x) = x
f = xSmooth
plt.plot(xSmooth, f, label = "x", color='r')

# g(x) = x**2
g = xSmooth**2
plt.plot(xSmooth, g, label = "x**2", color='g')

# h(x) = x**3
h = xSmooth**3
plt.plot(xSmooth, h, label = "x**3", color='b')
yMax = int(max(h))

plt.title("X to increasing powers", size = 20, color = 'dimgrey')

plt.xticks([0,1,2,3,4])
plt.yticks(range(0,yMax+4,4))

plt.xlabel("X-axis", size = 15, color = 'slategray')
plt.ylabel("Y-axis", size = 15, color = 'slategray')

plt.grid(axis = 'y')

plt.legend()
plt.show()