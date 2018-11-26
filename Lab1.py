import math
import matplotlib.pyplot as plt
import numpy as np

c = 3.0E8
magnetic_field = [0.0, 0.0, -1.5]  # Tesla


class Particle:
    def __init__(self, position, velocity, charge, mass):
        self.position = position
        self.velocity = velocity
        self.charge = charge
        self.mass = mass

    def period(self, magnetic_field):
        return (2.0 * math.pi * self.mass) / (self.charge * np.linalg.norm(magnetic_field))

    def radius(self):
        return (self.mass * np.linalg.norm(self.velocity)) / (self.charge * np.linalg.norm(magnetic_field))

    def gamma_factor(self):
        return 1.0 / (1.0 - (np.linalg.norm(self.velocity) / c) ** 2.0) ** 0.5


proton = Particle([0.0, 0.0, 0.0], [0.05 * c, 0.0, 0.0], 1.6E-19, 1.67E-27)

hh = proton.period(magnetic_field) / 400
print(hh)


e_max = 5.0E6
n = 2500
T = proton.period(magnetic_field)
ang_freq = (2 * math.pi)/T


def electric_field(time_1):
    e_field = e_max * np.sign(np.cos((ang_freq * time_1) - math.pi / 2))
    return e_field


ee = []
time = 0.0
for p in range(n):
    e = e_max * np.sign(np.cos((ang_freq * time) - math.pi / 2))
    ee.append(e)
    time = time + hh

radius = proton.radius()
gap = (-1) * 0.5 * radius

print("The gap equals to = ", gap)
print("\n")


def acceleration(charge, mass, position, velocity, time_2):
    if position[0] >= 0 or position[0] < gap and position[1] > 0:
        a = (charge * np.cross(velocity, magnetic_field)) / mass
    elif gap < position[0] < 0 and (position[1] > 0):
        a = (charge * electric_field(time_2)) / mass
    elif position[0] >= 0 or position[0] < gap and position[1] < 0:
        a = (charge * np.cross(velocity, magnetic_field)) / mass
    elif gap < position[0] < 0 and (position[1] < 0):
        a = (charge * electric_field(time_2)) / mass
    return a


h = proton.period(magnetic_field) / 400

r0 = np.array(proton.position)
v0 = np.array(proton.velocity)

RK4_position = []
RK4_velocity = []

for i in range(n):
    r1 = r0
    v1 = v0
    l1 = h * v0
    k1 = h * acceleration(proton.charge, proton.mass, r1, v1, (h * i))
    l2 = h * (v1 + (k1 / 2))
    k2 = h * acceleration(proton.charge, proton.mass, r1 + (l1 / 2), v1 + (k1 / 2), (h * i))
    l3 = h * (v1 + (k2 / 2))
    k3 = h * acceleration(proton.charge, proton.mass, r1 + (l2 / 2), v1 + (k2 / 2), (h * i))
    l4 = h * (v1 + k3)
    k4 = h * acceleration(proton.charge, proton.mass, r1 + l3, v1 + k3, (h * i))

    r = r1 + (l1 + (2 * (l2 + l3)) + l4) / 6
    v = v1 + (k1 + (2 * (k2 + k3)) + k4) / 6

    r0 = r
    v0 = v

    RK4_position.append(r)
    RK4_velocity.append(v)

# print(RK4_position)
# print(RK4_velocity)

x = []
y = []
z = []

vx = []
vy = []
vz = []

for i in RK4_position:
    x.append(i[0])
    y.append(i[1])
    z.append(i[2])

for i in RK4_velocity:
    vx.append(i[0])
    vy.append(i[1])
    vz.append(i[2])

print("\n")

vs = [(((x ** 2) + (y ** 2)) ** 0.5) for x, y in zip(vx, vy)]

# print(vs)

t = np.zeros([n])
for i in range(n):
    t[i] = (i * h)


plt.plot(x, y)
plt.show()


plt.plot(t, vs)
plt.plot(t, ee)
plt.show()



