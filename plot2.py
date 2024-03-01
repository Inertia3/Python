import matplotlib.pyplot as mp
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([10,20,30,40,50])

mp.scatter(x,y)

mp.title("Scatter Graph")
mp.xlabel("X-axis")
mp.ylabel("Y-axis")

mp.show()