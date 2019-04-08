import matplotlib.pyplot as plt
import numpy as npy


def waveFunction(x):
    return x * npy.sin(1/x)

x = npy.arange(-1.0, 1.0, 0.002)

vfunc = npy.vectorize(waveFunction)
vfunc(x)

plt.plot(x, vfunc(x), linewidth=1.0)

plt.title('y = x * sin(1/x)')
plt.xlabel('x')
plt.ylabel('y')

plt.grid(True)
plt.show()
