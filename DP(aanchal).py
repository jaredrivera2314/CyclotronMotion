import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import scipy.integrate as integrate

L1 = 2.0
L2 = 2.0
M1 = 1.0
M2 = 1.0
g = 9.8
theta1 = 120
thetadot1 = 0.0
theta2 = 0
thetadot2 = 0.0

initial = np.radians([theta1, thetadot1, theta2, thetadot2])


t = []
e = 0.0
for w in range(400):
    t.append(e)
    e = e + 0.05


def update(func, t):
    a = func[1]

    b = ((-g*((2*M1)+M2)*np.sin(func[0])) - (M2*g*np.sin(func[0] - (2*func[2]))) -
         (2*np.sin(func[0] - func[2])*M2*((func[3]**2)*L2 + (func[1]**2)*L1*np.cos(func[0]-func[2]))))/\
        (L1*((2*M1)+M2-(M2*np.cos(2*func[0]-2*func[2]))))

    c = func[3]

    d = (2*np.sin(func[0]-func[2])*(((func[1]**2)*L1*(M1+M2)) + (g*(M1+M2)*np.cos(func[0]))+
                                    ((func[3]**2)*L2*M2*np.cos(func[0]-func[2]))))/\
        (L2*((2*M1)+M2-(M2*np.cos(2*func[0]-2*func[2]))))

    return [a, b, c, d]


yy = integrate.odeint(update, initial, t)

x1 = L1 * np.sin(yy[:, 0])
y1 = -L1 * np.cos(yy[:, 0])
x2 = L2 * np.sin(yy[:, 2]) + x1
y2 = -L2 * np.cos(yy[:, 2]) + y1

fig = plt.figure()
ax = fig.add_subplot(111, xlim=(-5, 5), ylim=(-5, 5))
line, = ax.plot([], [], lw=2)


def init():
    line.set_data([], [])
    return line,


def animate(i):
    x_ = [0, x1[i], x2[i]]
    y_ = [0, y1[i], y2[i]]
    line.set_data(x_, y_)
    return line,


anim = animation.FuncAnimation(fig, animate, 400,
                               interval=25, blit=True, init_func=init)
plt.show()

