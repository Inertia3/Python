# A company produces two products, Product X and Product Y using 
# two types of resources: Labour and Material Each unit of product X 
# requires 2 hours of labour and 1 unit of material, whilw each unit 
# of Product Y requires 3 hours of labour and 2 unit of material. 
# The compant has 100 hours of laboura and 80 units of material available.
#  The profit earned from each unit of Product X is 10 and from 
# product Y is 15 
#  Maximize the total profit.
# Constraints: Limited Availibility of Labour = 100 hours
#              Limited availibility of Material = 80 units 
from scipy.optimize import minimize


def total_profit(x):
    return -(10*x[0] + 15*x[1])  # Negative because we are maximizing profit

# Constraints:
# 1. Labour constraint: 2x + 3y <= 100
def labour_constraint(x):
    return 100 - (2*x[0] + 3*x[1])

# 2. Material constraint: x + 2y <= 80
def material_constraint(x):
    return 80 - (x[0] + 2*x[1])

guess = [0, 0]

constraints = [
    {"type": "ineq", "fun": labour_constraint},
    {"type": "ineq", "fun": material_constraint}
]
# Perform the optimization
res = minimize(total_profit, guess, constraints=constraints)

# Print the optimal result
print("Optimal total profit:", -res.fun)  # Negate the result to get the actual profit
print("Optimal number of units for Product X and Y:", res.x)
