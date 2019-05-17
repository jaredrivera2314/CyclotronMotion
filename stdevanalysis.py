from matplotlib import pyplot as plt


n = [30/400, 30/500, 30/600, 30/700, 30/800]


stdev = [0.010900626719684565, 0.0036860616547505953, 0.002239910796947778, 0.002030006740653487, 0.002005339746723398]

comptime = [0.19494128227233887, 0.2164759635925293, 0.2624847888946533, 0.33491063117980957, 0.33598995208740234]

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time step')


ax1.set_ylabel('comp_time', color=color)
ax1.plot(n, comptime, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('stdev', color=color)
ax2.plot(n, stdev, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()



