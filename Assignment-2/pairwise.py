# -*- coding: utf-8 -*-



import itertools


        
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

