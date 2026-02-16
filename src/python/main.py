from geometry2D import point2D, circle, ellipse, square
from random import randint

lst: list[point2D] = [circle(point2D(randint(-100, 100), randint(-100, 100)), 10) for _ in range(10)]
for x in lst: print(x)
print(lst[0].dimenshion)
print(lst[0].move(1, 2))
print(lst[0])

s: square = square(point2D(2, 5), 2)
print(s)
print(s.area())
print(s.perimeter())