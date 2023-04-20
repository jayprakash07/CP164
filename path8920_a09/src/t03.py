"""
-------------------------------------------------------
Assignment 9, Task 3
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-04-03"
-------------------------------------------------------
"""
# Imports
from functions import comparison_total, insert_words
from Hash_Set_BST import Hash_Set

# Code
fv = open("gibbon.txt", "r")
hs = Hash_Set(20)
insert_words(fv, hs)

total, max_word = comparison_total(hs)

print("Using linked BST Hash_set")
print("")
print(f"Total Comparisons: {total}")
print(f"Word with maximum comparisons: {max_word}")
