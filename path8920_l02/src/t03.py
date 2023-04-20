"""
-------------------------------------------------------
Lab 3, Task 3
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-01-28"
-------------------------------------------------------
"""
from utilities import stack_to_array, array_to_stack
from Stack_array import Stack
# Constants

stack = Stack()
data = [0, 1, 2, 3, 4]
array_to_stack(stack, data)
for i in stack:
    print(i)

target = []
stack_to_array(stack, target)


print(target)
print(stack.is_empty())
