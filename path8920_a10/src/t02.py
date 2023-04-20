"""
-------------------------------------------------------
Assignment 10, Task 2
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-04-10"
-------------------------------------------------------
"""
# Imports
from Sorts_List_linked import Sorts
from List_linked import List

a = List()
a.append(0)
a.append(0)
a.append(0)


Sorts.radix_sort(a)

for v in a:
    print(v)
