import matplotlib.pyplot as plt
import numpy as npy
from scipy.interpolate import interp1d

x = npy.linspace(0.0, 2*npy.pi, 100)

# original function
plt.plot(x, npy.sin(x), linewidth=1.0, label="sin(x)")

# 8 support points from 0 to 2*Pi
support_points_x = npy.linspace(0.0, 2*npy.pi, 8)
support_points_y = npy.sin(support_points_x)
plt.scatter(support_points_x, support_points_y, c="k")

interpolation_linear = interp1d(support_points_x, support_points_y)
interpolation_cubic = interp1d(
    support_points_x, support_points_y, kind='cubic')
plt.plot(x, interpolation_linear(x), '--', label="linear interpolation")
plt.plot(x, interpolation_cubic(x), '-', label="cubic interpolation")

plt.title('sine approximated with linear and cubic splines')
plt.grid(True)
plt.legend()
plt.show()
