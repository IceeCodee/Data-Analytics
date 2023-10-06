# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 11:48:13 2023

@author: taylor headen
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn-pastel')
fig = plt.figure()
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=10)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    theta = np.linspace(0, 2*np.pi, 1000)
    x = np.cos(theta[i:i+4])
    y = np.sin(theta[i:i+4])
    line.set_data(x, y)
    return line,
anim = FuncAnimation(fig, animate, init_func=init,
               frames=1000, interval=2, blit=True)
writergif = animation.PillowWriter(fps=30) 
anim.save('osc.gif', writer=writergif)
