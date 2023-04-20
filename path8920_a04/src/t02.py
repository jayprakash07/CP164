"""
-------------------------------------------------------
Assignment 4, Task 2
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-02-12"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from utilities import array_to_queue
# Constants

# create queue objects
source = Queue()
target = Queue()

# create arrays with content
source_arr = [1, 2, 3, 4, 5]
target_arr = [5, 4, 3, 2, 1]

# convert arrays to queues
array_to_queue(source, source_arr)
array_to_queue(target, target_arr)

# display contents
print(f'source queue: {source._values}')
print(f'target queue: {target._values}')

# verify if equal
equals = (source == target)
print(f'equal queues: {equals}')
