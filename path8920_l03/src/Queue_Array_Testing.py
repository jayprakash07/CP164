"""
-------------------------------------------------------
Lab 3, Array-Based Queues
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-02-04"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from utilities import array_to_queue, queue_to_array, queue_test
# Constants
print('Array to queue...')
queue = Queue()
source = [1, 2, 3, 4, 5]
print(f'Before: {source}')
print(f'Empty queue: {queue.is_empty()}')
array_to_queue(queue, source)
print(f'After: {source}')
print('Queue contents:')
for i in queue:
    print(i)
print('End of queue')
print('-' * 50)
queue_test(queue)
print(f'Empty queue: {queue.is_empty()}')
print('-' * 50)
print('Queue to array...')
print('Queue contents:')
for i in queue:
    print(i)
target = []
print(f'Target before: {target}')
queue_to_array(queue, target)
print(f'Target after: {target}')
print(f'Empty queue: {queue.is_empty()}')
