import matplotlib.pyplot as plt
import numpy as npy

x = npy.arange(-8.0, 8.0, 0.001)
x_plus = npy.arange(-8.0, 8.0, 0.001)

y_equals_x = x
ln_x = npy.log(x_plus)
exponential_x = npy.exp(x)

lineObjects = plt.plot(x, ln_x, x, exponential_x, x, y_equals_x, linewidth=1.0)

plt.title('Umkehrfunktion: Spiegelung an 1. Winkelhalbierenden')
plt.legend(lineObjects, ('ln(x)', 'e^x', '1. Winkelhalbierende'))

plt.axis([-8, 8, -8, 8], 'equal')

plt.grid(True)
plt.show()
