# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
Write code that prompts for and inputs an integer, say, div. It then repeatedly prompts for and inputs a number, assigned, say, to n, until a 0 is entered for n. For each value of n, if n ≤ div, then n is added to sm1 (which is initially 0); otherwise, n is added to sm2 (also initially 0). After the loop, print the values of sm1 and sm2. (Note that an integer typed at the console can be input and converted to an integer with eval(input('My prompt: ')). You could use int() instead of eval().) The following is an example run.

Enter the dividing integer: 5

Enter a number: 2

Enter a number: 7

Enter a number: 3

Enter a number: 8

Enter a number: 0

5 15

"""
sm1 = 0 
sm2 = 0
div= eval(input('Enter the dividing interger: ' ))
n = eval(input('Enter a number: '))

while (n != 0):
    if n <= div:
        sm1 +=n
    else:
        sm2 += n
        
    n = eval(input('Enter a number: '))
print(sm1, sm2)
    
