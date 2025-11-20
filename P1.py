import math

r = 42
angle = 60


length = (angle / 360) * 2 * math.pi * r


side = length / 4


area = side * side

print("Length of wire =", round(length, 2))
print("Side of square =", round(side, 2))
print("Area of square =", round(area, 2))
