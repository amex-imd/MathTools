from geometry import point2D, circle, ellipse, square
from random import randint

e: square = square(point2D(0, 0), 5)
print(e)
print(e.perimeter())
print(e.area())
print(e.vertices())
print(e.diagonal())