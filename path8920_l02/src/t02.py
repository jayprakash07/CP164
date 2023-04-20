"""
-------------------------------------------------------
Lab 2, Task 2
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-01-28"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_stack
from Stack_array import Stack
# Constants

s = Stack()
data = [0, 1, 2, 3, 4]
print(data)
array_to_stack(s, data)

print(s.is_empty())

for i in s:
    print(i)
print(data)
