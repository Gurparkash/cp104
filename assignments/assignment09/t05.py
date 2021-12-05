"""
------------------------------------------------------------------------
CP104 Assignment 09, Task 05
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2021-12-03"
------------------------------------------------------------------------
"""
from functions import matrix_rotate_right

# Make sure to create and test two more matrices
matrix = [[1, 2, 9], [8, 7, 12], [4, 2, 0]]

print(f'Original Matrix: {matrix}')

rotated = matrix_rotate_right(matrix)

print(f'Rotated Matrix: {rotated}')
