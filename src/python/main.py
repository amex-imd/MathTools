from geometry import point2D, circle, ellipse
from random import randint

e: ellipse = ellipse(point2D(0, 0), 5, 2)
print(e)
print(e.perimeter())
print(e.area())
print(e.eccentricity())
print(e.directrix())
print(e.focalDistance())