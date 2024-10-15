import math

radius = int(input("Enter the radius of a cylinder in cm\n"))
depth = int(input("Enter the depth of a cylinder in cm\n"))

print(f'{str(round((float(float(math.pi * (radius**2)) * float(depth))), 3))}cm³ (3 d.p)')