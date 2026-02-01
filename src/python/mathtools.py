__EPSILON: float = 1e-12

def reverse(val: int) -> int:
    res: int = 0
    sign: int = -1 if val < 0 else 1
    x *= sign
    while x > 0:
        res = res * 10 + x % 10
        x //= 10
    res *= sign
    return res