# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 22:39:54 2023

@author: taylor headen
COMP 651
Problem 1

write a code that keeps a running sum of numbers prompted for at the console and input
stop when the user enters 0, and output the sum
"""

#prompt for user input, initialized variable
x = eval(input("Enter a number: ")) 
total = 0

#keep running total of number entered
#stops when a 0 is entered
while( x !=0):
    total = total + x
    x = eval(input("Enter another number: "))
    
#print the sum
else:
    print("Sum is ",total)
    
