from typing import Callable, List
from functools import reduce

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
__SPECIAL_ROMAN_TABLE: dict = {
    'I' : 1,
    'IV' : 4,
    'V' : 5,
    'IX' : 9,
    'X' : 10,
    'XL' : 40,
    'L' : 50,
    'XC' : 90,
    'C' : 100,
    'CD' : 400,
    'D' : 500,
    'CM' : 900,
    'M' : 1000
}

def __GCDHelper(val1: int, val2: int) -> int:
        if val1 == 0 and val2 == 0: raise ValueError('The arguments \'val1\' and \'val2\' equal 0')
        while val2 != 0:
            val1, val2 = val2, val1 % val2
        return abs(val1)

def sign(val: float) -> int:
    if val < -__EPSILON: return -1
    if val > __EPSILON: return +1
    return 0

def abs(val: float) -> float:
    return val * sign(val)

def is_equal(val1: float, val2: float) -> bool:
    return abs(val1 - val2) <= __EPSILON

def is_zero(val: float) -> bool:
    return is_equal(val, 0)

def is_even(val: int) -> bool:
    return val % 2 == 0
def is_odd(val: int) -> bool:
    return not is_even(val)

def Newton_Raphson_root(num: float, pow: int, approx: float = 1.0) -> tuple[float, int]:
    if pow <= 0: raise ValueError('The argument \'pow\' must be greater than 0')
    if is_even(pow) and num < -__EPSILON: raise ValueError('It is impossible to take a root with the power \'pow\' of the negative number \'num\'')
    if is_zero(num): return 0

    prev: float = approx
    curr: float = ((pow - 1) * prev + num/(prev ** (pow - 1))) / pow
    iter_num: int = 1

    while abs(prev - curr) > __EPSILON:
        prev = curr
        if is_zero(prev): raise ArithmeticError('Division by 0 is prohibited')

        curr = ((pow - 1) * prev + num/(prev ** (pow - 1))) / pow
        iter_num += 1
    return (curr, iter_num)

def power(num: float, pow: int) -> float:
    if pow == 0:
        if is_zero(num): raise ValueError('The expression \'0^0\' is not defined')
        else: return 1
    if pow < 0: return 1 / power(num, -pow)
    if pow == 1: return num
    
    res: float = 1
    while(pow > 0):
        if is_even(pow):
            num *= num
            pow //= 2
        else:
            res *= num
            pow -= 1
    return res

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
    if is_even(val): return False

    for i in range(3, int(Newton_Raphson_root(val, 2, val / 2)[0]) + 1, 2):
        if val % i == 0:
            return False
    return True

def Eratosthenes_sieve(num: int) -> list[int]:
    primes: list = [True] * num
    primes[0] = primes[1] = False
    for i in range(2, int(Newton_Raphson_root(num, 2, num / 2)[0]) + 1):
        if primes[i]:
            j = i * i
            while j < num:
                primes[j] = False
                j += i
    return [i for i in range(2, num) if primes[i]]

def number_primes(num: int) -> int:
    return len(Eratosthenes_sieve(num))

def all_divisors(val: int) -> list[int]:
    res: list = []
    for i in range(1, int(Newton_Raphson_root(val, 2, val / 2)[0]) + 1):
        if val % i == 0:
            res.append(i)
            if val // i != i: # Checking for duplicates
                res.append(val // i)
    return res

def number_divisors(val: int) -> list:
    return len(all_divisors(val))

def roman_to_integer(line: str) -> int:
    if not line: raise ValueError('The argument \'line\' must be not empty')

    res: int = 0
    L: int = len(line)

    for i in range(0, L-1):
        if __ROMAN_TABLE[line[i+1]] > __ROMAN_TABLE[line[i]]:
            res -= __ROMAN_TABLE[line[i]]
        else: res += __ROMAN_TABLE[line[i]]
    return res + __ROMAN_TABLE[line[-1]]

def integer_to_roman(val: int) -> str:
    if val <= 0: raise ValueError('The argument \'val\' must be greater than 0')

    res: str = ''
    for key, num in __SPECIAL_ROMAN_TABLE.items().__reversed__():
        if val == 0: break
        count = val // num
        res += key * count
        val -= count * num
    return res

def integer_to_english(val: int) -> str:
    def helper(part: int) -> str:
        res: list[str] = []
        if part >= 100:
            res.append(digits[part // 100] + ' ' + rangs[0])
            part %= 100
        if part >= 20:
            if part % 10 == 0: res.append(tens2[part // 10])
            else: res.append(tens2[part // 10] + ' ' + digits[part % 10])
        elif part >= 10: res.append(tens1[part % 10])
        elif part > 0: res.append(digits[part])
        return ' '.join(res)

    if val < 0: raise ValueError('The argument \'val\' must not be lesser than 0')
    if val == 0: return 'Zero'

    digits: list[str] = ['', 'One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    tens1: list[str] = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
    tens2: list[str] = ['', '', 'Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
    rangs: list[str] = ['Hunred', 'Thousand', 'Million', 'Billion']
    res: list[str] = []
    rang: int = 0

    while val > 0:
        part: int = val % 1000
        tmp: str = helper(part)
        if tmp:
            if rang > 0: res.append(rangs[rang]) # ignoring the case of zero
            res.append(tmp)
        val //= 1000
        rang += 1
    return ' '.join(reversed(res))

def interval_halving_method(f: Callable, beg: float, end: float) -> tuple[float, int]:
    if f(beg) * f(end) >= 0: raise ValueError('The function \'f\' must have values with different signs at the ends of the interval \'[beg; end]\'')
    mid: float = 0
    iter_num: int = 0

    while abs(beg - end) > __EPSILON:
        mid = (beg + end) / 2
        if f(beg) * f(mid) < 0:
            end = mid
        elif f(mid) * f(end) < 0:
            beg = mid
        iter_num += 1
    return (mid, iter_num)

def clamp(val: float, min: float, max: float):
    if val < min - __EPSILON: return min
    if val > max + __EPSILON: return max
    return val

def GCD(*nums) -> int:
    

    if len(nums) == 0: raise ValueError('The argument \'nums\' is empty')
    
    res: int = nums[0]
    for i in range(1, len(nums)):
        res = __GCDHelper(res, nums[i])
        if res == 1: break
    return res

def LCM(*nums) -> int:
    if len(nums) == 0: raise ValueError('The argument \'nums\' is empty')

    res: int = nums[0]
    for i in range(1, len(nums)):
        res = abs(res * nums[i]) // __GCDHelper(res, nums[i])

    return res
    
def isRelativelyPrime(*nums) -> bool:
    return GCD(*nums) == 1

def normalize(data: List[float]):
    minValue, maxValue = min(data), max(data)
    if minValue == maxValue: return [0.5 for _ in data]
    return [(x - minValue) / (maxValue - minValue) for x in data] # Formula

def arithmeticMean(data: List[float]):
    S = sum(data)
    N = len(data)
    return S / N

def geometricMean(data: List[float]):
    P = reduce(lambda x, y: x * y, data, 1)
    N = len(data)
    return Newton_Raphson_root(P, N)

def mean(data: List[float]):
    return (arithmeticMean(data), geometricMean(data))