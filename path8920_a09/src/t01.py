"""
-------------------------------------------------------
Assignment 9, Task 1
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-04-03"
-------------------------------------------------------
"""
# Imports
from functions import comparison_total, insert_words
from Hash_Set_array import Hash_Set

# Code
fv = open("gibbon.txt", "r")
hash_set = Hash_Set(20)
insert_words(fv, hash_set)

total, max_word = comparison_total(hash_set)

print("Using array-based list Hash_set")
print("")
print(f"Total Comparisons: {total}")
print(f"Word with maximum comparisons: {max_word}")
