# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:12:55 2023

@author: taylor headen
COMP 651 
Question #2 of Assignment 3
"""

def file_sums(infile, outfile):
    """ Outputs a text file of integer sums from the input text file
    
    This function takes two parameters (infile and outfile) that are bound to file names.
    Each line in infile has one or more integers separated by whitespace. This function 
    writes as a line to outfile the sum of the integers on the corresponding line of
    infile. 
    

    Parameters
    ----------
    infile : a text file conatinins one or more intergers seperated
        by white space. This is to be read in by the program
    outfile : a text file where the output is be be stored 

    Returns
    -------
    out : a text file containing the sum of the integers on the
        corresponding line of the infile

    """
    with open(infile, 'r') as infile, \
        open(outfile, 'w') as outfile:
            for line in infile:
                lst = line.split()
                sumlst = sum([int(x) for x in lst])
                out = outfile.write(str(sumlst) + '\n')
    return out
    
    

print(file_sums('data.txt', 'output.txt'))

