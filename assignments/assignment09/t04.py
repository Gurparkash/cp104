"""
------------------------------------------------------------------------
CP104 Assignment 09, Task 04
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2021-12-03"
------------------------------------------------------------------------
"""
from functions import flatten

matrix = [[1, 2, 9], [8, 7, 12], [4, 2, 0]]

print(f'Original Matrix: {matrix}')

flat = flatten(matrix)

print(f'Flattened Matrix: {flat}')
