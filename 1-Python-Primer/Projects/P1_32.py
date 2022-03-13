"""
📝 Author: Saud Hashmi
🧷 Problem Index: P-1.32
🚩 Problem Statement:
    Write a Python program that can simulate a simple calculator, using the
    console as the exclusive input and output device. That is, each input to the
    calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
    can be done on a separate line. After each such input, you should output
    to the Python console what would be displayed on your calculator.
"""

import sys

def calculator(args):
    a, sign, b = args[1:]
    a, b = int(a), int (b)
    if sign=='+': return a + b
    if sign=='-': return a - b
    if sign=='x' or sign=='*': return a * b
    if sign=='/': return a / b
    else: return "The second argument must be from: [+,-,*,x,/]"

if __name__ == "__main__":
    assert (len(sys.argv) == 4)
    print(calculator(sys.argv))