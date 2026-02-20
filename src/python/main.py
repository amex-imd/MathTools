from geometry2D import point2D, circle, ellipse, square
from random import randint

from combinatorics import arithmeticProgression

def main() -> None:
    a = arithmeticProgression(5, 0.01)
    for x in range(3):
        print(next(a))

main()