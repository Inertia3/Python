from scipy.optimize import minimize

def f(x):
    return (x**2) - 4*x + 5

x0 = 0
res = minimize(f, x0, method = "Nelder-Mead")

minvalue = res.fun

minx = res.x

print(f"The minvalue is {minvalue} at x = {minx}")