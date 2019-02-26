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
m1=mass(2,3,0,0)
m2=mass(2,3,np.pi/6,0)


def a1(angle1pos,angle1velocity,angle2pos,angle2velocity):
    aa1=-((g*m1.m*angle1pos)+(g*m2.m*angle1pos)-(g*m2.m*angle2pos))/(m1.armlength*m1.m)
    return aa1

def a2(angle1pos,angle1velocity,angle2pos,angle2velocity):
    aa2=-((-g*m1.m*angle1pos)-(g*m2.m*angle1pos)+(g*m1.m*angle2pos)+(g*m2.m*angle2pos))/(m2.armlength*m1.m)
    return aa2


def rk4(iterations, desired_value):

    RK4_pos1 = []
    RK4_vel1 = []
    RK4_pos2 = []
    RK4_vel2 = []


    h=.05

    theta10=m1.angle
    thetadot10=m1.angularvelocity
    theta20=m2.angle
    thetadot20=m2.angularvelocity

    for i in range(iterations):
        global value1, value2


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



        if desired_value == 'velocity':
            vel_mag = np.linalg.norm(np.array(particle.vel))
            RK4_vel.append(vel_mag)
            value = RK4_vel
        elif desired_value == 'position':
            RK4_pos1.append(theta10)
            value1 = RK4_pos1
            RK4_pos2.append(theta20)
            value2 = RK4_pos2

    return value1,value2


rk4(3000,"position")

value1x=[None]*3000
for i in range(0,len(value1)):
    value1x[i]=m1.armlength*np.sin(value1[i])
value1y=[None]*3000
for i in range(0,len(value1)):
    value1y[i]=-m1.armlength*np.cos(value1[i])
value2x=[None]*3000
for i in range(0,len(value2)):
    value2x[i]=m1.armlength*np.sin(value1[i])+m2.armlength*np.sin(value2[i])
value2y=[None]*3000
for i in range(0,len(value2)):
    value2y[i]=-m1.armlength*np.cos(value1[i])-m2.armlength*np.cos(value2[i])



fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-10, 10), ylim=(-10, 5))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)

def init():
    line.set_data([], [])
    return line,# time_text


def animate(i):
    thisx = [0, value1x[i], value2x[i]]
    thisy = [0, value1y[i], value2y[i]]

    line.set_data(thisx, thisy)
    return line, #time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(value1y)),
                              interval=25, blit=True, init_func=init)

plt.show()