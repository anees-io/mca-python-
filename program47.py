
import graphics.circle
import graphics.rectangle

print("Rectangle")
print("Area:", graphics.rectangle.area(10, 5))
print("Perimeter:", graphics.rectangle.perimeter(10, 5))

print("\nCircle")
print("Area:", graphics.circle.area(7))  # Replaced 'y' with 7
print("Perimeter:", graphics.circle.perimeter(7))

# Importing specific functions from the sub-package
from graphics.threeD_graphics.cuboid import area, perimeter

print("\nCuboid")
print("Surface Area:", area(10, 5, 4))
print("Perimeter:", perimeter(10, 5, 4))

# Importing all functions from sphere using *
from graphics.threeD_graphics.sphere import *

print("\nSphere")
print("Surface Area:", area(7))
print("Perimeter:", perimeter(7))


