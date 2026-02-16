from typing import List

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