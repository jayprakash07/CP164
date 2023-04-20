"""
-------------------------------------------------------
Linked version of the BST ADT - Exam
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

# Imports
from copy import deepcopy


class BST:

    def are_adjacents(self, v1, v2):
        """
        -------------------------------------------------------
        Determines if nodes containing values v1 and v2 are adjacents.
        Nodes are adjacents if they have the same parent.
        Use: b = source.are_adjacents(v1, v2)
        -------------------------------------------------------
        Parameters:
            v1 - a node value (*)
            v2 - a node value (*)
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            adjacents - True if the nodes containing v1 and v2 are adjacents,
                False otherwise.
        -------------------------------------------------------
        """
        adjacents = self._are_adjacents_aux(self._root, v1, v2)
        return adjacents

    def _are_adjacents_aux(self, parent, v1, v2):
        """
        -------------------------------------------------------
        Determines if nodes containing values v1 and v2 are adjacents.
        Nodes are adjacents if they have the same parent.
        Use: adjacents = self._are_adjacents_aux(parent, v1, v2)
        -------------------------------------------------------
        Parameters:
            parent - a potential parent of nodes containing v1 and v2 (_BST_Node)
            v1 - a node value (*)
            v2 - a node value (*)
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            adjacents - True if the nodes containing v1 and v2 are adjacents,
                False otherwise.
        -------------------------------------------------------
        """
        if parent is None:
            return False

        if (parent.left and parent.left.data == v1 and parent.right and parent.right.data == v2) or \
                (parent.left and parent.left.data == v2 and parent.right and parent.right.data == v1):
            return True

        if parent.data == v1:
            return self._are_adjacents_aux(self._root, v1, v2)

        if parent.data == v2:
            return self._are_adjacents_aux(self._root, v2, v1)

        if v1 < parent.data and v2 < parent.data:
            return self._are_adjacents_aux(parent.left, v1, v2)

        if v1 > parent.data and v2 > parent.data:
            return self._are_adjacents_aux(parent.right, v1, v2)

        return False

    def furthest(self):
        """
        -------------------------------------------------------
        Returns the values of the left-most and right-most nodes.
        Use: values = self.furthest()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            values - the values in the left-most and right-most nodes,
                in that order, an empty list if the bst is empty (list of *)
        -------------------------------------------------------
        """
        if self._root is None:
            return []

        leftmost = self._leftmost(self._root).data
        rightmost = self._rightmost(self._root).data

        return [leftmost, rightmost]

    def _leftmost(self, node):
        while node.left is None:
            node = node.left
        return node

    def _rightmost(self, node):
        while node.right is None:
            node = node.right
        return node

    def max_path(self):
        """
        ---------------------------------------------------------
        Returns the values in the longest path of source. If there are multiple
        paths of the same maximum length, return the leftmost path.
        Returns an empty list if source is empty.
        Use: path = source.max_path()
        ---------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            path - a list of values of the longest path from 
                root to the leaves of source (list of *)
        ---------------------------------------------------------
        """
        path = self._max_path_aux(self._root)
        return path

    def _max_path_aux(self, node):
        """
        ---------------------------------------------------------
        Returns a list of the values in the longest path from node to the
        leaves of self.
        Private auxiliary method for max_path.
        Use: path = self._max_path_aux(node)
        ---------------------------------------------------------
        Parameters:
            node - a BST node (_BST_Node)
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            path - a list of the values in the longest path from node
                to the leaves of self (list of *)
        ---------------------------------------------------------
        """
        if node is None:
            return 0, []

        left_depth, left_path = self._max_path_aux(node.left)
        right_depth, right_path = self._max_path_aux(node.right)

        if left_depth > right_depth:
            return left_depth + 1, [node.data] + left_path
        elif right_depth > left_depth:
            return right_depth + 1, [node.data] + right_path
        else:
            return left_depth + 1, [node.data] + left_path

# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            A BST object (BST)
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into bst. Values may appear
        only once in a tree.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data to be inserted into bst (?)
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            inserted - True if value is inserted into bst,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into node.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
            value - data to be inserted into the node (?)
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            node - the current node (_BST_Node)
            inserted - True if value is inserted into node,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: add a new node containing the value.
            node = _BST_Node(value)
            self._count += 1
            inserted = True
        elif value < node._value:
            # General case: check the left subtree.
            node._left, inserted = self._insert_aux(node._left, value)
        elif value > node._value:
            # General case: check the right subtree.
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            # Base case: value is already in the BST.
            inserted = False

        if inserted:
            # Update the node height if any of its children have been changed.
            node._update_height()
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in bst. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        node = self._root
        value = None

        while node is not None and value is None:

            if node._value > key:
                node = node._left
            elif node._value < key:
                node = node._right
            elif node._value == key:
                # for comparison counting
                value = deepcopy(node._value)
        return value

    def inorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: a = bst.inorder()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """
        a = []
        self._inorder_aux(self._root, a)
        return a

    def _inorder_aux(self, node, a):
        """
        ---------------------------------------------------------
        Traverses node subtree in inorder. a contains the contents of
        node and its children in inorder.
        Private recursive operation called only by inorder.
        Use: self._inorder_aux(node, a)
        ---------------------------------------------------------
        Parameters:
            node - an BST node (_BST_Node)
            a - target list of data (list of ?)
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            None
        ---------------------------------------------------------
        """
        if node is not None:
            self._inorder_aux(node._left, a)
            a.append(deepcopy(node._value))
            self._inorder_aux(node._right, a)
        return

    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """
        a = []
        self._preorder_aux(self._root, a)
        return a

    def _preorder_aux(self, node, a):
        """
        ---------------------------------------------------------
        Traverses node subtree in preorder. a contains the contents of
        node and its children in preorder.
        Private recursive operation called only by preorder.
        Use: self._preorder_aux(node, a)
        ---------------------------------------------------------
        Parameters:
            node - an BST node (_BST_Node)
            a - target of data (list of ?)
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            None
        ---------------------------------------------------------
        """
        if node is not None:
            a.append(deepcopy(node._value))
            self._preorder_aux(node._left, a)
            self._preorder_aux(node._right, a)
        return

    def _node_height(self, node):
        """
        ---------------------------------------------------------
        Helper function to determine the height of node - handles empty node.
        Private operation called only by _is_valid_aux.
        Use: h = self._node_height(node)
        ---------------------------------------------------------
        Parameters:
            node - the node to get the height of (_BST_Node)
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            height - 0 if node is None, node._height otherwise (int)
        ---------------------------------------------------------
        """
        if node is None:
            height = 0
        else:
            height = node._height
        return height


class _BST_Node:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a BST node containing value. Child pointers
        are None, height is 1.
        Use: node = _BST_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for the node (?)
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            A _BST_Node object (_BST_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1
        self._count = 0

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node. _height is 1 plus
        the maximum of the node's (up to) two child heights.
        Use: node._update_height()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​​‌‌​​​‌​‌​​​:
            None
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return f"h: {self._height}, v: {self._value}"
