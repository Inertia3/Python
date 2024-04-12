from scipy.optimize import minimize

def f(x):
    return x[0]**2 + x[1]**2

def eq_const(x):
    return x[0] + x[1] - 1

def ineq_const(x):
    return x[0] - x[1]

guess = [0.5, 0.5]

constraints = [{"type": "eq", "fun": eq_const}, {"type": "ineq", "fun": ineq_const}]

res = minimize(f, guess, constraints=constraints)
print("Optimal value:", res.fun)
print("Optimal result:", res.x)


# Example- A factory manufactures 2 type of goods Goods A and B based on workforce 
# and raw material
# Good A - requires 3 hours of work force and 2 units of raw material

# Good B - requires 4 hour of workforce and 3 units of raw material

# The factory has 150 hours of workforce and 120 unit of raw material 
# Profit earned form each unit is 
# Good A = 20
# Good B = 25

# What is the best production plan to maximize total profit