"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-01-23"
-------------------------------------------------------
"""
from functions import file_analyze

fv = open("student_information.txt", "r")
u, l, d, w, r = file_analyze(fv)

print("The number of uppercase letters in the file: {}".format(u))
print("The number of lowercase letters in the file: {}".format(l))
print("The number of digits in the file: {}".format(d))
print("The number of whitespace characters in the file: {}".format(w))
print("The number of remaining characters in the file: {}".format(r))
