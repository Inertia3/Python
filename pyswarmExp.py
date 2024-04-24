from pyswarm import pso
import numpy as np

def f(x):
    return np.sum(x**2)

lowerbound = [-5, -5, -5]  # Lower bounds for variables
upperbound = [5, 5, 5]     # Upper bounds for variables

bestsol, bestval = pso(f, lowerbound, upperbound)

print("Optimal Solution:", bestsol)
print("Optimal Value:", bestval)
