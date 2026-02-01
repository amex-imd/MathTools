import math # Temporary

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

def is_prime(val: int) -> bool:
    if val < 0: return False
    if val == 2: return True
    if val == 0 or val == 1: return False
    if val % 2 == 0: return False
    for i in range(3, int(math.sqrt(val)) + 1, 2):
        if val % i == 0:
            return False
    return True

def Eratosthenes_sieve(num: int) -> list:
    primes: list = [True] * num
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(num)) + 1):
        if primes[i]:
            j = i * i
            while j < num:
                primes[j] = False
                j += i
    return [i for i in range(2, num) if primes[i]]