"""
------------------------------------------------------------------------
CP104 Assignment 09, Task 01
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2021-12-03"
------------------------------------------------------------------------
"""
from functions import file_head

file = input('Enter a filename: ')
line_count = int(input('Enter a number: '))

file = open(file, 'r', encoding='utf-8')

file_head(file, line_count)

file.close()
