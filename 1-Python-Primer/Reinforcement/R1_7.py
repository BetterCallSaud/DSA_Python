"""
๐ Author: Saud Hashmi
๐งท Problem Index: R-1.7
๐ฉ Problem Statement:
    Give a single command that computes the sum from Exercise R-1.6, relying on Python's comprehension syntax and the built-in sum function
"""

def odd_less_than_sum(n):
    return sum([i for i in range(1,n,2)])

# If no output, then the code works. โ
if __name__=="__main__":
    assert (odd_less_than_sum(3) == 1)
    assert (odd_less_than_sum(6) == 9)
    assert (odd_less_than_sum(10) == 25)