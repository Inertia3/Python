from scipy.optimize import minimize

# Define the objective function
def total_time(tasks):
    task_times = [3, 5, 4]  # Time required for each task
    return sum(task_times[i] * tasks[i] for i in range(len(tasks)))

# Define the resource constraint function
def resource_constraint(tasks):
    task_resources = [[2, 3, 1]]  # Resource usage for each task
    total_resources = 10  # Total available resources
    return total_resources - sum(task_resources[i][j] * tasks[j] for i in range(len(task_resources)) for j in range(len(tasks)))

# Initial guess
x0 = [0, 0, 0]  # Initial guess for the number of days allocated to each task

# Define constraints
constraints = ({'type': 'eq', 'fun': resource_constraint})

# Minimize the total time subject to the resource constraint
res = minimize(total_time, x0, constraints=constraints, method='SLSQP')

# Extract the minimum value and the corresponding allocation of days to each task
min_time = res.fun
allocation = res.x

# Print the results
print("Optimal total time required:", min_time)
print("Optimal allocation of days to each task:", allocation)