import random

import pylab

dt = pylab.linspace(0, 12 * pylab.pi, 10000)
xs = pylab.sin(dt) * (
    pylab.exp(pylab.cos(dt)) - 2 * pylab.cos(4 * dt) + (pylab.sin(dt / 12)) ** 5
)
ys = pylab.cos(dt) * (
    pylab.exp(pylab.cos(dt)) - 2 * pylab.cos(4 * dt) + (pylab.sin(dt / 12)) ** 5
)

for i in range(5):
    for j in range(5):
        c = [random.random() for x in range(3)]
        pylab.fill(xs + j * 10, ys + i * 10, color=c)
for i in range(5):
    for j in range(5):
        if i == j or i + j == 4:
            c = [random.random() for x in range(3)]
            pylab.fill(xs + (j + 6) * 10, ys + i * 10, color=c)

pylab.axis("off")
pylab.show()
