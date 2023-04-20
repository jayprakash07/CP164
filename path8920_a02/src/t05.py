"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-01-30"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies, genre_counts

fv = open("movies.txt", "r", encoding="utf-8")
movies = read_movies(fv)


m = genre_counts(movies)

print(m)
fv.close()
