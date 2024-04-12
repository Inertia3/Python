
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

def simpson(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    i = h / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
    return i

a = 0
b = 2
n = 10

result = simpson(f, a, b, n)
print('When n =', n, 'then the result is =', result)

x_values = np.linspace(a, b, n + 1)  
plt.plot(x_values, f(x_values), label='x^2 function')
# plt.fill_between(x_values, f(x_values), alpha=0.2)  # Improvement

plt.legend()
plt.show()
