"""
-------------------------------------------------------
Assignment 3, Task 6
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-02-06"
-------------------------------------------------------
"""
from functions import is_mirror_stack

mirror = is_mirror_stack("cmc", "abc", "m")

print("Calling: is_mirror_stack(\"cmc\", \"abc\", \"m\")\n\tResult = Mirror: {}".format(mirror.value))

mirror = is_mirror_stack("zzxzuzxzz", "xyz", "u")

print("Calling: is_mirror_stack(\"zzxzuzxzz\", \"xyz\", \"u\")\n\tResult = Mirror: {}".format(mirror.value))

mirror = is_mirror_stack("cmc", "ab", "m")

print("Calling: is_mirror_stack(\"cmc\", \"ab\", \"m\")\n\tResult = Mirror: {}".format(mirror.value))

mirror = is_mirror_stack("zzxzxzxzz", "xyz", "u")

print("Calling: is_mirror_stack(\"zzxzxzxzz\", \"xyz\", \"u\")\n\tResult = Mirror: {}".format(mirror.value))

mirror = is_mirror_stack("zzxzuzx", "xyz", "u")

print("Calling: is_mirror_stack(\"zzxzuzx\", \"xyz\", \"u\")\n\tResult = Mirror: {}".format(mirror.value))
