"""
-------------------------------------------------------
Assignment 2, Task 1
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-01-30"
-------------------------------------------------------
"""
# Imports
from Movie import Movie
from Movie_utilities import get_by_year

movies = [Movie("Movie 1", 2004, "Max Mazzetti", 4, [1, 2]),
          Movie("Movie 2", 2005, "Max Mazzetti", 4, [1, 2]),
          Movie("Movie 3", 2006, "Max Mazzetti", 4, [1, 2]),
          Movie("Movie 4", 2007, "Max Mazzetti", 4, [1, 2])]

for movie in get_by_year(movies, 2004):
    print("Movie name :", movie.title, ",  Movie year :", movie.year)
