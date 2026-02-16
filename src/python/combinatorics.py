

def factorial(number: int):
    if number == 0 or number == 1: return 1
    res: int = 1
    for i in range(2, number + 1):
        res *= i
    return res

