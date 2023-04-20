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

# Peek Task
print(f"Peek: {list.peek()}")  # first value in list

# Get_Item Task
print(f"Get_Item Task: {list[0]}")

# Set_Item Task
list[0] = 44  # changes first value in list from 1 to 44
print(f"Set_Item Task: {list[0]}")

# Remove Task
list.remove(77)
for i in list:
    print(i)
print()
