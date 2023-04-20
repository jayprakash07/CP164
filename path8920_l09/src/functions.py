"""
-------------------------------------------------------
Lab 9, Functions
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-03-24"
-------------------------------------------------------
"""


def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
    Hash     Slot Key
    -------- ---- --------------------
    1652346    3 Dark City, 1998
    848448    6 Zulu, 1964
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    elements = []
    for movie in values:
        elements.append([hash(movie), hash(movie) % slots, movie.key()])
    print("Hashes")
    # table header
    print("{:>8} {:>4} {:<20}".format("Hash", "Slot", "Key"))
    print("{:>8} {:>4} {:<20}".format(
        str('-' * 8), str('-' * 4), str('-' * 20)))
    for el in elements:
        print("{:>8} {:>4} {:<20}".format(el[0], el[1], el[2]))

    return
