"""
------------------------------------------------------------------------
CP104 Lab 11, Task 02
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2021-12-02"
------------------------------------------------------------------------
"""
from functions import generate_matrix_char

rows = int(input('Enter the number of rows: '))
cols = int(input('Enter the number of cols: '))

matrix = generate_matrix_char(rows, cols)

print(f'Randomly generated matrix: {matrix}')