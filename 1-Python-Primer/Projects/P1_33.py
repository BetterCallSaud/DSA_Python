"""
📝 Author: Saud Hashmi
🧷 Problem Index: P-1.33
🚩 Problem Statement:
    Write a Python program that simulates a handheld calculator. Your program should process input from the Python console representing buttons
    that are “pushed,” and then output the contents of the screen after each operation is performed. Minimally, your calculator should be able to process
    the basic arithmetic operations and a reset/clear operation.
"""

import sys

def calculator(args):
    a, sign, b = args[0], args[1], args[2]
    a, b = int(a), int (b)
    if sign=='+': return a + b
    if sign=='-': return a - b
    if sign=='x' or sign=='*': return a * b
    if sign=='/': return a / b
    else: return "The second argument must be from: [+,-,*,x,/]"

if __name__=="__main__":
    while True:
        x = input()
        if x == 'OFF': break
        print(calculator(x))