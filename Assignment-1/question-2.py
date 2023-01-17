# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 10:00:02 2023

@author: taylor headen
COMP 651
question 2
A palindrone is a wrod that reads the same  forwards and backwards

one way to contruct such strings of letters:
    start with the empty string
    repeatedly add the same letter to the front and back
    
Write a python code to produce pseudo-palindromes in this way
(only of even length)
Prompt for and input a letter at a time, enter an empty string to stop
"""

#initialze string and prompt for user input
pseudo = ''
string = input("Enter a letter: ")

#concat the letters entered by the user into one string
#stops when empty string is entered
while(string != ''):
    pseudo += string
    string = input("Enter another letter: ")

#print finalized pseudo palindrome 
else:
    print(pseudo[::-1] + pseudo)
    





