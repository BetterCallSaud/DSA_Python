"""
📝 Author: Saud Hashmi
🧷 Problem Index: C-1.24
🚩 Problem Statement:
     Write a short Python function that counts the number of vowels in a given
    character string.
"""

vowels = ['a', 'e', 'i', 'o', 'u']
num_vowels = lambda word : len([letter for letter in word if letter.lower() in vowels])
print(num_vowels("ABRACADABRA"))