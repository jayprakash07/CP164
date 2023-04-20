"""
-------------------------------------------------------
Assignment 6, Task 3
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-03-13"
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque
# Constants
d = Deque()
for i in range(5):
    d.insert_front(i)

for j in d:
    print(i, end=" ")
