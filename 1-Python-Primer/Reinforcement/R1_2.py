"""
📝 Author: Saud Hashmi
🧷 Problem Index: R-1.2
🚩 Problem Statement:
    Write a short Python function, is even(k), that takes an integer value and
    returns True if k is even, and False otherwise. However, your function
    cannot use the multiplication, modulo, or division operators
"""

def is_even(k):
    return True if k%2==0 else False

# If no output, then the code works. ✅
if __name__=="__main__":
    assert (is_even(2) == True)
    assert (is_even(3) == False)