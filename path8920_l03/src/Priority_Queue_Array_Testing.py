"""
-------------------------------------------------------
Lab 3, Priority Queue Array
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-02-04"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq, pq_to_array, priority_queue_test
# Constants

# array to pq
source = [1, 3, 5, 9]
print(f'Source before: {source}')
pq = Priority_Queue()
array_to_pq(pq, source)
print('Contents of Priority Queue object...')
for i in pq:
    print(i)
print(f'Source after: {source}')
print('-' * 50)

# queue test
a = [10, 20, 30, 40, 50]
priority_queue_test(a)
print('-' * 50)

# pq to array
target = []
print('Target before: ')
pq_to_array(pq, target)
print(f'Target after: {target}')
print(f'pq empty: {pq.is_empty()}')
