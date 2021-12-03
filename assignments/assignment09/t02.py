"""
------------------------------------------------------------------------
CP104 Assignment 09, Task 02
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2021-12-03"
------------------------------------------------------------------------
"""
from functions import file_integers

fh = open('numbers.txt', 'r', encoding='utf-8')

numbers = file_integers(fh)

fh.close()

print(type(numbers))
print(type(numbers[0]))
print(f'Numbers: {numbers}')
