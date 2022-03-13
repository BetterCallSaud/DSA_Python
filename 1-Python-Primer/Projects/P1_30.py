"""
📝 Author: Saud Hashmi
🧷 Problem Index: P-1.30
🚩 Problem Statement:
    Write a Python program that can take a positive integer greater than 2 as
    input and write out the number of times one must repeatedly divide this
    number by 2 before getting a value less than 2.
"""

def count_divs(n):
    assert n > 2
    ctr = 0
    while (n >= 2):
        ctr += 1
        n = n//2
    return ctr

n = int(input('Enter a number greater than 2: '))
print(count_divs(n))