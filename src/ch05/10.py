import pylab

xs = pylab.linspace(-2 * pylab.pi, pylab.pi * 2, 10000)
pylab.fill_between(xs, pylab.sin(xs), 0, where=pylab.sin(xs) > 0, color=(0.3, 0.9, 0.9))
pylab.fill_between(xs, pylab.sin(xs), 0.5, where=pylab.sin(xs) > 0.5, color=(0, 0, 0.8))
pylab.fill_between(xs, pylab.sin(xs), 0, where=pylab.sin(xs) <= 0, color=(0, 0.3, 0))
pylab.fill_between(xs, pylab.sin(xs), -0.5, where=pylab.sin(xs) < -0.5, color=(1, 0, 0))

pylab.grid()
pylab.show()
