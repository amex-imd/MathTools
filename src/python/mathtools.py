import math # Temporary

__EPSILON: float = 1e-12
__ROMAN_TABLE: dict = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

def is_equal(num1: float, num2: float) -> bool:
    return abs(num1 - num2) <= __EPSILON

def is_zero(num: float) -> bool:
    return is_equal(num, 0)

def Newton_Raphson_root(num: float, pow: int, approx: float = 1.0) -> tuple[float, int]:
    if pow <= 0: raise ValueError(f'The argument \'{pow}\' must be greater than 0')
    if pow % 2 == 0 and num < 0: raise ValueError(f'It is impossible to take a root with the power \'{pow}\' of the negative number \'{num}\'')

    prev: float = approx
    curr: float = ((pow - 1) * prev + num/(prev ** (pow - 1))) / pow
    iter_num: int = 1
    while abs(prev - curr) > __EPSILON:
        prev = curr
        if is_zero(prev): raise ArithmeticError('Division by 0 is prohibited')

        curr = ((pow - 1) * prev + num/(prev ** (pow - 1))) / pow
        iter_num += 1
    return (curr, iter_num)

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

def number_primes(num: int) -> int:
    return len(Eratosthenes_sieve(num))

def all_divisors(num: int) -> list:
    res: list = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            res.append(i)
            if num // i != i: # Checking for duplicates
                res.append(num // i)
    return res

def number_divisors(num: int) -> list:
    return len(all_divisors(num))

def sign(val: float) -> int:
    if val < -__EPSILON: return -1
    if val > __EPSILON: return +1
    return 0

def abs(val: float) -> float:
    return val * sign(val)

def roman_to_integer(line: str) -> int:
    if not line: raise ValueError('The argument \'line\' must be not empty')

    res: int = 0
    L: int = len(line)

    for i in range(0, L-1):
        if __ROMAN_TABLE[line[i+1]] > __ROMAN_TABLE[line[i]]:
            res -= __ROMAN_TABLE[line[i]]
        else: res += __ROMAN_TABLE[line[i]]
    return res + __ROMAN_TABLE[line[-1]]