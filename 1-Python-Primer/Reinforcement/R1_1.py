"""
๐ Author: Saud Hashmi
๐งท Problem Index: R-1.1
๐ฉ Problem Statement:
    Write a short Python function, is_multiple(n, m), that takes two integer
    values and returns True if n is a multiple of m, that is, n = mi for some
    integer i, and False otherwise.
"""

def is_multiple(n,m):
    if n%m == 0:
        return True
    return False

# If no output, then the code works. โ
if __name__=="__main__":
    assert (is_multiple(12,4) == True)
    assert (is_multiple(12,8) == False)
    assert (is_multiple(32,16) == True)
    assert (is_multiple(32,10) == False)