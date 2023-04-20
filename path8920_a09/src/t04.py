"""
-------------------------------------------------------
Assignment 9, Task 4
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-04-03"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST


bst = BST()
bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.insert(-1)

zero, one, two = bst.node_counts()
print("node_counts:")
print(f"Zero: {zero}")
print(f"One: {one}")
print(f"Two: {two}")
print("-------------------")
print("__contains__:")

print(bst.__contains__(1))
print(bst.__contains__(99))
print("-------------------")
print("parent (iterative)")

print(f"Parent of node with value == 4: {bst.parent(4)}")


print("-------------------")
print("parent (recursive)")

print(f"Parent of node with value == 4: {bst.parent_r(4)}")
