# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 20:32:20 2023

@author: taylor headen
COMP 651 
question 3

Write code the prompts for and reads a list of integers
it splits the list in half 
outputs the half with the larger sum

"""
#ask for user input
lst = eval(input("Enter a list of number: "))

''' find where to split the list
if the list is of odd length, it includes 1 more number in the
second half then in the first'''
split= (len(lst)) // 2
half1 = lst[:split]
half2 = lst[split:]

#find the sum of both halves of the list
sumhalf1 = sum(half1)
sumhalf2 = sum(half2)

#for loop to return the bigger half.
if sumhalf1 > sumhalf2:
    print(half1)
else:
    print(half2)


