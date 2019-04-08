import matplotlib.pyplot as plt
import numpy as npy

t = npy.arange(0.0, 6.4, 0.1)
sin_t = 5*npy.sin(t)
cos_t = 3*npy.cos(t)
plt.plot(t, sin_t, "r4", t, cos_t, "k^:", linewidth=2.0)
# plt.plot(t, sin_t, linewidth=2)
# plt.plot(t, cos_t, "r", linewidth=2)
plt.xlabel('time in seconds')
plt.ylabel('y(t)')
plt.title('5*sin(t) and 3*cos(t) [red]')
plt.grid(True)
plt.show()
