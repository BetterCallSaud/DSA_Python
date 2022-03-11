"""
📝 Author: Saud Hashmi
🧷 Problem Index: R-1.3
🚩 Problem Statement:
    Write a short Python function, minmax(data), that takes a sequence of
    one or more numbers, and returns the smallest and largest numbers, in the
    form of a tuple of length two. Do not use the built-in functions min or
    max in implementing your solution.
"""

def minmax(data):
    if len(data) == 1:
        return (data[0], data[0])
    local_min, local_max = data[0], data[0]
    for i in range(1,len(data)):
        if data[i] <= local_min:
            local_min = data[i]
        elif data[i] >= local_max:
            local_max = data[i]
    return local_min, local_max

# If no output, then the code works. ✅
if __name__=="__main__":
    assert (minmax([3,7,0,1,5]) == (0,7))
    assert (minmax([100,99,0-100,1,5]) == (-100,100))
    assert (minmax([-6, -9, 6, 9]) == (-9,9))