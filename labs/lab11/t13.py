"""
------------------------------------------------------------------------
CP104 Lab 11, Task 13
------------------------------------------------------------------------
Author: Your Full Name
ID:     190400000
Email:  yourlaurieremail@mylaurier.ca
__updated__ = "2021-12-02"
------------------------------------------------------------------------
"""
# from functions import generate_matrix_num
from functions import scalar_multiply

# If available use generate_matrix_num
# matrix = generate_matrix_num(2,3,0,100,'float')

# Else use the code below
matrix = [[6954, 345, 3697], [9279, 9892, 9094]]
# You can ask for input for num
num = 2

print(f'Matrix (without scalar multiplication: {matrix} ')

scalar_multiply(matrix, num)

print(f'Matrix (with scalar multiplication: {matrix}')