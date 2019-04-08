import matplotlib.pyplot as plt
import numpy as npy

x = npy.arange(-8.0, 8.0, 0.001)
exponential_x = npy.exp(x)  # function 1
y_equals_x = x  # function 2

x_plus = npy.arange(0.00001, 8.0, 0.001)  # ln defined for x > 0 only
ln_x = npy.log(x_plus)  # function 3

plotObjects = plt.plot(x, exponential_x, x, y_equals_x, linewidth=1.0)
plotObjects[len(plotObjects):] = plt.plot(x_plus, ln_x, linewidth=1.0)

plt.title('Umkehrfunktion: Spiegelung an 1. Winkelhalbierenden')
plt.legend(plotObjects, ('e^x', '1. Winkelhalbierende', 'ln(x)'))

plt.axis([-8, 8, -8, 8], 'equal')

plt.grid(True)
plt.show()
