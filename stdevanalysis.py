from matplotlib import pyplot as plt


n = [30/400, 30/500, 30/600, 30/700, 30/800]

stdev = [1.6527150377497226, 1.6523010313744455, 1.6520143553026985, 1.6518049933779948, 1.6516465489646033]

comptime = [0.04291653633117676, 0.04487895965576172, 0.04787087440490723, 0.04886889457702637, 0.05385589599609375]

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time step')
ax1.set_ylabel('stdev', color=color)
ax1.plot(n, stdev, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('comp_time', color=color)  # we already handled the x-label with ax1
ax2.plot(n, comptime, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
