"""
๐ Author: Saud Hashmi
๐งท Problem Index: C-1.24
๐ฉ Problem Statement:
     Write a short Python function that counts the number of vowels in a given
    character string.
"""

vowels = ['a', 'e', 'i', 'o', 'u']
num_vowels = lambda word : len([letter for letter in word if letter.lower() in vowels])
print(num_vowels("ABRACADABRA"))