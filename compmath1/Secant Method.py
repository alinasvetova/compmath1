import math

# Define the function f(x)
def f(x):
    return x**2 - 4  # Example function (x^2 - 4)

# Initial guesses
x0 = 1
x1 = 3

for i in range(1000):
    if f(x1) - f(x0) == 0:  # Avoid division by zero
        print("Error: Division by zero!")
        break
    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))  # Secant formula
    if abs(x2 - x1) <= 0.0001:  # Convergence condition
        print(f"Converged at iteration {i}")
        break
    x0 = x1
    x1 = x2

print("Root:", x2)