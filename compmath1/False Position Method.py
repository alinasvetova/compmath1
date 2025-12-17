import math

# Define the function f(x)
def f(x):
    return x**2 - 4  # Example function (x^2 - 4)

# Initial guesses
a = 1
b = 3

for i in range(1000):
    c = b - f(b) * (b - a) / (f(b) - f(a))  # False position formula
    if abs(f(c)) <= 0.0001:  # Convergence condition
        print(f"Converged at iteration {i}")
        break
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

print("Root:", c)