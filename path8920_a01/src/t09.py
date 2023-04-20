"""
-------------------------------------------------------
Assignment 1, Task 9
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-01-23"
-------------------------------------------------------
"""
from functions import shift

with open("pelee.txt", "r") as readfile, open("shift.txt", "w") as writefile:

    for line in readfile:

        estring = shift(line, 26)

        writefile.write(estring)
