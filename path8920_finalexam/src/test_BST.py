"""
-------------------------------------------------------
Exam: Simple BST testing
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-04-14"
-------------------------------------------------------
"""
# pylint: disable=E1128
# pylint: disable=W0212
# pylint: disable=E0633

# Imports
from BST_linked import BST


# Constants
VALUES = [11, 7, 6, 9, 8, 15, 12, 18]
SEP = '-' * 60


def test_are_adjacents():
    """
    Tests the 'are_adjacents' method.
    """
    print(SEP)
    print("Test 'are_adjacents'")
    print()
    bst = BST()

    for v in VALUES:
        bst.insert(v)

    print(f"  Preorder: {bst.preorder()}")
    print(f"  are_adjacents(11, 15): {bst.are_adjacents(11, 15)}")
    print(f"  are_adjacents(7, 15): {bst.are_adjacents(7, 15)}")
    print(f"  are_adjacents(7, 18): {bst.are_adjacents(7, 18)}")


def test_furthest():
    """
    Tests the 'furthest' method.
    """
    print(SEP)
    print("Test 'furthest'")
    print()
    bst = BST()

    print(f"  Preorder: {bst.preorder()}")
    print(f"  Furthest: {bst.furthest()}")
    print()

    bst.insert(VALUES[0])
    print(f"  Preorder: {bst.preorder()}")
    print(f"  Furthest: {bst.furthest()}")
    print()

    for v in VALUES[1:]:
        bst.insert(v)
    print(f"  Preorder: {bst.preorder()}")
    print(f"  Furthest: {bst.furthest()}")


def test_max_path():
    """
    Tests the 'max_path' method.
    """
    print(SEP)
    print("Test 'max_path'")
    print()
    bst = BST()

    print(f"  Preorder: {bst.preorder()}")
    print(f"  Max Path: {bst.max_path()}")
    print()

    bst.insert(VALUES[0])
    print(f"  Preorder: {bst.preorder()}")
    print(f"  Max Path: {bst.max_path()}")
    print()

    for v in VALUES[1:]:
        bst.insert(v)
    print(f"  Preorder: {bst.preorder()}")
    print(f"  Max Path: {bst.max_path()}")


if __name__ == "__main__":
    print("BST_linked Testing")
    test_are_adjacents()
    test_furthest()
    test_max_path()
