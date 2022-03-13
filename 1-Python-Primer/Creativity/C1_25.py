"""
📝 Author: Saud Hashmi
🧷 Problem Index: C-1.25
🚩 Problem Statement:
     Write a short Python function that takes a string "s", representing a sentence,
    and returns a copy of the string with all punctuation removed. For example, if given the string "Let's try, Mike.", this function would return
    "Lets try Mike".
"""

from string import punctuation

def remove_punctuation(s):
    new_s = ''
    for letter in s:
        if letter not in punctuation:
            new_s += letter
    return new_s

print(remove_punctuation("You ain't messin' with my chillin'. Sike! That's the wrong email@address.com"))