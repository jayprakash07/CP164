"""
-------------------------------------------------------
Assignment 6, Task 2
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-03-13"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_linked import Priority_Queue
# Constants

source = Priority_Queue()
source.insert(1)
source.insert(2)
source.insert(3)
source.insert(4)
source.insert(5)
target1, target2 = source.split_alt()
for i in target1:
    print(i, end=" ")
print()
for i in target2:
    print(i, end=" ")
print()
