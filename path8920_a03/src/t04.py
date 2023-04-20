"""
-------------------------------------------------------
Assignment 3, Task 4
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-02-06"
-------------------------------------------------------
"""
from functions import postfix

# Postfix Expression 1
string = "12 5 -"
print('\"', string, '\"', " evaluates to: ", postfix(string), sep="")

# Postfix Expression 2
string2 = "4 5 + 12 * 2 3 * -"
print('\"', string2, '\"', " evaluates to: ", postfix(string2), sep="")
