"""
📝 Author: Saud Hashmi
🧷 Problem Index: P-1.35
🚩 Problem Statement:
    The birthday paradox says that the probability that two people in a room
    will have the same birthday is more than half, provided n, the number of
    people in the room, is more than 23. This property is not really a paradox,
    but many people find it surprising. Design a Python program that can test
    this paradox by a series of experiments on randomly generated birthdays,
    which test this paradox for n = 5,10,15,20,...,100.
"""

from random import choice
from collections import Counter

def generate_birthdays(n):
    months = [m for m in range(1,13)]
    days = [d for d in range(1,31)]
    birthdays = []

    for _ in range(n):
        m = choice(months)
        if m == 2: d = choice(days[:28])
        elif m in [1,3,5,7,10,12]: d = choice(days)
        else: d = choice(days[:30])
        birthdays.append('{}.{}'.format(d,m))

    ctr = Counter(birthdays)
    q = 0
    for v in ctr.values():
        if v>=2: q += 1
    return f'n={n}, p={q}/{n}'
    

if __name__=="__main__":
    nums = [x for x in range(5,101,5)]
    for num in nums:
        print(generate_birthdays(num), end=' | ')