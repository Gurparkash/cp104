"""
------------------------------------------------------------------------
CP104 Lab 11, Task 11
------------------------------------------------------------------------
Author: Your Full Name
ID:     190400000
Email:  yourlaurieremail@mylaurier.ca
__updated__ = "2021-12-02"
------------------------------------------------------------------------
"""
from functions import find_word_vertical

# I advise that you use this or make your own with a word included
matrix = [['c', 'c', 'd'], ['a', 'a', 'o'], ['t', 't', 'g']]
# You can ask for input for the word
word = 'cat'

cols = find_word_vertical(matrix, word)

print(f'Matrix: {matrix}')
print(f'The location(s) of {word}: {cols}')