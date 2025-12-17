import math

# Define the function f(x)
def f(x):
    return x**2 - 4  # Example function (x^2 - 4)

# Bisection Method
a = 1
b = 3
x = 0

for i in range(1000):
    x1 = (a + b) / 2  # Midpoint
    if abs(f(x1)) <= 0.0001:  # Convergence condition
        print(f"Converged at iteration {i}")
        break
    if f(a) * f(x1) < 0:
        b = x1
    else:
        a = x1

print("Root:", x1)