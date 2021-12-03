"""
------------------------------------------------------------------------
CP104 Assignment 09, Task 06
------------------------------------------------------------------------
Author: Gurparkash Singh Randhawa
ID:     190406260
Email:  rand6260@mylaurier.ca
__updated__ = "2021-12-01"
------------------------------------------------------------------------
"""
from functions import get_addresses

fh = open('addresses.txt', 'r', encoding='utf-8')

addresses = get_addresses(fh)

fh.close()

for i in addresses:
    print(i)
