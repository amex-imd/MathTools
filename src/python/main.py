from geometry2D import point2D, circle, ellipse, square
from random import randint

from combinatorics import HarmonicProgression

def main() -> None:
    a = HarmonicProgression(1, 1)
    for x in range(10):
        print(next(a))

    a.close()

main()