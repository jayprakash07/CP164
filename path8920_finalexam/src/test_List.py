"""
-------------------------------------------------------
Exam: Simple List testing
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-04-14"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from List_linked import List

# Constants
VALUES = [3, 8, 6, 7, 6, 2, 4, 6]
SEP = '-' * 60


def to_python_list(source):
    """
    Testing helper method. Copies List values to a Python list.
    """
    values = []
    for value in source:
        values.append(value)
    return values


def from_python_list(values):
    """
    Testing helper method. Copies Python list values to a List.
    """
    source = List()
    for value in values:
        source.append(value)
    return source


def test_shift_front():
    """
    Tests the 'shift_front' method.
    """
    print(SEP)
    print("Test 'shift_front'")
    print()

    source = List()
    print(f"  List: {to_python_list(source)}")
    source.shift_front()
    print(f"  After 'shift_front': {to_python_list(source)}")
    print()

    source = from_python_list(VALUES[:1])
    print(f"  List: {to_python_list(source)}")
    source.shift_front()
    print(f"  After 'shift_front': {to_python_list(source)}")
    print()

    source = from_python_list(VALUES)
    print(f"  List: {to_python_list(source)}")
    source.shift_front()
    print(f"  After 'shift_front': {to_python_list(source)}")
    print()


def test_shift_rear():
    """
    Tests the 'shift_rear' method.
    """
    print(SEP)
    print("Test 'shift_rear'")
    print()

    source = List()
    print(f"  List: {to_python_list(source)}")
    source.shift_rear()
    print(f"  After 'shift_rear': {to_python_list(source)}")
    print()

    source = from_python_list(VALUES[:1])
    print(f"  List: {to_python_list(source)}")
    source.shift_rear()
    print(f"  After 'shift_rear': {to_python_list(source)}")
    print()

    source = from_python_list(VALUES)
    print(f"  List: {to_python_list(source)}")
    source.shift_rear()
    print(f"  After 'shift_rear': {to_python_list(source)}")
    print()


if __name__ == "__main__":
    print("List_linked Testing")
    test_shift_front()
    test_shift_rear()
