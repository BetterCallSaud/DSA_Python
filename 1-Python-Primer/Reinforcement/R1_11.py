"""
📝 Author: Saud Hashmi
🧷 Problem Index: R-1.11
🚩 Problem Statement:
    Demonstrate how to use Python's list comprehension syntax to produce
    the list [1, 2, 4, 8, 16, 32, 64, 128, 256]
"""

def demo():
    print([2**i for i in range(9)])

if __name__=="__main__":
    demo()