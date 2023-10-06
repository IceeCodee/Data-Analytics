# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 00:14:13 2023

@author: taylor headen
"""
import numpy as np
import random
import matplotlib.pyplot as plt


x= np.random.normal(2, 0.5, 1000)
plt.hist(x, bins=50, histtype='step')
plt.title('Lengths of Dogs in Greensboro in feet')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()
plt.savefig('dog-length-gso')