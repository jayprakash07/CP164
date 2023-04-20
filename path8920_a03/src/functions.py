"""
-------------------------------------------------------
Assignment 3, Functions
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-02-06"
-------------------------------------------------------
"""
# Imports
from enum import Enum

from Stack_array import Stack

# Constants
OPERATORS = "+-*/"

MIRRORED = Enum('MIRRORED', {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",

                'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",

                             'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()
    while(not source.is_empty()):
        target1.push(source.pop())
        if(not source.is_empty()):
            target2.push(source.pop())
    return target1, target2


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    stack = Stack()
    palindrome = True
    i = 0
    string = string.upper()
    _str = string.strip("!").split(" ")
    string = ""
    for _str in _str:
        string += _str
    n = len(string)
    while i < (n // 2):
        stack.push(string[i])
        i += 1
    i += 1
    while i < n:
        if stack.is_empty():
            palindrome = False
            return palindrome
        else:
            top = stack.pop()
            if top == string[i]:
                palindrome = True
                return palindrome


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()

    for item in string.split(' '):
        if item.isdigit():
            stack.push(int(item))
        elif item in OPERATORS:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if item == '+':
                stack.push(operand1 + operand2)
            elif item == '-':
                stack.push(operand1 - operand2)
            elif item == '*':
                stack.push(operand1 * operand2)
            elif item == '/':
                stack.push(operand1 / operand2)

    return stack.pop()


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    s = Stack()

    s.push('Start')
    while not s.is_empty():
        current = s.peek()
        if current == 'X':
            break
        branches = maze[current]
        if len(branches) == 0:
            s.pop()
        else:
            branch = branches.pop()
            s.push(branch)
        if s.is_empty():
            return None
        else:
            path = []
        while not s.is_empty():
            path.append(s.pop())

    return path[::-1]


def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    if m in valid_chars or m not in string:

        return MIRRORED.NOT_MIRRORED

    mirroringCheck = False

    stack = []

    for i in string:

        if i not in valid_chars and i != m:

            return MIRRORED.INVALID_CHAR

        elif i != m and not mirroringCheck:

            stack.append(i)

        elif i == m:

            mirroringCheck = True

            if len(stack) < (len(string) - (len(stack)+1)):

                return MIRRORED.TOO_MANY_RIGHT

            elif len(stack) > (len(string) - (len(stack)+1)):

                return MIRRORED.TOO_MANY_LEFT

        else:

            if i != stack.pop():

                return MIRRORED.MISMATCHED

    assert m not in valid_chars and m != '{}'

    return MIRRORED.IS_MIRRORED
