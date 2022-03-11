"""
📝 Author: Saud Hashmi
🧷 Problem Index: R-1.6
🚩 Problem Statement:
    Write a short Python function that takes a positive integer n and returns
    the sum of the squares of all the odd positive integers smaller than n.
"""

def odd_less_than_sum(n):
    local_sum = 0
    for i in range(1,n,2):
        local_sum += i
    return local_sum

# If no output, then the code works. ✅
if __name__=="__main__":
    assert (odd_less_than_sum(3) == 1)
    assert (odd_less_than_sum(6) == 9)
    assert (odd_less_than_sum(10) == 25)