import numpy as np
import math as math 
import matplotlib.pyplot as plt


#Force on block
#Assigning set up variables and equations

F=1.0
x=0.0
v=0.0
m=2.0
t=0.0
a=F/m
xl=0.0
xr=0.0

#Defining arrays for position and time for future plotting
xmatrix=[]
tmatrix=[]





##
## v=a*t
## x=a*(t**2)
##
#Looping parameters
steps=1000
timeinterval=10.0/steps #10 second time frame, looking at 1000 different slices of those 10 seconds

#Mixture of rectangular methods for integration
#Looping to find v and x
for i in range(0,steps):
	if i==0:
		v=v+(a*timeinterval)
		xr=x+(v*timeinterval)
		x=xr
		t=t+timeinterval
		xmatrix.append(x)
		tmatrix.append(t)
	elif i!=0 & i!=(steps-1):
		xl=x+(v*timeinterval)
		v=v+(a*timeinterval)
		xr=x+(v*timeinterval)
		x=(xl+xr)/2
		t=t+timeinterval
		xmatrix.append(x)
		tmatrix.append(t)
	elif i==steps-1:
		xl=x+(v*timeinterval)
		v=v+(a*timeinterval)
		xr=x+(v*timeinterval)
		x=(xl+xr)/2
		t=t+timeinterval
		xmatrix.append(x)
		tmatrix.append(t)

print(xmatrix)
#Plotting
plt.plot(tmatrix,xmatrix)
plt.xlabel('Time')
plt.ylabel('X-Position')
plt.show()