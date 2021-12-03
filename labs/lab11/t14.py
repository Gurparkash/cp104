"""
------------------------------------------------------------------------
CP104 Lab 11, Task 14
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2021-12-02"
------------------------------------------------------------------------
"""
# from functions import generate_matrix_num
from functions import matrix_transpose

# If available use generate_matrix_num
# a = generate_matrix_num(2,3,0,100,'float')
# or generate_matrix_char
# a = generate_matrix_char(2,3)

# Else use the code below
a = [[6954, 345, 3697], [9279, 9892, 9094]]

b = matrix_transpose(a)

print(f'Matrix: {a} ')
print(f'Transposed Matrix: {b}')