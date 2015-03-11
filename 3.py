#!/usr/bin/env python

from math import sqrt

primes = [2, 3, 5, 7]

def factor(n):
    facts = []
    n_sqrt = int(sqrt(n))
    i = 2
    while n > 1:
            if not n % i:
                facts.append(i)
                n /= i
                print n
            else:
                i += 1
    return facts

def is_prime(n):
    n_sqrt = int(sqrt(n))
    for p in primes:
        if p < n_sqrt:
            if n % p == 0:
                return False
        else:
            break
    for i in range(p, n_sqrt + 1):
        if n % i == 0:
            primes.append(i)
    return True

print factor(600851475143)
