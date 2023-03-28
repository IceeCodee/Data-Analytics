# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 10:40:55 2023

@author: taylor headen
Quiz 2 question 1

"""

def find_key(d, num):
    for k , n  in d.items():
        if num == n:
           return k
    return None
         
    
            
        
             
        
        
d = {'a': 1, 'b': 5, 'c': 3, 'd': 4}

print(find_key(d, 3))

print(find_key(d, 2))
