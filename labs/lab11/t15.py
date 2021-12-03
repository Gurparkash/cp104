"""
------------------------------------------------------------------------
CP104 Lab 11, Task 15
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2021-12-02"
------------------------------------------------------------------------
"""
# from functions import generate_matrix_num
from functions import matrix_equal

# If available use generate_matrix_num
# matrix1 = generate_matrix_num(2,3,0,100,'float')
# matrix2 = generate_matrix_num(2,3,0,100,'float')
# or generate_matrix_char
# matrix1 = generate_matrix_char(2,3)
# matrix2 = generate_matrix_char(2,3)

# Else use the code below
matrix1 = [[6954, 345, 3697], [9279, 9892, 9094]]
matrix2 = [[6954, 345, 3697], [9279, 9892, 9094]]

equal = matrix_equal(matrix1, matrix2)

print(f'Matrix 1: {matrix1}')
print(f'Matrix 2: {matrix2}')

if equal:
    print('Matricies are equal')
else:
    print('Matricies are unequal')