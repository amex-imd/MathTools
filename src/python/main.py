from geometry2D import point2D, circle, ellipse, square
from random import randint

from combinatorics import FibonacciNumbers

def main() -> None:
    a = FibonacciNumbers()
    for x in range(10):
        print(next(a))

    a.close()

main()