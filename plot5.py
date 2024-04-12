from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([5, 6, 7, 8, 9, 2])

xnew = np.linspace(np.min(x), np.max(x), 50)  # Corrected spelling of linspace
f = interpolate.interp1d(x, y)

plt.plot(xnew, f(xnew), "red", label="linear interpolation")
plt.scatter(x, y, label="original data")
plt.legend()
plt.show()


