"""
-------------------------------------------------------
[CP164: List_Linked Testing]
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-03-10"
-------------------------------------------------------
"""
# Imports
from List_linked import List
list = List()

list.append(1), list.append(4), list.append(
    55), list.append(77), list.append(4)

print(f"Find: {list.find(77)}")
print(f"Index: {list.index(4)}")
print(f"Contains: {77 in list}")  # Result= True
print(f"Contains: {99 in list}")  # Result= False
