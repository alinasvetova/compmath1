import math

# Define the function g(x) for fixed point iteration
def g(x):
    return math.cos(x)  # Example fixed point function

# Initial guess
x = 0

for i in range(1000):
    x1 = g(x)  # Apply fixed-point formula
    if abs(x1 - x) <= 0.0001:  # Convergence condition
        print(f"Converged at iteration {i}")
        break
    x = x1

print("Root:", x1)