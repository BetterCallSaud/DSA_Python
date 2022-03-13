"""
📝 Author: Saud Hashmi
🧷 Problem Index: C-1.20
🚩 Problem Statement:
    Python’s random module includes a function shuffle(data) that accepts a
    list of elements and randomly reorders the elements so that each possible order occurs with equal probability. The random module includes a
    more basic function randint(a, b) that returns a uniformly random integer
    from a to b (including both endpoints). Using only the randint function,
    implement your own version of the shuffle function.
"""

from random import randint

def shuffle():
    a = [randint(1,50) for _ in range(10)]
    b = a.copy()
    res = []
    n = len(a)
    for _ in range(n):
        idx = randint(0,n-1)
        res.append(a[idx])
        del a[idx]
        n -= 1
    return b, res

arr, shuffled_arr = shuffle()
print(arr)
print(shuffled_arr)