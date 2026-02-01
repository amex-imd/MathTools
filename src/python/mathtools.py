__EPSILON: float = 1e-12

def reverse(val: int) -> int:
    res: int = 0
    sign: int = -1 if val < 0 else 1
    val *= sign
    while val > 0:
        res = res * 10 + val % 10
        val //= 10
    res *= sign
    return res

def is_palindrome(val: int) -> bool:
    if val < 0: return False
    if val < 10: return True
    if val % 10 == 0: return False

    half: int = 0
    while val > half:
        half = half * 10 + val % 10
        val //= 10
    return val == half or val == half // 10

def number_digits(val: int) -> int:
    res: int = 0
    sign: int = -1 if val < 0 else 1
    val *= sign
    while val > 0:
        res += 1
        val //= 10
    return res