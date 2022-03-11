"""
📝 Author: Saud Hashmi
🧷 Problem Index: R-1.4
🚩 Problem Statement:
    Write a short Python function that takes a positive integer n and returns
    the sum of the squares of all the positive integers smaller than n.
"""

def less_than_sum(n):
    return n*(n+1)/2 - n

# If no output, then the code works. ✅
if __name__=="__main__":
    assert (less_than_sum(3) == 3)
    assert (less_than_sum(6) == 15)
    assert (less_than_sum(10) == 45)