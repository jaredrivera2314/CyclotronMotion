import matplotlib.pyplot as plt
#import numpy as np

F = 1 #N
m = 1 #kg
a = F/m #m/s/s

dx = .01 #m
dt = .01 #s
tot_t = 60 #s
tot_steps = int(tot_t/dt)

v = [0]*tot_steps
x = [0]*tot_steps
t = [0]*tot_steps

for i in range (0, tot_steps):
    if i>1:
        v[i] = v[i-1] + (a*dt)
    else:
        v[i] = a*dt
    t[i] = i
    if i == 0:
        x_LHS = v[i]*dt
        x_RHS = 0
        x[i]= x_LHS
    elif i > 0 and i < tot_steps-1:
        x_LHS = x[i-1] + v[i]*dt
        x_RHS = x[i-1] + v[i+1]*dt
        x[i] = (x_LHS + x_RHS)/2.0
    else:
        x_LHS = 0
        x_RHS = x[i-1] + v[i]*dt
        x[i] = x_RHS

plt.plot(t, x)
plt.show()

