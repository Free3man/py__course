import math

x, u, o = eval(input("Input x, mu, sigma (in that order and dividing by commas): "))
f = round(1 / math.sqrt(2 * math.pi * o ** 2) * math.pow(math.e, -((x - u) ** 2 / (2 * o ** 2))), 10)
print(f"Result: {f}")
