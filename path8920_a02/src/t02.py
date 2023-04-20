"""
-------------------------------------------------------
Assignment 2, Task 2
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-01-30"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import get_by_rating, read_movies
# Constants


fv = open("movies.txt", "r", encoding="utf-8")
movies = read_movies(fv)

rating = float(input('Search for movies by rating: '))
rmovies = get_by_rating(movies, rating)

print(f'Movies by Rating: {rating}')
print("-" * 80)
for i in rmovies:
    print(i)
print("-" * 80)

fv.close()
