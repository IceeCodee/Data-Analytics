# -*- coding: utf-8 -*-
"""

Quiz 2 
    question 1

Write a Python function find_key() that takes two arguments, a dictionary and a possible
value in that dictionary. It returns the key for that value in the dictionary if the value indeed
occurs in the dictionary; otherwise, it returns None. If the value occurs several times in the
dictionary, any associated key will do.
"""

def find_key(d, num):
    for k , n  in d.items():
        if num == n:
           return k
    return None
          
d = {'a': 1, 'b': 5, 'c': 3, 'd': 4}

print(find_key(d, 3))

print(find_key(d, 2))
