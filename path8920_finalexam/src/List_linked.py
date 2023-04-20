"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author: Jayprakash Pathak
ID:     169018920
Email:  path8920@mylaurier.ca
__updated__ = "2023-04-17"
-------------------------------------------------------
"""
# pylint: disable=W0212
# pylint: disable=E2515
# pylint: disable=E0303
# pylint: disable=W0613
# pylint: disable=E1128

from copy import deepcopy


class List:

    def shift_front(self):
        """
        -------------------------------------------------------
        Moves the front node to the rear of the List.
        Use: source.shift_front()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            None
        -------------------------------------------------------
        """
        if self._front is None or self._front == self._rear:
            return

        value = self._front._value
        self._front = self._front._next
        self._rear._next = _List_Node(value, None)
        self._rear = self._rear._next

        return

    def shift_rear(self):
        """
        -------------------------------------------------------
        Moves the rear node to the front of the List.
        Use: source.shift_rear()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            None
        -------------------------------------------------------
        """
        if self._front is None or self._front == self._rear:
            # List is empty or only has one node.
            return

        # Traverse the list to find the node before the rear node.
        current = self._front
        while current._next != self._rear:
            current = current._next

        # Rearrange the pointers.
        self._rear._next = self._front
        self._front = self._rear
        self._rear = current
        self._rear._next = None

        return


# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            None
        -------------------------------------------------------
        """
        # Create the new node.
        node = _List_Node(value, None)

        if self._front is None:
            # list is empty - update the front of the List.
            self._front = node
        else:
            self._rear._next = node
        # Update the rear of the List.
        self._rear = node
        self._count += 1
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next


class _List_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
