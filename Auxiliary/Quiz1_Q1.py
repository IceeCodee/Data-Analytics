# -*- coding: utf-8 -*-
"""
QUIZ 1
  Problem1 
  
Write code to prompt for and read in (with the requisite conversion) a 
list of at least three numbers. The idea is to slice the list into three 
parts. So, we need two integers, one for the first index in the second part 
of the list, and one for the first index of the third (and last) part. So, 
separately prompt for and read in (with the requisite conversion) these two
integers, and then print the three parts of the list with text identifying
each as the first, middle, or last part. (This is a slicing problem.) You do
not need to check that a list of numbers is correctly input or that the integer
indices are in range and ordered. (Note that a list of numbers typed at the 
console can be input and converted to a list of integers (as opposed to the 
string returned as input) with eval(input('My prompt: '). Also, an integer 
typed at the console can be input and converted to an integer with 
eval(input('My other prompt: '); here we could use int() instead of eval().) 
The following is an example run.

Enter a list of at least 3 numbers: [0,2,4,6,8,10,12,14,16,18]

Enter the lower dividing index: 4

Enter the higher dividing index: 7

The first part:  [0, 2, 4, 6]

The middle part:  [8, 10, 12]

The last part:  [14, 16, 18]
"""

lst = eval(input("Enter a list of at least 3 numbers: "))
low = eval(input("Enter lower dividing index: "))
high  = eval(input("Enter lower dividing index: "))

first = lst[0:low]
mid = lst[low:high]
last = lst[high:]

print("The first part: ", first)
print("The middle part: ", mid)
print("The last part: ", last)
