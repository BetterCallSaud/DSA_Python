"""
📝 Author: Saud Hashmi
🧷 Problem Index: C-1.22
🚩 Problem Statement:
     Write a short Python program that takes two arrays a and b of length n
    storing int values, and returns the dot product of a and b. That is, it returns
    an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n-1.
"""

a = [1,2,3,4,5]
b = [2,3,4,5,6]
assert len(a) == len(b)

dot = lambda a,b : sum([a[i]*b[i] for i in range(len(a))])
print(dot(a,b))