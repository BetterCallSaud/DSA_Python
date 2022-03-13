"""
📝 Author: Saud Hashmi
🧷 Problem Index: P-1.34
🚩 Problem Statement:
    A common punishment for school children is to write out a sentence multiple times. Write a Python stand-alone program that will write out the
    following sentence one hundred times: “I will never spam my friends
    again.” Your program should number each of the sentences and it should
    make eight different random-looking typos.
"""

import random
random.seed(42)

alphabets = [chr(i) for i in range(65,93)]

def generate(sen, total_typos):
    indices = [random.randint(0,len(sen)-1) for _ in range(8)]
    print(indices)
    for i in range(1,101):
        if i in indices:
            sen2 = sen[:i] + random.choice(alphabets) + sen[i+1:]
            print(i,sen2)
        # print(i, sen)

if __name__=="__main__":
    sen = "I will never spam my friends again."
    generate(sen, 8)