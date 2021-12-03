"""
------------------------------------------------------------------------
CP104 Lab 11, Task 06
------------------------------------------------------------------------
Author: Your Full Name
ID:     190400000
Email:  yourlaurieremail@mylaurier.ca
__updated__ = "2021-12-02"
------------------------------------------------------------------------
"""
# from functions import generate_matrix_num
from functions import stats

# If available use generate_matrix_num
# matrix = generate_matrix_num(2,3,0,100,'float')

# Else use the code below
matrix = [[6954, 345, 3697], [9279, 9892, 9094]]

smallest, largest, total, average = stats(matrix)

print(f'Matrix: {matrix}')
print(f'Smallest Values: {smallest}')
print(f'Largest Values: {largest}')
print(f'Total: {total}')
print(f'average: {average}')