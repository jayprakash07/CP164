"""
-------------------------------------------------------
Assignment 4, Task 6
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-02-12"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue

queue = Priority_Queue()
count = int(input("# of values: "))

for i in range(count):
    value = int(input(f"Value {i+1}: "))
    queue.insert(value)
key = int(input("Key: "))
target1, target2 = queue.split_key(key)

print("Target 1:")
for i in target1:
    print(i)

print("Target 2:")
for i in target2:
    print(i)
