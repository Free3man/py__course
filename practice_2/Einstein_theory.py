from scipy import constants
import math
m, v = eval(input("Input mass and velocity of the object (dividing by commas): "))
m_r = m / math.sqrt(1 - v ** 2 / constants.c ** 2)
E = m_r * constants.c ** 2
print(f"Relativistic mass: {E}")
