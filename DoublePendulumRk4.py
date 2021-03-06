import numpy as np
import math as math 
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib import animation
import scipy.integrate as integrate

g=9.81 #m/s^2
class mass:
	def __init__(self,m,armlength,angle,angularvelocity):
			self.m=m #mass in kg
			self.armlength=armlength
			self.angle=angle
			self.angularvelocity=angularvelocity
m1=mass(1,1,np.pi/6,0)
m2=mass(1,1,0,0)


InitEnergy=-(m1.m+m2.m)*g*m1.armlength*np.cos(m1.angle)-m2.m*g*m2.armlength*np.cos(m2.angle)+0.5*m1.m*(m1.armlength**2)*(m1.angularvelocity**2)+0.5*m2.m*((m1.armlength**2)*(m1.angularvelocity**2)+(m2.armlength**2)*(m2.angularvelocity**2)+2*m1.armlength*m2.armlength*m1.angularvelocity*m2.angularvelocity*np.cos(m1.angle-m2.angle))
print (InitEnergy)

theta1doubledot=-(g*(2*m1.m+m2.m)*np.sin(m1.angle)+g*m2.m*np.sin(m1.angle-2*m2.angle)+2*m2.m*(m2.armlength*m2.angularvelocity**2+m1.armlength*(m1.angularvelocity**2)*np.cos(m1.angle-m2.angle))*np.sin(m1.angle-m2.angle))/(2*m1.armlength*(m1.m+m2.m-m2.m*(np.cos(m1.angle-m2.angle))**2))

theta2doubledot=((m1.armlength*(m1.m+m2.m)*m1.angularvelocity**2+g*(m1.m+m2.m)*np.cos(m1.angle)+m2.armlength*m2.m*(m2.angularvelocity**2)*np.cos(m1.angle-m2.angle))*np.sin(m1.angle-m2.angle))/(m2.armlength*(m1.m+m2.m-(m2.m*(np.cos(m1.angle-m2.angle)**2))))

def a1(angle1pos,angle1velocity,angle2pos,angle2velocity):
	aa1=-(g*(2*m1.m+m2.m)*np.sin(angle1pos)+g*m2.m*np.sin(angle1pos-2*angle2pos)+2*m2.m*(m2.armlength*angle2velocity**2+m1.armlength*(angle1velocity**2)*np.cos(angle1pos-angle2pos))*np.sin(angle1pos-angle2pos))/(2*m1.armlength*(m1.m+m2.m-m2.m*(np.cos(angle1pos-angle2pos))**2))
	return aa1

def a2(angle1pos,angle1velocity,angle2pos,angle2velocity):
	aa2=((m1.armlength*(m1.m+m2.m)*angle1velocity**2+g*(m1.m+m2.m)*np.cos(angle1pos)+m2.armlength*m2.m*(angle2velocity**2)*np.cos(angle1pos-angle2pos))*np.sin(angle1pos-angle2pos))/(m2.armlength*(m1.m+m2.m-(m2.m*(np.cos(angle1pos-angle2pos)**2))))
	return aa2


def rk4(iterations, desired_value):

    RK4_pos1 = []
    RK4_vel1 = []
    RK4_pos2 = []
    RK4_vel2 = []
    RK4_energy=[]



    h=.01

    theta10=m1.angle
    thetadot10=m1.angularvelocity
    theta20=m2.angle
    thetadot20=m2.angularvelocity

    for i in range(iterations):
    	global value1, value2, valueE


        theta11=thetadot10*h
        theta21=thetadot20*h
        thetadot11=a1(theta10,thetadot10,theta20,thetadot20)*h
        thetadot21=a2(theta10,thetadot10,theta20,thetadot20)*h

        theta12=(thetadot10+((thetadot11)/2))*h
        theta22=(thetadot20+((thetadot21)/2))*h
        thetadot12=a1(theta10+(theta11/2),thetadot10+(thetadot11/2),theta20+(theta21/2),thetadot20+(thetadot21/2))*h
        thetadot22=a2(theta10+(theta11/2),thetadot10+(thetadot11/2),theta20+(theta21/2),thetadot20+(thetadot21/2))*h

        theta13=(thetadot10+(thetadot12/2))*h
        theta23=(thetadot20+(thetadot22/2))*h
        thetadot13=a1(theta10+(theta12/2),thetadot10+(thetadot12/2),theta20+(theta22/2),thetadot20+(thetadot22/2))*h
        thetadot23=a2(theta10+(theta12/2),thetadot10+(thetadot12/2),theta20+(theta22/2),thetadot20+(thetadot22/2))*h

        theta14=(thetadot10+thetadot13)*h
        theta24=(thetadot20+thetadot23)*h
        thetadot14=a1(theta10+theta13,thetadot10+thetadot13,theta20+theta23,thetadot20+thetadot23)*h
        thetadot24=a2(theta10+theta13,thetadot10+thetadot13,theta20+theta23,thetadot20+thetadot23)*h

        thetadot10=thetadot10+((thetadot11+(2*thetadot12)+(2*thetadot13)+thetadot14)/6.0)
        thetadot20=thetadot20+((thetadot21+(2*thetadot22)+(2*thetadot23)+thetadot24)/6.0)
        theta10=theta10+((theta11+(2*theta12)+(2*theta13)+theta14)/6.0)
        theta20=theta20+((theta21+(2*theta22)+(2*theta23)+theta24)/6.0)

        PotentialEnergy0=-(m1.m+m2.m)*g*m1.armlength*np.cos(theta10)-m2.m*g*m2.armlength*np.cos(theta20)
        KineticEnergy0=0.5*m1.m*(m1.armlength**2)*(thetadot10**2)+0.5*m2.m*((m1.armlength**2)*(thetadot10**2)+(m2.armlength**2)*(thetadot20**2)+2*m1.armlength*m2.armlength*thetadot10*thetadot20*np.cos(theta10-theta20))
        TotalEnergy=KineticEnergy0+PotentialEnergy0
#ENERGY=-(m1.m+m2.m)*g*m1.armlength*np.cos(m1.armlength)-m2.m*g*m2.armlength*np.cos(m2.armlength)+0.5*m1.m*(m1.armlength**2)*(m1.angularvelocity**2)+0.5*m2.m*((m1.armlength**2)*(m1.angularvelocity**2)+(m2.armlength**2)*(m2.angularvelocity**2)+2*m1.armlength*m2.armlength*m1.angularvelocity*m2.angularvelocity*np.cos(m1.angle-m2.angle))


        if desired_value == 'velocity':
            RK4_vel1.append(thetadot10)
            valuevel1 = RK4_vel1
            RK4_vel2.append(thetadot20)
            valuevel2 = RK4_vel2

        elif desired_value == 'position':
            RK4_pos1.append(theta10)
            value1 = RK4_pos1
            RK4_pos2.append(theta20)
            value2 = RK4_pos2

        elif desired_value=="energy":
            RK4_vel1.append(thetadot10)
            valuevel1 = RK4_vel1
            RK4_vel2.append(thetadot20)
            valuevel2 = RK4_vel2
            RK4_pos1.append(theta10)
            value1 = RK4_pos1
            RK4_pos2.append(theta20)
            value2 = RK4_pos2
            RK4_energy.append(TotalEnergy)
            valueE=RK4_energy



    return value1,value2
h=0.01
dt=h
iterations=3000
t=np.arange(0.0,iterations*dt,dt)

rk4(iterations,"energy")

value1x=[None]*iterations
for i in range(0,len(value1)):
	value1x[i]=m1.armlength*np.sin(value1[i])
value1y=[None]*iterations
for i in range(0,len(value1)):
	value1y[i]=-m1.armlength*np.cos(value1[i])
value2x=[None]*iterations
for i in range(0,len(value2)):
	value2x[i]=m1.armlength*np.sin(value1[i])+m2.armlength*np.sin(value2[i])
value2y=[None]*iterations
for i in range(0,len(value2)):
	value2y[i]=-m1.armlength*np.cos(value1[i])-m2.armlength*np.cos(value2[i])



fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-10, 10), ylim=(-10, 5))
ax.grid()
#Goes to 30 seconds of simuulation
line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text


def animate(i):
    thisx = [0, value1x[i], value2x[i]]
    thisy = [0, value1y[i], value2y[i]]
    time_text.set_text(time_template % (i*dt))

    line.set_data(thisx, thisy)
    return line, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(value1y)),
                              interval=25, blit=True, init_func=init)

plt.show()
#print (valueE)
#print(valueE[0])
#print(valueE[iterations-1])

#print(DeltaE)
#print (valueE[0])
#print(InitEnergy)
#InitEnergy and valueE[0] ARE NOT EQUIVALENT valueE[0] CORRESPONDS TO time=0+dt

EnergyArray=np.array(valueE)
print (EnergyArray) #Loses some digits, down to 8 digits after decimal place
DeltaEArray=EnergyArray-InitEnergy
print (DeltaEArray)



TimeArray=np.arange(0,(dt*iterations)+dt,dt) #This is one extra element

EnergyArray=np.insert(EnergyArray,[0],[InitEnergy])

print (EnergyArray)

EnergyDifference=EnergyArray-InitEnergy
print (EnergyDifference)

line,=plt.plot(TimeArray,EnergyDifference,lw=2)
plt.show()
