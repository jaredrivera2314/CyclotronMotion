# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 19:31:11 2018

@author: Hassan Farhat
"""

#Import Libraries
import numpy as np
import math as math 
import matplotlib.pyplot as plt

#Initializing Variables
F=1
m=1
t=60
i=0
dt=0.01
dx=0.01
n = int (t/dt)  #This step was important because the floats can be used as counters
a = F/m
v = []
x = []
t = []
xRHS = []
xLHS = []

#Interating and calculating the velocity in time steps
for i in range(0, n):
    # .append addes a new position in a defined array
    v.append(i)
    t.append(i)
    x.append(i)
    xRHS.append(i)
    xLHS.append(i)
    v[i]= a*dt
    t[i]=i
    
    if i == 0:
        xLHS[i] = v[i]*t[i] 
        xRHS[i] = 0
        x[i] = xLHS[i]
    elif i == n:
        xRHS[i] = v[i]*t[i] 
        xLHS[i] = 0
        x[i] = xRHS[i]
    else:
        xLHS[i] = v[i]*t[i] 
        xRHS[i] = v[i-1]*t[i]
        x[i] = (0.5)*(xRHS[i] + xLHS[i])
        
#Plot the graph of time and position
plt.plot(x,t)
plt.xlabel('Position')
plt.ylabel('Time')
plt.title('Force on a box')