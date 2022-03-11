"""
📝 Author: Saud Hashmi
🧷 Problem Index: R-1.5
🚩 Problem Statement:
    Give a single command that computes the sum from Exercise R-1.4, relying on Python's comprehension syntax and the built-in sum function.
"""

def less_than_sum(n):
    less_sum = sum([i for i in range(1,n)])
    return less_sum

# If no output, then the code works. ✅
if __name__=="__main__":
    assert (less_than_sum(3) == 3)
    assert (less_than_sum(6) == 15)
    assert (less_than_sum(10) == 45)