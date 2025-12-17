import math


# Define the function f(x)
def f(x):
    return math.cos(x) - x  # Example function (cos(x) - x)


# Initial guesses
x0 = 0.5
x1 = 0.7
x2 = 0.9

for i in range(1000):
    # Coefficients of the quadratic equation
    h1 = x1 - x0
    h2 = x2 - x1
    delta1 = (f(x1) - f(x0)) / h1
    delta2 = (f(x2) - f(x1)) / h2
    a = (delta2 - delta1) / (h2 + h1)
    b = a * h2 + delta2
    c = f(x2)

    # Solving the quadratic equation
    D = b ** 2 - 4 * a * c
    if D < 0:
        print("No real root found.")
        break
    sqrt_D = math.sqrt(D)
    if abs(b + sqrt_D) > abs(b - sqrt_D):
        x3 = x2 - 2 * c / (b + sqrt_D)
    else:
        x3 = x2 - 2 * c / (b - sqrt_D)

    if abs(x3 - x2) <= 0.0001:  # Convergence condition
        print(f"Converged at iteration {i}")
        break

    x0 = x1
    x1 = x2
    x2 = x3

print("Root:", x3)