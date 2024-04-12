from scipy.optimize import minimize

def f(x):
    return x[0]**2 + x[1]**2

def constr(x):
    return x[0] + x[1] - 5

def lag(x, lambdac):
    return f(x) + lambdac * constr(x)

x0 = [1, 2]

constraint = [{"type": "eq", "fun": constr}]

lambdac = 1.0

res = minimize(lambda x: lag(x, lambdac=lambdac), x0, constraints=constraint)

print("Optimal root:", res.x)
print("Optimal value:", res.fun)
print("Lagrange Multiplier:", res.fun - f(res.x))
