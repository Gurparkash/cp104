"""
------------------------------------------------------------------------
CP104 Assignment 09, Task 03
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2021-12-03"
------------------------------------------------------------------------
"""
from functions import file_stats

fh = open('addresses.txt', 'r', encoding='utf-8')

ucount, lcount, dcount, wcount = file_stats(fh)
fh.close()

print(f'Number of uppercase letters: {ucount}')
print(f'Number of lowercase letters: {lcount}')
print(f'Number of digits in the file: {dcount}')
print(f'Number of whitespace characters in the file: {wcount}')
