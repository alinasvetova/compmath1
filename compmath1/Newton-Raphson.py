def f(x):
    #     return math.exp(x) - x ** 2
    return x ** 2 + 3 * x + 2


def df(x):
    #     return math.exp(x) - 2 * x
    return 2 * x + 3


x = 0

for i in range(1000):
    x1 = x
    x = x - f(x) / df(x)
    if abs(x - x1) <= 0.0001:
        print(i)
        break
print(x)