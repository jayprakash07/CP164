"""
-------------------------------------------------------
Assignment 1, Task 3
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-01-23"
-------------------------------------------------------
"""
from functions import find_subs

string = input(f"String: ")
sub = input(f"Sub: ")

locations = find_subs(string, sub)
print(locations)
