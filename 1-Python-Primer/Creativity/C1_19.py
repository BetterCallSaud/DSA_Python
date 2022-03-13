"""
📝 Author: Saud Hashmi
🧷 Problem Index: C-1.19
🚩 Problem Statement:
    Demonstrate how to use Python’s list comprehension syntax to produce
    the list [ a , b , c , ..., z ], but without having to type all 26 such
    characters literally.
"""

alphabets = [chr(i).lower() for i in range(65,91)]
print(alphabets)