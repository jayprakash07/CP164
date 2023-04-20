"""
-------------------------------------------------------
Lab 9, Task 1
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-03-24"
-------------------------------------------------------
"""
from functions import hash_table
from Movie import Movie

if __name__ == "__main__":
    # testing
    movies = []
    # creating Movie Objects
    m1 = Movie("Dark City", 1988, "Bruce Jones", 9.8, [0, 6])
    m2 = Movie("Zulu", 1964, "Candice Jill", 7.6, [1, 2])
    m3 = Movie("I Am Legend", 2007, "John Doe", 6.5, [1, 4])
    m4 = Movie("Omega Man, The", 1971, "Bong Nail", 5.7, [0, 7])
    m5 = Movie("Dark City", 1988, "Bruce Jones", 7.4, [2])
    m6 = Movie("Dark City", 1988, "Bruce Jones", 6.8, [0, 1])
    # appending movie objects to the list movies
    movies.extend([m1, m2, m3, m4, m5, m6])
    hash_table(7, movies)  # printing hash_table
