"""
-------------------------------------------------------
Assignment 3, Task 2
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-02-06"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack

arr = [5, 7, 8, 9, 12, 14, 8]
# print(len(arr))
source = Stack()
array_to_stack(source, arr)
print(f'Stack: {source._values}')
target1, target2 = source.split_alt()
print(f'{target1._values}')
print(f'{target2._values}')
