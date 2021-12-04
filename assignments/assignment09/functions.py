"""
------------------------------------------------------------------------
CP104 Assignment 09, Functions
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2021-12-03"
------------------------------------------------------------------------
"""


def file_head(fh, linecount):
    """
    -------------------------------------------------------
    Prints first linecount lines of fh. Line numbering starts at 0.
    If length of file is shorter than linecount, stops printing after
    last line of file.
    Use: file_head(fh, linecount)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
        linecount - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    current_line = 0
    line_content = fh.readline()
    while current_line < linecount and line_content != '':
        print(f'{line_content}', end='')
        line_content = fh.readline()
        current_line += 1
    return


def file_integers(fh):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: numbers = file_integers(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process ( (file handle - open for reading)
    Returns:
        numbers - a list of integers from fh (list of int)
    -------------------------------------------------------
    """
    numbers = []
    for i in fh:
        split_values = i.split(',')
        for j in split_values:
            if j.isnumeric():
                if int(j) > 0:
                    numbers.append(int(j))
    return numbers


def file_stats(fh):
    """
    -------------------------------------------------------
    Evaluates the contents of a file.
    Use: ucount, lcount, dcount, wcount = file_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
    Returns:
        ucount - The number of uppercase letters in the file (int)
        lcount - The number of lowercase letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of whitespace characters in the file (int)
    -------------------------------------------------------
    """
    ucount, lcount, dcount, wcount = 0, 0, 0, 0
    for i in fh:
        for j in i:
            if j.isdigit():
                dcount += 1
            elif j.isupper():
                ucount += 1
            elif j.islower():
                lcount += 1
            else:
                wcount += 1
    return ucount, lcount, dcount, wcount


def flatten(matrix):
    """
    -------------------------------------------------------
    Flatten the contents of 2D list matrix. A 'flattened' list is a
    2D list that is converted into a 1D list by rows.
    matrix must be unchanged.
    Use: flat = matrix_flatten(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of int)
    Returns:
        flat - the flattened version of matrix (list of int)
    -------------------------------------------------------
    """
    flat = []
    for i in matrix:
        for j in i:
            flat.append(j)
    return flat


def matrix_rotate_right(matrix):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    a must be unchanged.
    Use: rotated = matrix_rotate_right(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2d list of int/float)
    Returns:
        rotated - the rotated version of matrix (2D list of int/float)
    -------------------------------------------------------
    """
    rotated = []
    for i in range(len(matrix[0])):
        temp_list = []
        for j in range((len(matrix) - 1), -1, -1):
            temp_list.append(matrix[j][i])
        rotated.append(temp_list)
    return rotated


def get_addresses(fh):
    """
    -------------------------------------------------------
    Reads a addresses from fh into a list of addresses.
    Addresses are stored in fh in the form:
        name
        street
        city
        postal code
        --
    Each address in the list of addresses is a list of the form:
    [name, street, city, postal code]
    Use: addresses = get_addresses(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
    Returns:
        addresses - the addresses from fh (list of str)
    -------------------------------------------------------
    """
    addresses = []
    temp_list = []
    for i in fh:
        if i.strip() == '--':
            addresses.append(temp_list)
            temp_list = []
        else:
            temp_list.append(i.strip())
    return addresses
