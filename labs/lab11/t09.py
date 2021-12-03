"""
------------------------------------------------------------------------
CP104 Lab 11, Task 09
------------------------------------------------------------------------
Author: Your Full Name
ID:     190400000
Email:  yourlaurieremail@mylaurier.ca
__updated__ = "2021-12-02"
------------------------------------------------------------------------
"""
# from functions import generate_matrix_char
from functions import count_frequency

# If available use generate_matrix_char
# char = input('Enter a character: ')
# matrix = generate_matrix_char(2,3)

# Else use the code below
matrix = [['a', 'y', 'j'], ['k', 's', 'l']]
# You could ask for input for char
char = 'y'

count = count_frequency(matrix, char)

print(f'Matrix: {matrix}')
print(f'{char} appears {count} time(s)')