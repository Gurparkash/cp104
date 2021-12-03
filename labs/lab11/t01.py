"""
------------------------------------------------------------------------
CP104 Lab 11, Task 01
------------------------------------------------------------------------
Author: Your Full Name
ID:     190400000
Email:  yourlaurieremail@mylaurier.ca
__updated__ = "2021-12-02"
------------------------------------------------------------------------
"""
from functions import generate_matrix_num

rows = int(input('Enter the number of rows: '))
cols = int(input('Enter the number of cols: '))
low = float(input('Enter the minimum value: '))
high = float(input('Enter the maximum value: '))
value_type = input('Enter the type of values: ')

matrix = generate_matrix_num(rows, cols, low, high, value_type)

print(f'Randomly generated matrix: {matrix}')
