"""
-------------------------------------------------------
Assignment 2, Task 3
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2023-01-30"
-------------------------------------------------------
"""
from Movie import Movie
from Movie_utilities import get_by_genre

movies = [Movie("Movie1", 2020, "Director1", 8, [1, 2, 3]),
          Movie("Movie2", 2019, "Director2", 7, [4, 2, 3]),
          Movie("Movie3", 2020, "Director1", 8, [1, 3]),
          Movie("Movie4", 2010, "Director1", 8, [2, 3]),
          Movie("Movie5", 2019, "Director1", 8, [3, 4, 5]),
          Movie("Movie6", 2018, "Director1", 8, [1, 4, 5])]

gmovies = get_by_genre(movies, 4)

for m in gmovies:
    print(m.title)
