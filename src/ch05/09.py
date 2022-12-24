import pylab

theda = pylab.linspace(0, 2 * pylab.pi, 10000)
xs1 = [-30, 30, 30, -30]
ys1 = [-20, -20, 20, 20]
xs2 = [-30, 90, 90, -30]
ys2 = [-60, -60, 20, 20]
theda2 = 150 * pylab.pi / 180
xs3 = [15 * pylab.cos(0 + i * theda2) for i in range(0, 13)]
ys3 = [15 * pylab.sin(0 + i * theda2) for i in range(0, 13)]

xs = pylab.cos(theda)
ys = pylab.sin(theda)
pylab.fill(xs2, ys2, color=(1, 0, 0))
pylab.fill(xs1, ys1, color=(0, 0, 1))

pylab.fill(xs3, ys3, color=(1, 1, 1))
pylab.fill(xs * 8.5, ys * 8.5, color=(0, 0, 1))
pylab.fill(xs * 7.5, ys * 7.5, color=(1, 1, 1))
pylab.axis("off")
pylab.show()
