import math

def get_prime_factors(n):
    factors = []
    i = 2
    while i ** 2 <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

get_prime_factors(12)