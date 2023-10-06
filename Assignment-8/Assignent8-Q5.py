# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 11:07:40 2023

@author: taylor headen
"""
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

def scatterplot_3d(filename, ax, marker, color):
    data = np.loadtxt(filename)
        
    x = data[:, 0]
    y = data[:, 1]
    z = data[:, 2]
    radius = np.pi * (data[:, 3] ** 2)
    ax.scatter(x, y, z, marker=marker, color=color)
    

ax = plt.axes(projection="3d")
scatterplot_3d('data1.txt', ax, '>', 'c')
scatterplot_3d('data2.txt', ax, '<', 'k')
plt.show()
