"""
------------------------------------------------------------------------
CP104 Lab 11, Functions
------------------------------------------------------------------------
Author: Your Full Name
ID:     190400000
Email:  yourlaurieremail@mylaurier.ca
__updated__ = "2021-12-02"
------------------------------------------------------------------------
"""
from random import randint, uniform


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    # Initialize the matrix
    matrix = []
    for i in range(rows):
        temp_list = []
        for i in range(cols):
            if value_type == 'float':
                temp_list.append(uniform(low, high))
            # This could've been an else statement
            elif value_type == 'int':
                temp_list.append(randint(low, high))
        matrix.append(temp_list)
    return matrix


def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random lower case letter ('a' - 'z') values
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of str)
    -------------------------------------------------------
    """
    # Initialize the matrix
    matrix = []
    for i in range(rows):
        temp_list = []
        for i in range(cols):
            temp_list.append(chr(randint(97, 122)))
        matrix.append(temp_list)
    return matrix


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    print(f'          0', end='')
    for i in range(1, len(matrix[0])):
        print(f'      {i}', end='')
    print()
    for i in range(len(matrix)):
        print(f'   {i}', end='')
        for j in matrix[i]:
            if value_type == 'float':
                print(f'   {j:.2f}', end='')
            else:
                print(f'   {j:>4d}', end='')
        print()
    return


def print_matrix_char(matrix):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list of strings in a formatted table.
    Prints row and column headings.
    Use: print_matrix_char(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of strings (2D list)
    Returns:
        None.
    -------------------------------------------------------
    """
    print(f'          0', end='')
    for i in range(1, len(matrix[0])):
        print(f'      {i}', end='')
    print()
    for i in range(len(matrix)):
        print(f'   {i}', end='')
        for j in matrix[i]:
            print(f'      {j}', end='')
        print()
    return


def words_to_matrix(word_list):
    """
    -------------------------------------------------------
    Generates a 2D list of character values from the given
    list of words. All words must be the same length.
    Use: matrix = words_to_matrix(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a list containing the words to be placed in
            the matrix (list of string)
    Returns:
        matrix - a 2D list of characters of the given words
         in word_list (2D list of string).
    -------------------------------------------------------
    """
    # Initialize the matrix
    matrix = []
    for i in word_list:
        temp_list = []
        for j in i:
            temp_list.append(j)
        matrix.append(temp_list)
    return matrix


def stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
		Use: smallest, largest, total, average = stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    smallest = matrix[0][0]
    largest = matrix[0][0]
    num_values = 0
    total = 0
    for i in matrix:
        for j in i:
            num_values += 1
            total += j
            if j < smallest:
                smallest = j
            if j > largest:
                largest = j
    average = total / num_values
    return smallest, largest, total, average


def find_position(matrix):
    """
    -------------------------------------------------------
    Determines the first locations [row, column] of smallest and
    largest values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of of the row and column location of
            the largest value in matrix (list of int)
    -------------------------------------------------------
    """
    s_loc = [0, 0]
    l_loc = [0, 0]
    current_lowest = matrix[0][0]
    current_highest = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < current_lowest:
                current_lowest = matrix[i][j]
                s_loc = [i , j]
            elif matrix[i][j] > current_highest:
                current_highest = matrix[i][j]
                l_loc = [i , j]
    return s_loc, l_loc


def find_less(matrix, n):
    """
    -------------------------------------------------------
    Finds the location [row, column] of the first value in matrix
    that is smaller than a target value, n. If there is no such
    number in matrix, it should return an empty list.
    Use: loc = find_less(matrix, n)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
        n - the target value (float)
    Returns:
        loc - a list of the row and column location of
            the the first value smaller than n in values,
            an empty list otherwise (list of int)
    -------------------------------------------------------
    """
    loc = []
    i = 0
    not_done = True
    while i < len(matrix) and not_done:
        j = 0
        while j < len(matrix[i]) and not_done:
            if matrix[i][j] < n:
                loc = [i, j]
                not_done = False
            j += 1
        i += 1
    return loc


def count_frequency(matrix, char):
    """
    -------------------------------------------------------
    Count the number of appearances of the given character char
    in matrix.
    Use: count = count_frequency(matrix, char)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to search in it (2D list of str)
        char - character to search for it (str, len = 1)
    Returns:
        count - the number of appearances of char in the matrix (int)
    -------------------------------------------------------
    """
    # Initialize count to 0
    count = 0
    for i in matrix:
        for j in i:
            if j == char:
                count += 1
    return count


def find_word_horizontal(matrix, word):
    """
    -------------------------------------------------------
    Look for word in each row of the given matrix of characters.
    Returns a list of indexes of all rows that are equal to word.
    Returns an empty list if no row is equal to word.
    Use: rows = find_word_horizontal(matrix, word)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix of characters (2D list of str)
        word - the word to search for (str)
    Returns:
        rows - a list of row indexes (list of int)
    ------------------------------------------------------
    """
    rows = []
    for i in range(len(matrix)):
        current_word = ''
        for j in range(len(matrix[i])):
            current_word += matrix[i][j]
        if current_word == word:
            rows.append(i)
    return rows


def find_word_vertical(matrix, word):
    """
    -------------------------------------------------------
    Look for word in each column of the given matrix of characters.
    Returns a list of indexes of all column that are equal to word.
    Returns an empty list if no column is equal to word.
    Use: cols = find_word_vertical(matrix, word)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix of characters (2D list of str)
        word - the word to search for (str)
    Returns:
        cols - a list of column indexes (list of int)
    ------------------------------------------------------
    """
    cols = []
    for i in range(len(matrix[0])):
        current_word = ''
        for j in range(len(matrix)):
            current_word += matrix[j][i]
        if current_word == word:
            cols.append(i)
    return cols


def find_word_diagonal(matrix, word):
    """
    -------------------------------------------------------
    Returns whether word is on the diagonal of a square matrix
    of characters.
    Use: found = find_word_diagonal(matrix, word)
    -------------------------------------------------------
    Parameters:
        matrix - a 2d list of characters (2d list of str)
        word - the word to compare against the diagonal of matrix (str)
    Returns:
        found - True if word is on the diagonal of matrix,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    found = False
    diagonal = ''
    for i in range(len(matrix)):
        diagonal += matrix[i][i]
    if diagonal == word:
        found = True
    return found


def scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in matrix:
        for j in range((len(i))):
            temp_num = i[j] * num
            i[j] = temp_num
    return


