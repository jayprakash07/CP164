"""
-------------------------------------------------------
Assignment 10, Task 4
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-04-10"
-------------------------------------------------------
"""
# Imports
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque

a = Deque()
a.insert_rear(0)
a.insert_rear(0)
a.insert_rear(0)

Sorts.gnome_sort(a)
for v in a:
    print(v)
