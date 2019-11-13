#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 00:17:18 2019

@author: li
"""

import numpy as np 
import matplotlib.pyplot as plt

x0  =  0
def euler(y0,xf,step):
    n=int((xf-x0)/step)
    x  = np.linspace(x0 , xf , n+1)
    y  =  np.zeros(n+1)
    y[0] = y0

    
    for i in range(1,n):
        y[i]= -step**2*y[i-1]+y[i-1]


    plt.plot(x, y)
  
    plt.show()
    return y
    


a=euler(1,1000,0.001)
b=euler(0,1000,0.001)
plt.plot(a,b)
plt.show()