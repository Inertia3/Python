from scipy.optimize import minimize

def f(x):
    return -(x**2) - 4*x + 5

x0 = 0
res = minimize(f, x0, method = "Nelder-Mead")

maxvalue = -res.fun

maxx = res.x

print(f"The maxvalue is {maxvalue} at x = {maxx}")