"""
------------------------------------------------------------------------
CP104 Lab 11, Task 08
------------------------------------------------------------------------
Author: Your Full Name
ID:     190400000
Email:  yourlaurieremail@mylaurier.ca
__updated__ = "2021-12-02"
------------------------------------------------------------------------
"""
# from functions import generate_matrix_num
from functions import find_less

# If available use generate_matrix_num
# matrix = generate_matrix_num(2,3,0,100,'float')
# n = float(input('Enter a value: ))

# Else use the code below
matrix = [[6954, 345, 3697], [9279, 9892, 9094]]
# You could get input for n
n = 1000

loc = find_less(matrix, n)

print(f'Matrix: {matrix}')
print(f'Location of the first value smaller than {n}: {loc}')