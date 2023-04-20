"""
-------------------------------------------------------
Assignment 6, Task 1
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-03-13"
-------------------------------------------------------
"""
# Imports
from Queue_linked import Queue
# Constants

q = Queue()

q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)

s = Queue()
s.insert(5)
s.insert(6)
s.insert(7)
s.insert(8)

print("Queue 1:")
for i in q:
    print(i, end=" ")
print()
print("Queue 2:")
for j in s:
    print(j, end=" ")
print()
q._append_queue(s)
print("Queue 1 after append:")
for i in q:
    print(i, end=" ")
