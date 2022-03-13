"""
📝 Author: Saud Hashmi
🧷 Problem Index: P-1.31
🚩 Problem Statement:
    Write a Python program that can “make change.” Your program should
    take two numbers as input, one that is a monetary amount charged and the
    other that is a monetary amount given. It should then return the number
    of each kind of bill and coin to give back as change for the difference
    between the amount given and the amount charged. The values assigned
    to the bills and coins can be based on the monetary system of any current
    or former government. Try to design your program so that it returns as
    few bills and coins as possible.
"""

den = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]

def make_change(amt_charged, amt_given):
    diff = amt_given - amt_charged
    cash_sum = 0
    seq = []
    i = len(den)-1
    while cash_sum < diff:
        if den[i] > diff: i -= 1
        else:
            if cash_sum + den[i] <= diff: 
                cash_sum += den[i]
                seq.append(den[i])
            else: i -= 1
    return seq

print(make_change(1310, 2000))
print(make_change(1000, 2000))
print(make_change(6942, 13884))