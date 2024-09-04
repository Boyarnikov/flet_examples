import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_xlim([0, 10])

scat = ax.scatter(1, 0)
x = np.linspace(0, 10)


def animations():
    for j in range(10):
        for i in range(10):
            scat.set_offsets((x[i], 0))
            yield


a = animations()

def animate(i):
    next(a)

ani = animation.FuncAnimation(fig, animate, repeat=True,
                                    frames=len(x) - 1, interval=500)

plt.show()