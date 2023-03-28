# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:46:21 2023

@author: taylor headen
Quiz 2 question 2
"""

def factorial(n):

    if n <= 0:

        return 1

    return n * factorial(n-1)

def fac_list(ls, low =0, high =10):
    sol =[]
    for ele in ls:
        if low < ele <= high :
            sol.append(factorial(ele))
        
    return sol
            
print(fac_list([3, -1, 1, 7, 11, 8]))

print(fac_list([3, -1, 1, 7, 11, 8], low=2, high=7))