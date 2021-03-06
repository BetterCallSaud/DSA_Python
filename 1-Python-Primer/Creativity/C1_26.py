"""
๐ Author: Saud Hashmi
๐งท Problem Index: C-1.26
๐ฉ Problem Statement:
     Write a short program that takes as input three integers, a, b, and c, from
    the console and determines if they can be used in a correct arithmetic
    formula (in the given order), like โa+b = c,โ โa = bโc,โ or โa โ b = c.โ
"""

def op(a,b,c):
    if a+b==c or b+c==a or c+a==b: return True
    elif b-c==a or a-b==c or c-a==b or c-b==a or b-a==c or a-c==b: return True
    elif a*b==c or b*c==a or c*a==a: return True
    return False

print(op(2,5,10))
print(op(2,5,7))
print(op(2,-5,-3))
print(op(-2,5,-10))
print(op(-2,5,10))