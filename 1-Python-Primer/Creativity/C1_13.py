"""
📝 Author: Saud Hashmi
🧷 Problem Index: C-1.13
🚩 Problem Statement:
    Write a pseudo-code description of a function that reverses a list of n
    integers, so that the numbers are listed in the opposite order than they
    were before, and compare this method to an equivalent Python function
    for doing the same thing.
"""

def reverse(arr):
    n = len(arr)
    for i in range(int(n/2)):
        temp = arr[i]
        arr[i] = arr[n-i-1]
        arr[n-i-1] = temp
    return arr

arr = [1,2,3,4,5,6,7]

# Reverse using slicing method
print(arr[::-1])

# Reverse using Custom function call
print(reverse(arr))
