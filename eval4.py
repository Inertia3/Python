# A project manager needs to schedule three task: task 1, taskk 2, task 3.
# Each task requires sa certain amount of time to complete and consumes specific 
# amount of resources. THe manager wants to minimize the total time required to
# complete all the task while ensuring that resouce usage does not exceed 
# the availability capacity. Minimize the total time required to complete all tasks.

# Task details:
# Task 1: Requires 2 unit of resource and takes 3 days to complete 
# Task 2: Requires 3 unit of resource and takes 5 days to complete 
# Task 3: Requires 1 unit of resource and takes 4 days to complete

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


