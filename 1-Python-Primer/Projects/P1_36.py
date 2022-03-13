"""
📝 Author: Saud Hashmi
🧷 Problem Index: P-1.35
🚩 Problem Statement:
    Write a Python program that inputs a list of words, separated by whitespace, and outputs how many times each word appears in the list. You
    need not worry about efficiency at this point, however, as this topic is
    something that will be addressed later in this book
"""

import re

def word_appearances(sen):
    new_sen = re.findall(r'\w+', sen)
    ctr = dict()
    for word in new_sen:
        if word not in ctr: ctr[word] = 1
        else: ctr[word] += 1
    return ctr

sen = "David, here it is. My philosophy is basically this. And this is something that I live by. And I always have. And I always will. Don't ever, for any reason, do anything to anyone, for any reason, ever, no matter what. No matter... where. Or who, or who you are with, or, or where you are going, or... or where you've been... ever. For any reason, whatsoever."

print(word_appearances(sen))