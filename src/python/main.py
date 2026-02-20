from geometry2D import point2D, circle, ellipse, square
from random import randint

from combinatorics import geometricProgression

def main() -> None:
    a = geometricProgression(5,0.5)
    for x in range(3):
        print(next(a))

    a.close()

main()