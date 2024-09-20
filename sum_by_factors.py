import math
from functools import lru_cache


@lru_cache(maxsize=None)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def sum_for_list(lst):
    primes = set()
    final = []

    for i in lst:
        abs_i = abs(i)
        if abs_i < 2:
            continue
        for j in range(2, abs_i + 1):
            if is_prime(j) and abs_i % j == 0:
                primes.add(j)

    for prime in sorted(primes):
        sum_multiples = sum(num for num in lst if num % prime == 0)
        final.append([prime, sum_multiples])

    return final


result = sum_for_list([105790, -413270, -875703, -862781, -562170, 865932, -758701, -178261, -658650, -793782,
                       538420, -332889, -813922, -906678])
print(result)


# TODO : TOO FKING SLOW
