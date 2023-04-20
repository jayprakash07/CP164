"""
-------------------------------------------------------
Assignment 4, Task 5
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-02-12"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from functions import pq_split_key
# Constants
key = 5
source = Priority_Queue()
source.insert(10)
source.insert(1)
source.insert(5)
source.insert(25)
source.insert(0)
print(f'source: {source._values}')
print(f'key: {key}')

target1 = Priority_Queue()
target2 = Priority_Queue()

target1, target2 = pq_split_key(source, key)
print(f'target1: {target1._values}')
print(f'target2: {target2._values}')
