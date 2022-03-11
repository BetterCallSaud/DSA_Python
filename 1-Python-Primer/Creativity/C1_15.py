"""
📝 Author: Saud Hashmi
🧷 Problem Index: C-1.15
🚩 Problem Statement:
    Write a Python function that takes a sequence of numbers and determines
    if all the numbers are different from each other (that is, they are distinct).
"""

def distinct(seq):
    num_set = set()
    for e in seq:
        if e in num_set: return False
        elif e not in num_set: num_set.add(e)
    return True
    
print(distinct([1,2,3,4,5]))
print(distinct([1,2,3,4,5,5]))