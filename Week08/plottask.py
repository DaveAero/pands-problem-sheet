# plottask.py
# This program is used to graph x being raised to different powers
# author: David Burke

# importing libarys
import matplotlib.pyplot as plt
import numpy as np

# using numpy to create an array of data points, the more points the smoother the curve
# 100 points in the array
dataPoints = np.array(np.arange(0,4.04,0.04))
x = dataPoints

# f(x) = x
f = dataPoints
plt.plot(x, f, label = "x", color='r')

# g(x) = x**2
g = dataPoints**2
plt.plot(x, g, label = "x**2", color='g')

# h(x) = x**3
h = dataPoints**3
plt.plot(x, h, label = "x**3", color='b')

#finding the max y-axis value to use in the y-axis ticks
yMax = int(max(h))

# adding title to the graph
plt.title("X to increasing powers", size = 20, color = 'dimgrey')

#adding ticks to each axis
plt.xticks([0,1,2,3,4])
plt.yticks(range(0,yMax+4,4))

# adding labes to each axis                     *** Ref 10 
plt.xlabel("X-axis", size = 15, color = 'slategray')
plt.ylabel("Y-axis", size = 15, color = 'slategray')

# adding grid to just the y-axis, as this has a much larger range
plt.grid(axis = 'y')

# adding a legend to identify each line
plt.legend()

# printing final graph
plt.show()