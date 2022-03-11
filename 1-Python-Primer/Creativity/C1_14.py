"""
📝 Author: Saud Hashmi
🧷 Problem Index: C-1.14
🚩 Problem Statement:
    Write a short Python function that takes a sequence of integer values and
    determines if there is a distinct pair of numbers in the sequence whose
    product is odd.
"""

def distinct_pair(seq):
    for i in seq:
        for j in seq:
            if i != j and (i*j)%2 == 1:
                yield((i,j))
    
seq = [1,2,3,4,5]
gen = distinct_pair(seq)
for g in gen:
    print(g)