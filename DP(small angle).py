import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import scipy.integrate as integrate
import time

start = time.time()

L1 = 2.0
L2 = 2.0
M1 = 1.0
M2 = 1.0
g = 9.8
theta1 = 50
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

    b = (g/L1)*((M2/M1)*func[2] - ((M2/M1)+1)*func[0]) - (M2/M1)*(func[0]-func[2])*((func[1])**2 + (L2/L1)*(func[3])**2)

    c = func[3]

    d = (g/L2)*(((M2/M1)+1)*(func[0]-func[2]))+(func[0]-func[2])*((L1/L2)*(1+(M2/M1))*(func[1]**2)+(M2/M1)*(func[3]**2))

    return [a, b, c, d]


yy = integrate.odeint(update, initial, t)

func0 = np.array(yy[:, 0])
func1 = np.array(yy[:, 1])
func2 = np.array(yy[:, 2])
func3 = np.array(yy[:, 3])
PE = []
KE = []

for i in range(len(func0)):
    pe = -(M1 + M2) * g * L1 * np.cos(func0[i]) - M2 * g * L2 * np.cos(func2[i])
    ke = 0.5 * M1 * (L1 ** 2) * (func1[i] ** 2) + 0.5 * M2 * (
                (L1 ** 2) * (func1[i] ** 2) + (L2 ** 2) * (func3[i] ** 2) + 2 * L1 * L2 * func1[i] * func3[i] * np.cos(
                 func0[i] - func2[i]))
    PE.append(pe)
    KE.append(ke)

E = []
for i in range(len(PE)):
    e = PE[i] + KE[i]
    E.append(e)


x1 = L1 * np.sin(yy[:, 0])
y1 = -L1 * np.cos(yy[:, 0])
x2 = L2 * np.sin(yy[:, 2]) + x1
y2 = -L2 * np.cos(yy[:, 2]) + y1

end = time.time()

fig = plt.figure()
ax = fig.add_subplot(111, xlim=(-5, 5), ylim=(-5, 5))
line, = ax.plot([], [], '-o', lw=2)


def init():
    line.set_data([], [])
    return line,


def animate(i):
    x_ = [0, x1[i], x2[i]]
    y_ = [0, y1[i], y2[i]]
    line.set_data(x_, y_)
    return line,


anim = animation.FuncAnimation(fig, animate, 400,
                               interval=40, blit=True, init_func=init)
plt.show()


sd = np.std(E)
print(sd)
print(end - start)