import matplotlib.pyplot as plt


F = 2
m = 1
a = F / m
total_time = 60
delta_t = 1
num_steps = total_time/delta_t
dt = []
v = [0]
s = [0]
for i in range(0, int(num_steps), int(delta_t)):
    dt.append(i)
    if i == (total_time - 1):
        break
    elif i != (total_time - 1):
        vf = v[i] + int(a * delta_t)
        v.append(vf)
        sq = s[i] + (v[i] * delta_t) + (0.5 * a * (delta_t ** 2))
        sf = s[i] + (v[i] * dt[i]) + (0.5 * a * (delta_t * delta_t))
        s.append(sf)

print(dt)
print(v)
print(s)


plt.plot(v, dt)
# plt.show()
plt.plot(s, dt)
plt.show()

