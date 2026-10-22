#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 20:57:15 2026

@author: marienavestadgundersen
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -x**2-5


x = np.linspace(-10, 10, 200)

y=f(x)

plt.close('all')
plt.figure(1)
plt.plot(x,y)
plt.legend()
plt.title('f(x)=-x^2-5')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()



