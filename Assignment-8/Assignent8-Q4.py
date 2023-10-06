# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 00:31:27 2023

@author: taylor headen
"""
import matplotlib.pyplot as plt
import numpy as np


file = np.loadtxt('fruit.txt')
a= np.sum(file[:,0])
o= np.sum(file[:,1])
b= np.sum(file[:,2])
p= np.sum(file[:,3])
 

fig , ax = plt.subplots()
ax.pie([a,o,p,b], (0.1, 0, 0, 0), labels= ['Apples', 'Oranges', 'Pears','Bananas'], autopct = '%1.1f%%', shadow=True, startangle=90, colors=['#66b3ff','#99ff99','#ff9999','mediumpurple'])
plt.title('Relative proportions of the fruits')
plt.savefig('fruit-piechart')