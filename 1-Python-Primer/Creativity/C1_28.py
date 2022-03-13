"""
📝 Author: Saud Hashmi
🧷 Problem Index: C-1.28
🚩 Problem Statement:
    The p-norm of a vector v = (v1,v2,...,vn) in n-dimensional space is defined.
    For the special case of p = 2, this results in the traditional Euclidean
    norm, which represents the length of the vector. For example, the Euclidean norm of a two-dimensional vector with coordinates (4,3) has a
    Euclidean norm of √
    42 +32 = √16+9 = √
    25 = 5. Give an implementation of a function named norm such that norm(v, p) returns the p-norm
    value of v and norm(v) returns the Euclidean norm of v. You may assume
    that v is a list of number
"""

def norm(v, p):
    inner_sum = sum([v_i**p for v_i in v])
    return round(inner_sum**(1/p), 3)

v = [1, 2, 3, 4]
print(norm(v,1))
print(norm(v,2))
print(norm(v,3))