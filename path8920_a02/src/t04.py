"""
-------------------------------------------------------
Assignment 2, Task 4
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-01-30"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies, get_by_genres

fv = open("movies.txt", "r", encoding="utf-8")
movies = read_movies(fv)

genres = [3, 4, 5, 8]
m = get_by_genres(movies, genres)

print(f'Movies by Genre code: {genres}')
for i in m:
    print("\n")
    print(i)

fv.close()
