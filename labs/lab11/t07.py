"""
------------------------------------------------------------------------
CP104 Lab 11, Task 07
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2021-12-02"
------------------------------------------------------------------------
"""
# from functions import generate_matrix_num
from functions import find_position

# If available use generate_matrix_num
# matrix = generate_matrix_num(2,3,0,100,'float')

# Else use the code below
matrix = [[6954, 345, 3697], [9279, 9892, 9094]]

s_loc, l_loc = find_position(matrix)

print(f'Matrix: {matrix}')
print(f'Location of Smallest Value: {s_loc}')
print(f'Location of Largest Value: {l_loc}')