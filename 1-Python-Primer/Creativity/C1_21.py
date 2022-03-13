"""
📝 Author: Saud Hashmi
🧷 Problem Index: C-1.21
🚩 Problem Statement:
     Write a Python program that repeatedly reads lines from standard input
    until an EOFError is raised, and then outputs those lines in reverse order
    (a user can indicate end of input by typing ctrl-D).
"""

def read_inputs(filename):
    fp = open(filename, 'r')
    lines = []
    while True:
        try:
            line = fp.readline()
            if line == '': raise EOFError
            lines.append(line)
        except EOFError:
            return lines

filename = 'D:/PythonPrograms/DSA_Python/1-Python-Primer/Creativity/inputs.txt'
print(read_inputs(filename))