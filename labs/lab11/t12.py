"""
------------------------------------------------------------------------
CP104 Lab 11, Task 12
------------------------------------------------------------------------
Author: Your Full Name
ID:     190400000
Email:  yourlaurieremail@mylaurier.ca
__updated__ = "2021-12-02"
------------------------------------------------------------------------
"""
from functions import find_word_diagonal

# I advise that you use this or make your own with a word included
matrix = [['c', 'c', 'd'], ['a', 'a', 't'], ['t', 't', 't']]
# You can ask for input for the word
word = 'cat'

found = find_word_diagonal(matrix, word)

print(f'Matrix: {matrix}')
if found:
    print(f'{word} was on the diagonal')
else:
    print(f'{word} was not on the diagonal')