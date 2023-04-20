"""
-------------------------------------------------------
Assignment 4, Task 4
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-02-12"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
# Constants

target = Queue()
source1 = Queue()
source2 = Queue()

source1.insert(5)
source1.insert(8)
source1.insert(12)
source1.insert(8)
source2.insert(7)
source2.insert(9)
source2.insert(14)

print(f'source1: {source1._values}')
print(f'source2: {source2._values}')
target.combine(source1, source2)
print(f'Target: {target._values}')
