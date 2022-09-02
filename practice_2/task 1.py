import math
try:
    r, h = eval(input("Input radius and height of the cylinder (splitting them by coma):"))
    v = round(h * math.pi * r ** 2, 3)
    a = round(h * 2 * math.pi * r + 2 * math.pi * r ** 2, 3)
    print(f'Volume: {v}, Area: {a}')
except:
    print("Are you stupid?")


