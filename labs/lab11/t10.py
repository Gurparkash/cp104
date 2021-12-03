"""
------------------------------------------------------------------------
CP104 Lab 11, Task 10
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2021-12-02"
------------------------------------------------------------------------
"""
from functions import find_word_horizontal

# I advise that you use this or make your own with a word included
matrix = [['c', 'a', 't'], ['c', 'a', 't'], ['d', 'o', 'g']]
# You can ask for input for the word
word = 'cat'

rows = find_word_horizontal(matrix, word)

print(f'Matrix: {matrix}')
print(f'The location(s) of {word}: {rows}')