import matplotlib.pyplot as plt
import numpy as npy


def cubicPolynom(x):
    return -(1/25)*x**3 - (1/13)*x**2 + 0.25*x


x = npy.arange(-6.0, 6.0, 0.002)

vfunc = npy.vectorize(cubicPolynom)
vfunc(x)

plt.plot(x, vfunc(x), linewidth=1.0)

plt.title('y = -(1/25)*x**3 - (1/13)*x**2 + 0.25*x')
plt.xlabel('x')
plt.ylabel('y')

plt.grid(True)
plt.show()
