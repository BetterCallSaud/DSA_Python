"""
๐ Author: Saud Hashmi
๐งท Problem Index: C-1.27
๐ฉ Problem Statement:
    In Section 1.8, we provided three different implementations of a generator
    that computes factors of a given integer. The third of those implementations, from page 41, was the most efficient, but we noted that it did not
    yield the factors in increasing order. Modify the generator so that it reports
    factors in increasing order, while maintaining its general performance advantages.
"""

def factors(n): # generator that computes factors
    k = 1
    second_half_factors = []
    while k*k < n: # while k < sqrt(n)
        if n % k == 0:
            yield k
            second_half_factors.append(n//k)
        k += 1
    if k * k == n: # special case if n is perfect square
        yield k
    for factor in reversed(second_half_factors):
        yield factor

gen = factors(36)
for g in gen:
    print(g, end=',')