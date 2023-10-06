# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 22:31:03 2023

@author: taylor headen
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches


blue_patch1 = mpatches.Patch(color='blue', label='sin(x)')
red_patch1 = mpatches.Patch(color='red', label='2 sin(x)')

plt.subplot(1,2 ,1)
x1 = np.linspace(-2*np.pi, 2*np.pi, num=40)
y1 = np.sin(x1)
plt.plot(x1,y1,  'b-')
plt.plot(x1,2*y1,'r--')
plt.axis([-2*np.pi, 2*np.pi, -2.5, 2.5])
plt.title(r'$sin(x)$ and $2sin(x)$')
plt.grid(True)
plt.legend(handles=[blue_patch1, red_patch1]) 



blue_patch1 = mpatches.Patch(color='blue', label='cos(x)')
red_patch1 = mpatches.Patch(color='red', label='2 cos(x)')

plt.subplot(1,2,2)
x2 = np.linspace(-2*np.pi, 2*np.pi, num=40)
y2 = np.cos(x2)
plt.plot(x2,y2,  'b-')
plt.plot(x2,2*y2,'r--')
plt.axis([-2*np.pi, 2*np.pi, -2.5, 2.5])
plt.title(r'$cos(x)$ and $2cos(x)$')
plt.grid(True)
plt.legend(handles=[blue_patch1, red_patch1]) 



