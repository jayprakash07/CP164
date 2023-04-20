"""
-------------------------------------------------------
Assignment 9, Functions
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-04-03"
-------------------------------------------------------
"""
from Hash_Set_array import Hash_Set
from Word import Word


def insert_words(fv, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in file_variable and inserts into
    a HashSet.
    -------------------------------------------------------
    Preconditions:
        file_variable - the already open file containing data to evaluate (file)
        hash_set - the HashSet to insert the words into (HashSet)
    Postconditions:
        Each Word object in hash_set contains the number of comparisons
        required to insert that Word object from file_variable into hash_set.
    -------------------------------------------------------
    """
    fv = fv.readlines()
    for line in fv:
        word_list = line.split(" ")
        for word in word_list:
            if word.isalpha() is True:
                word = Word(word.lower())
                hash_set.insert(word)

    return


def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    -------------------------------------------------------
    Preconditions:
        hash_set - a hash set of Word objects (HashSet)
    Postconditions:
        returns
        total - the total of all comparison fields in the HashSet
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """
    total = 0
    max_word = None
    for i in hash_set:
        total += i.comparisons
        if not max_word or i.comparisons > max_word.comparisons:
            max_word = i

    return total, max_word
