from geometry import Point2D, circle
from random import randint

c: circle = circle(Point2D(randint(0, 255), randint(0, 255)), 5)
print(c.area())
print(c.length())
print(c.radius)
print(c)