# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 12:16:52 2023

@author: taylor headen
comp 651 
assignment 2

"""

import itertools


def min_max(*lst):
    """ Finds the max element and min element in a list
    
    This function is passed any number of integer arguments and returns a tuple 
    with the smallest and largest among them. If only one argument is provided 
    the two elements will be the same. If no arguments are provided it will 
    return an empty tuple

    
    Args: 
        *lst: A list that is unpacked
        
    Returns:
        A tuple that contains the smallest and largest elements in the list
    """
    if len(lst) ==0:
        return ()
    lrg =0
    sml = lst[0]
    for i in lst:
        if i > lrg:
            lrg = i
    for i in lst:
        if i < sml:
            sml = i
    return sml , lrg

def alternates(lst, start=0):
    """Finds an sequence of alternating elements of a given list
    
    This function returns a 2-tuple of lists. The first list has every 
    other element of the list ls passed in starting at index 'start'
    and the second list has the other elements of ls starting at 'start + 1'
    The default value for start is 0. Use slicing. To use slicing to get every other
    element of a list
    
    Args:
        lst: A list of elements
        start: An integer that indicates the starting index
        
    Returns:
        A 2-tuple of lists with every other element of the list and the other has the
        other elements of the list
    """
    firsthalf = lst[start::2]
    secondhalf = lst[start +1::2]
    return [firsthalf,secondhalf] 

def list_diff(lst, lst1):
    """ Finds the difference between two lists
    
    This function is passed two list of integers and returns a list of all the integers
    in the first list that are not in the second list.
    
    Args:
        lst: A list of elements
        lst1: A list of elements
    
    Returns:
        A list of all integers in lst that are not in lst1
    
    """
    newlst = filter(lambda x: x not in lst1 , lst)
    return list(newlst)

def sum_pairs(lst):
    """ Sums up adjancent pairs for given list
    
    This function returns the result of mapping this function over the 
    list of adjacent pairs in the list passed in.
    
    Args: 
        lst: A list of elements
        
    Returns:
        A mapping of this function over the list of adjancent pairs
    
    
    """
    def add_double_2nd(t):
        """ Doubles the second element and adds it to the first
        
        This functions is passed a 2-tuple t of integers, returns 
        t[0] + 2*t[1]. 
        
        Args: 
            t: A 2-tuple t
            
        Returns:
            t[0] + 2*t[1]
        """
        return t[0] + 2*t[1]
    return list(map(add_double_2nd, pairwise(lst)))

def sum_pairs1(lst):
    """Sums up adjancent pairs for given list
    
    This function returns the result of mapping this function over the 
    list of adjacent pairs in the list passed in using a lambda function
    instead of a local function.
    
    Args: 
        lst: A list of elements
        
    Returns:
        A mapping of this function over the list of adjancent pairs
    
    """
    return list(map(lambda t: t[0] + 2*t[1], pairwise(lst)))

def pairwise(iterable):
    """ Return the zipped list of adjacent pairs of iterable 
    
    This returns a zipped list with, for each pair of items i1, i2 
    at adjacent positions in iterable,the tuple (i1, i2). Note that
    one may iterate over the zipped list.
    
    Args:
        iterable: An iterable whose adjacency pairs are included
    
    Returns:
        A zipped list of adjacent pairs of iterable
        
    """
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

def cum_sum_pairs(lst):
    """Outputs a list of 2-element tuples with the given number and running sum
    
    This function is passed the running list of integers and returns a list 
    of pairs (2-element tuples), where the first element of a pair is the original 
    number and the second is the sum of all previous numbers in the list 
    (0 for the first list element).
    
    Args:
        lst: A list of elements
        
    Returns: 
        A list of pairs where the first element of a pair is the original number 
        and the second is a running sum of all previous numbers.
            
    """
    newlst = [ (lst[i] , sum(lst[:i])) for i in range(len(lst))]
    return newlst

def pairs_smaller(lst):
    """ Outputs a list of 2-element tuples with the given number and a list
        of elements smaller than that number
        
    This funciton is passed the running list of integers and returns a list 
    of pairs (2-element tuples), where the first element in the pair, call it x,
    is the original number, and the second is a list of all those numbers in the
    running list that are less than x

    Args:
        lst : A list of elements.

    Returns:
        A list of pairs where the first element in the pair is the original number, 
        and the second is a list of all those numbers in the running list that are 
        less than that number. 

    """
    res= [(x,[ y for y in lst if y < x]) for x in lst]
    return res

if __name__=="__main__":
    lst = eval(input("Input a list: ")) 
    print('The smallest and largest elements: ', min_max(*lst)) 
    print('The smallest and largest of no arguments: ', min_max()) 
    start = int(input('The start index, 0 for the default: ')) 
    print('The alternating sequences are ', alternates(lst, start=start) if start else alternates(lst)) 
    start = int(input('The start index, 0 for the default: ')) 
    print('The alternating sequences are ', alternates(lst, start=start) if start else alternates(lst)) 
    lst1 = eval(input("Input another list: ")) 
    print('The difference of the two lists: ', list_diff(lst, lst1)) 
    print("The result of adding 1st of a pair to 2 X 2nd of a pair: ", sum_pairs(lst)) 
    print("The same result, using a lambda: ", sum_pairs1(lst)) 
    print('The first list of pairs as described: ', cum_sum_pairs(lst)) 
    print('The second list of pairs as described: ', pairs_smaller(lst))  

    