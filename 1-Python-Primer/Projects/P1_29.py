"""
📝 Author: Saud Hashmi
🧷 Problem Index: P-1.29
🚩 Problem Statement:
    Write a Python program that outputs all possible strings formed by using
    the characters c , a , t , d , o , and g exactly once.
"""

from itertools import permutations

chars = ['c', 'a', 't', 'd', 'o', 'g']

for permutation in permutations(chars):
    print(''.join(permutation), end=',')