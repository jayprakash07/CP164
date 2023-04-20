"""
-------------------------------------------------------
Lab 2, Task 5
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-01-28"
-------------------------------------------------------
"""
from utilities import stack_test

lst = []

fh = open("movies.txt", "r", encoding="utf-8")
for line in fh:
    data = line.strip().split("|")
    lst.append(data)

stack_test(lst)
fh.close()
