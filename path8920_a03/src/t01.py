"""
-------------------------------------------------------
Assignment 3, Task 1
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-02-06"
-------------------------------------------------------
"""
from Stack_array import Stack
from functions import stack_split_alt

S = Stack()
print("Displaying Original Stack : ")
for i in range(1, 11):
    S.push(i)
    print(S.peek())
target1, target2 = stack_split_alt(S)
print("Displaying First alternate Stack : ")
while(not target1.is_empty()):
    print(target1.pop())
print("Displaying Second alternate Stack : ")
while(not target2.is_empty()):
    print(target2.pop())
