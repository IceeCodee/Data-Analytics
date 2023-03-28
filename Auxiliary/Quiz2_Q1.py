# -*- coding: utf-8 -*-
"""

Quiz 2 
    question 2

Call factorial function (given below) in the definition of a function fac_list() that takes a list of integers, ls, and
two integer arguments, low (default 0) and high (default 10). It returns the list of factorials of
the items in ls that are between low and high inclusive. (The items in ls, not their factorials,
are between low and high inclusive.) 
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
