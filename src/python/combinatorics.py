from typing import List
from math import log2, ceil

def factorial(number: int):
    if number == 0 or number == 1: return 1
    res: int = 1
    for i in range(2, number + 1):
        res *= i
    return res

def PascalTriangle(rows: int) -> List[List[int]]:
    res: List[List[int]] = []
    for i in range(rows):
        tmp: List[int] = [1] * (i+1)
        for j in range(1, i-1):
            tmp[j] = res[i][j-1] + res[i][j]
        res.append(tmp)
    return res

def PasalTriangleRow(rowIndex: int) -> List[int]:
    res: List[int] = [1]
    for i in range(rowIndex):
        nextElem = res[i] * (rowIndex - i) // (i+1)
        res.append(nextElem)
    return res

def combinatorialCoefficient(n: int, k: int):
    if k == 0 or k == n: return 1
    if k == 1: return n
    if k > n // 2: k = n-k # for optimization

    res: int = 1
    for i in range(1, k+1):
        res *= (n-i+1) // i

    return res

def poorPigs(buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    # res: int = 0
    # states: int = minutesToTest // minutesToDie
    # while(states ** res < buckets):
    # pigs += 1
    return ceil(log2(buckets) / log2(minutesToTest // minutesToDie + 1)) # log doesn't work because of error

def JosephusRecursiveProblem(n: int, k: int):
    if n == 1: return 0
    return (JosephusRecursiveProblem(n - 1, k) + k) % n

def JosephusIterativeProblem(n: int, k: int):
    res: int = 0
    for i in range(2, n+1): res = (res + k) % i
    return res

def arithmeticProgression(start: float, step: float):
    curr: float = start
    while True:
        yield curr
        curr += step

def geometricProgression(start: float, factor: float):
    curr: float = start
    while True:
        yield curr
        curr *= factor

def HarmonicProgression(start: float, step: float):
    ap = arithmeticProgression(start, step)
    while True:
        yield 1 / next(ap)

def FibonacciNumbers():
    prev: float = 0
    curr: float = 1
    while True:
        yield prev
        (prev, curr) = (curr, prev + curr)

def LukeNumbers():
    prev: float = 2
    curr: float = 1
    while True:
        yield prev
        (prev, curr) = (curr, prev + curr)

def NarayanaAlgorithm(perm): # Next permutation
    j: int = -1
    for i in range(len(perm) - 1):
        if perm[i] < perm[i+1]:
            j = i
    if j < 0: return False
    l: int = j+1
    for i in range(l, len(perm)):
        if perm[i] > perm[j]:
            l = i

    (perm[j], perm[l]) = (perm[l], perm[j])
    perm[j+1:] = reversed(perm[j+1:])
    return True
    
    